import unittest
import smtplib
import OTPwithfuncdecom as O1

Name="Akarshan"
Email="akarshan4@gmail.com"

class BetweenAssertMixin(object):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (x, low, hi))
        
class Test_otp(unittest.TestCase,BetweenAssertMixin):
    def testcase1(self):
        print("TestCase 1:")

        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        otp = O1.generate_otp(4)
        self.assertBetween(len(otp),4,8)

        O1.send_email()
        print()

    def testcase2(self):
        print("TestCase 2")

        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "@" and "." and "com" and "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        otp = O1.generate_otp(5)
        self.assertBetween(len(otp),4,8)

        O1.send_email()
        print()

    def testcase3(self):
        print("TestCase 3")
        
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        otp = O1.generate_otp(9)
        self.assertBetween(len(otp),4,8)
        O1.send_email()
        
unittest.main()

