import unittest
from math import sqrt, isclose
from common.r3 import R3
from shadow.polyedr import Facet
from tests.matchers import R3ApproxMatcher, R3CollinearMatcher


class TestVoid(unittest.TestCase):

    # Эта грань не является вертикальной
    def test_vertical01(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(0.0, 3.0, 0.0)])
        self.assertFalse(f.is_vertical())

    # Эта грань вертикальна
    def test_vertical02(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(0.0, 0.0, 1.0), R3(1.0, 0.0, 0.0)])
        self.assertTrue(f.is_vertical())

    # Нормаль к этой грани направлена вертикально вверх
    def test_h_normal01(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(0.0, 3.0, 0.0)])
        self.assertEqual(R3CollinearMatcher(f.h_normal()), R3(0.0, 0.0, 1.0))

    # Нормаль к этой грани тоже направлена вертикально вверх
    def test_h_normal02(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(0.0, 3.0, 0.0), R3(3.0, 0.0, 0.0)])
        self.assertEqual(R3CollinearMatcher(f.h_normal()), R3(0.0, 0.0, 1.0))

    # Для нахождения нормали к этой грани рекомендуется нарисовать картинку
    def test_h_normal03(self):
        f = Facet([R3(1.0, 0.0, 0.0), R3(0.0, 1.0, 0.0), R3(0.0, 0.0, 1.0)])
        self.assertEqual(R3CollinearMatcher(f.h_normal()), R3(1.0, 1.0, 1.0))

    # Для каждой из следующих граней сначала «вручную» находятся
    # внешние нормали к вертикальным плоскостям, проходящим через
    # рёбра заданной грани, а затем проверяется, что эти нормали
    # имеют то же направление, что и вычисляемые методом v_normals

    # Нормали для треугольной грани
    def test_v_normal01(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(0.0, 3.0, 0.0)])
        normals = [R3(-1.0, 0.0, 0.0), R3(0.0, -1.0, 0.0), R3(1.0, 1.0, 0.0)]
        for t in zip(f.v_normals(), normals):
            self.assertEqual(R3CollinearMatcher(t[0]), t[1])

    # Нормали для квадратной грани
    def test_v_normal02(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(2.0, 0.0, 0.0),
                   R3(2.0, 2.0, 0.0), R3(0.0, 2.0, 0.0)])
        normals = [R3(-1.0, 0.0, 0.0), R3(0.0, -1.0, 0.0),
                   R3(1.0, 0.0, 0.0), R3(0.0, 1.0, 0.0)]
        for t in zip(f.v_normals(), normals):
            self.assertEqual(R3CollinearMatcher(t[0]), t[1])

    # Нормали для ещё одной треугольной грани
    def test_v_normal03(self):
        f = Facet([R3(1.0, 0.0, 0.0), R3(0.0, 1.0, 0.0), R3(0.0, 0.0, 1.0)])
        normals = [R3(0.0, -1.0, 0.0), R3(1.0, 1.0, 0.0), R3(-1.0, 0.0, 0.0)]
        for t in zip(f.v_normals(), normals):
            self.assertEqual(R3CollinearMatcher(t[0]), t[1])

    # Центр квадрата
    def test_center01(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(2.0, 0.0, 0.0),
                   R3(2.0, 2.0, 0.0), R3(0.0, 2.0, 0.0)])
        self.assertEqual(R3ApproxMatcher(f.center()), (R3(1.0, 1.0, 0.0)))

    # Центр треугольника
    def test_center02(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(0.0, 3.0, 0.0)])
        self.assertEqual(R3ApproxMatcher(f.center()), (R3(1.0, 1.0, 0.0)))

    # Центр грани внутри куба
    def test_cube_center01(self):
        f = Facet([R3(-0.5, -0.5, 0.0), R3(-0.5, 0.5, 0.0),
                   R3(0.5, -0.5, 0.0), R3(0.5, 0.5, 0.0)])
        self.assertEqual(f.is_outside(), False)

    # Центр грани снаружи куба
    def test_cube_center02(self):
        f = Facet([R3(10.0, 5.0, 0.0), R3(10.0, 10.0, 5.0),
                   R3(5.0, 10.0, 5.0), R3(5.0, 5.0, 0.0)])
        self.assertEqual(f.is_outside(), True)

    # Угол больше pi\7
    def test_is_less01(self):
        f = Facet([R3(10.0, 5.0, 0.0), R3(10.0, 10.0, 5.0),
                   R3(5.0, 10.0, 5.0), R3(5.0, 5.0, 0.0)])
        self.assertEqual(f.is_less(), False)

    # Угол меньше pi\7
    def test_is_less02(self):
        f = Facet([R3(10.0, 5.0, 0.0), R3(10.0, 10.0, 0.0),
                   R3(5.0, 10.0, 0.0), R3(5.0, 5.0, 0.0)])
        self.assertEqual(f.is_less(), True)

    # Грань видима целиком
    def test_visible01(self):
        f = Facet([R3(1.0, 1.0, 3.0), R3(6.0, 1.0, 3.0),
                   R3(6.0, 6.0, 3.0), R3(1.0, 6.0, 3.0)])
        f_over = Facet([R3(0.0, 0.0, 0.0), R3(5.0, 0.0, 0.0),
                        R3(5.0, 5.0, 0.0), R3(0.0, 5.0, 0.0)])
        self.assertEqual(f.facet_is_visible([f, f_over]), True)

    # Грань не видима целиком
    def test_visible02(self):
        f_over = Facet([R3(1.0, 1.0, 3.0), R3(6.0, 1.0, 3.0),
                        R3(6.0, 6.0, 3.0), R3(1.0, 6.0, 3.0)])
        f = Facet([R3(0.0, 0.0, 0.0), R3(5.0, 0.0, 0.0),
                   R3(5.0, 5.0, 0.0), R3(0.0, 5.0, 0.0)])
        self.assertEqual(f.facet_is_visible([f, f_over]), False)

    # Грань не видима целиком(т.к. вертикальна)
    def test_visible03(self):
        f_over = Facet([R3(1.0, 0.0, 0.0), R3(-1.0, 0.0, 0.0),
                        R3(1.0, 0.0, 2.0), R3(-1.0, 0.0, 2.0)])
        f = Facet([R3(1.0, 1.0, 3.0), R3(6.0, 1.0, 3.0),
                   R3(1.0, 1.0, 0.0), R3(6.0, 1.0, 0.0)])
        self.assertEqual(f.facet_is_visible([f, f_over]), False)
