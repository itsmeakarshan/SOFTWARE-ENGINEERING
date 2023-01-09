import unittest
import MYOTP

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        Email = MYOTP.validate_email('akarshanrasyal04@gmail.com')
        self.assertEquals(True,Email)

    def testcase2(self):
        size = 4
        OTP = MYOTP.generate_otp()
        self.assertEqual(len(OTP), size)

    def testcase3(self):
        Email = MYOTP.send_mail("8080")
        self.assertEquals(True,Email)

if __name__ == '__main__':
    unittest.main()