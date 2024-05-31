import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box1.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_area(self):
        self.polyedr.result()
        self.assertAlmostEqual(self.polyedr.area, 0.0)


class TestPolyedr2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	6	24
0.5	0.5	1.5
0.5	1.5	1.5
1.5	1.5	1.5
1.5	0.5	1.5
0.5	0.5	0.5
0.5	1.5	0.5
1.5	1.5	0.5
1.5	0.5	0.5
4	1    2    3    4
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5
4	8    7    6    5"""
        fake_file_path = 'data/my_cube.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 6)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 24)

    def test_area(self):
        self.polyedr.result()
        self.assertAlmostEqual(self.polyedr.area, 0.7071067811865477)


class TestPolyedr3(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """40.0	45.0	-30.0	-60.0
8	2	8
1.0 8.0 0.0
20.0 8.0 0.0
20.0 11.0 0.0
1.0 11.0 0.0
6.0 6.0 8.0
11.0 6.0 8.0
11.0 11.0 8.0
6.0 11.0 8.0
4	1    2    3    4
4	5    6    7    8"""
        fake_file_path = 'data/planes.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)

    def test_area(self):
        self.polyedr.result()
        self.assertAlmostEqual(self.polyedr.area, 21.65063509461097)


class TestPolyedr4(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """10.0	45.0	-30.0	-60.0
10	2	10
1.0 8.0 0.0
20.0 8.0 0.0
20.0 11.0 0.0
1.0 11.0 0.0
6.0 6.0 8.0
11.0 6.0 8.0
13.0 7.0 8.0
11.0 11.0 8.0
6.0 11.0 8.0
5.0 8.0 8.0
4	1    2    3    4
6	5    6    7    8    9    10"""
        fake_file_path = 'data/planes2.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 10)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 10)

    def test_area(self):
        self.polyedr.result()
        self.assertAlmostEqual(self.polyedr.area, 28.14582562299426)


class TestPolyedr5(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	60.0	-140.0	60.0
8	5	20
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	1    2    3    4
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 5)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 20)

    def test_area(self):
        self.polyedr.result()
        self.assertAlmostEqual(self.polyedr.area, 0.0)
