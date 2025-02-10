from Shared.driver import driver
from SignIn.SignIn import PerformSignin
from Utils.SelectingJobs import SelectJobs
from Utils.ChangePage import ChangePage
from Utils.ClickJobApply import ClickJobApply
from FillJobForm.FillJobFrom import FillJobForm

link = str(input("Please enter the link to your job page with easy apply applied in filter for more information you can refer to your Github account: "))
email = str(input("Please enter your email address for LinkedIn account: "))
password = str(input("Please enter your password for LinkedIn account:  "))
driver.get(link)

PerformSignin(email=email, password=password)

SelectJobs()