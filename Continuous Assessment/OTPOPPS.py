import random 
import re 
import smtplib

class otpSharing:
    def __init__(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)  
            self.server.ehlo()
            self.server.starttls()
            self.senderEmail = 'xxxxxxxxxxxxxx@gmail.com'
            self.senderPass = 'xxxx xxxx xxxx xxxx'
            self.server.login(self.senderEmail, self.senderPass)
        except:
            print("Unable to connect to the SMTP server")
            exit()

        self.otp = None
        for i in range(3): 
            self.eMail = input("Enter email id: ")
            if self.isEmail(self.eMail):
                break
            else:
                print("Invalid email id!!!")
        else:
            print("You've entered an invalid email too many times!!! \n Try again later...")
            exit()


    def isEmail(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
        if re.fullmatch(regex,email): #checking if the entered email matches the template
            return True
        else:
            return False

    def generateOTP(self, n):
        otp=""
        for i in range(n):
            otp+=str(random.randint(0,9))
        return(otp)

    def verifyOTP(self):
        print("Verify your email id: ")
        OTP = input("Enter the OTP: ")
        if OTP==self.otp:
            print("Email ID successfully verified...")
        else:
            print("Invalid OTP")
    def sendEmail(self,n):
        self.server.sendmail(self.senderEmail, self.eMail, "Subject:OTP\nYour OTP using OOP is " + self.otp) 
        print("An {} digit OTP has been sent to {}".format(n, self.eMail))



if __name__=='__main__':
    obj=otpSharing()
    n=int(input("Enter the OTP length: "))
    obj.otp=obj.generateOTP(n)
    obj.sendEmail(n)
    obj.verifyOTP()
    obj.server.close()
