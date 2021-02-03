import unittest
import pyPLTreader
import construct

data = open("1d_sample_data.plt", "rb")

str=data.read()

class TestStringMethods(unittest.TestCase):

    def test_construct_dword(self):
        bytes_to_parse = b"\x01\x00\x00\x00\x00\x00\x00\x01"
        qword_res = pyPLTreader.construct_qword(bytes_to_parse)
        target=72057594037927937
        self.assertEqual(qword_res['Correct'], True)
        self.assertEqual(qword_res['qword'], target)
        bytes_to_parse = b"\x01\x00\x00"
        qword_res = pyPLTreader.construct_qword(bytes_to_parse)
        self.assertEqual(qword_res['Correct'], False)

    def test_construct_qword_for_TecStr(self):
        bytes_to_parse = b"\x2e\x00\x00\x00\x2e\x00\x00\x00"
        qword_res = pyPLTreader.construct_qword(bytes_to_parse)
        self.assertEqual(qword_res['Correct'],True)
        self.assertEqual(qword_res['tec_str'], '..')

    def test_read_magic_number(self):
        #[hex(0x12345678 >> i & 0xff) for i in (24, 16, 8, 0)]
        mag_res = pyPLTreader.read_magic_number(b"\x23\x21\x54\x44\x56\x31\x31\x32")
        self.assertEqual(mag_res['Correct'], True)
        self.assertEqual(mag_res['uni_chars'], '#!TDV112')

    def test_read_headerr(self):
        #[hex(0x12345678 >> i & 0xff) for i in (24, 16, 8, 0)]
        mag_res = pyPLTreader.read_header(str)

        self.assertEqual(mag_res['Correct'], True)
        self.assertEqual(mag_res['magic_num']['uni_chars'], '#!TDV112')
        self.assertEqual(mag_res['ByteOrder'], 1)
        self.assertEqual(mag_res['FileType'], 'FULL')
        self.assertEqual(mag_res['NumVars'], 3)
        self.assertEqual(mag_res['Title'], '')


if __name__ == '__main__':
    unittest.main()
