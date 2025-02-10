from Shared.driver import driver
from SignIn.SignIn import PerformSignin
from Utils.SelectingJobs import SelectJobs
from Utils.ChangePage import ChangePage
from Utils.ClickJobApply import ClickJobApply
from FillJobForm.FillJobFrom import FillJobForm
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4053507858&f_AL=true&geoId=102713980&keywords=web%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')

PerformSignin(email='siddharthsingh9361@gmail.com', password='siddharth@123$')

SelectJobs()