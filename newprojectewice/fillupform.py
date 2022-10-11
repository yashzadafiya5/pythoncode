from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import requests
import time
browser=''
# wait = WebDriverWait(driver, 10)
# Start of login
def fill_till_3():
option=webdriver.ChromeOptions()
name=["param patel"]
browser=webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\chromedriver.exe")
browser.get("https://ewise.paramounttpa.com/")
loginusername=browser.find_element("name","inpUserName")
loginpassword=browser.find_element("name","inpPassword")
submit=browser.find_element("name","btnLogin")
loginusername.send_keys('11727')
loginpassword.send_keys('Osho@2232')
submit.click()
# End of login
# Start of getting to claim investigation page
browser.get("https://ewise.paramounttpa.com/ProductSelection.aspx")
time.sleep(3)
ewise_button=browser.find_element(By.ID,"anchrEWISE")
ewise_button.click()
browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727")
time.sleep(3)
image=browser.find_element(By.ID,"dvRightArrow")
image.click()
time.sleep(3)
investigation_btn=browser.find_element(By.ID,"anchrInvest")
investigation_btn.click()
browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727")
time.sleep(3)
claim_inv=browser.find_element(By.ID,"anchrFRD")
claim_inv.click()
browser.get("https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==")
# End of getting to claim investigation page
# Start of finding form fill up
time.sleep(3)
ccnnumber=browser.find_element(By.ID,"txtCcnSrch6")
ccnnumber.send_keys('5593992')
btnactive=browser.find_element(By.ID,"btnSearchActive")
btnactive.click()
time.sleep(3)
btninvestigate = browser.find_element(By.ID,"anchrInvestigate1")
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(btninvestigate).click(btninvestigate).perform()
time.sleep(5)
btnfillform = browser.find_element(By.ID,"anchrEditFir")
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(btnfillform).click(btnfillform).perform()
time.sleep(5)
p = browser.current_window_handle
parent = browser.window_handles[0]
chld = browser.window_handles[1]
browser.switch_to.window(chld)
print("Page title for browser tab:")
print(browser.title)
get_url = browser.current_url
print("The current url is:"+str(get_url))
time.sleep(5)
browser.get(get_url)
# End of finding form fill up
# Start of form filling 
# Start of patient detail
browser.find_element(By.ID,"txtPresentingComplintPatient").clear()
presenting_complain=browser.find_element(By.ID,"txtPresentingComplintPatient")
presenting_complain.send_keys('headache finally diagnosed with Acute Viral Fever With Upper Respiratory Tract Infection')
patient_vef = Select(browser.find_element(By.ID,'ddlPatientVerifiction'))
# select by visible text
patient_vef.select_by_visible_text('Yes')
emp_vef=Select(browser.find_element(By.ID,'ddlEmployerVerification'))
emp_vef.select_by_visible_text('Self Employed')
browser.find_element(By.ID,"txtPatientcurrentcondition").clear()
current_con=browser.find_element(By.ID,"txtPatientcurrentcondition")
current_con.send_keys('Under Treatment')
save_pat_detail=browser.find_element(By.ID,"btnSavePatient")
save_pat_detail.click()
WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
# End of patient detail
# Start of Ailment details
aliment_detail=browser.find_element(By.XPATH,'//*[@id="__tab_TabPanel2"]')
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(aliment_detail).click(aliment_detail).perform()
aliment_detail.click()
mode_treat=Select(browser.find_element(By.ID,'ddlModeTreatmen'))
mode_treat.select_by_visible_text('Surgical')
time.sleep(2)
save_pat_detail=browser.find_element(By.ID,"btnSaveMLCDetails")
save_pat_detail.click()
time.sleep(5)
WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
# End of Ailment details
# Start of hospital details
hospital_detail=browser.find_element(By.ID,"__tab_TabPanel3")
hospital_detail.click()
hospital_vef=Select(browser.find_element(By.ID,'ddlHospitalizationDetailsVerified'))
hospital_vef.select_by_visible_text('Yes')
browser.find_element(By.ID,"txtHospitalauthorityname").clear()
hos_authority=browser.find_element(By.ID,"txtHospitalauthorityname")
hos_authority.send_keys('Parth prajapati - 6359622244')
doa=browser.find_element(By.ID,"txtDOA")
doa.send_keys("30/07/2022")
doa.click()
dod=browser.find_element(By.ID,"txtDOD")
dod.send_keys("02/08/2022")
dod.click()
time.sleep(5)
roomcate=Select(browser.find_element(By.ID,'ddlRoomcategory'))
roomcate.select_by_visible_text('Semi deluxe')
browser.find_element(By.ID,"txtHospitalBillAmt").clear()
hos_amount=browser.find_element(By.ID,"txtHospitalBillAmt")
hos_amount.send_keys('37000')
modeOfPayment=Select(browser.find_element(By.ID,'ddlModeofPayment'))
modeOfPayment.select_by_visible_text('Cash')
hos_visit=Select(browser.find_element(By.ID,'ddlhospitalvisit'))
hos_visit.select_by_visible_text('No')
phone_call=Select(browser.find_element(By.ID,'ddlPhoneCall'))
phone_call.select_by_visible_text('Yes')
response_hospital=Select(browser.find_element(By.ID,'ddlResFrmHospital'))
response_hospital.select_by_visible_text('Cooperative')
save_hos_detail=browser.find_element(By.ID,"btnSaveHospitalDetails")
save_hos_detail.click()
WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
# End of hospital details
def fill_after_3():
# start of pharmacy 
pharmy=browser.find_element(By.ID,"__tab_TabPanel4")
pharmy.click()
pharmy_save=browser.find_element(By.ID,"btnPharmacyPathologyRadiologyDetails")
pharmy_save.click()
WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
# end of pharmacy
# Start of treating doctor detail
treating_doctor_detail=browser.find_element(By.ID,"__tab_TabPanel5")
treating_doctor_detail.click()
trt_name=browser.find_element(By.ID,"txtNameofTreatingDoctor")
trt_name.send_keys('Dr parth prajapati')
trt_qua=browser.find_element(By.ID,'txtTreatingDoctorQualification')
trt_qua.send_keys('Physician ')
trt_number=browser.find_element(By.ID,'txtConsultantContactNo')
trt_number.send_keys('6359622244')
trt_reg=browser.find_element(By.ID,'lblTreatingDoctorsRegistrationnumber')
trt_reg.send_keys('  ')
save_trt_details=browser.find_element(By.ID,"btnTreatingDoctorDetails")
save_trt_details.click()
WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
# End of treating doctor detail
# start of PHS conclusion
PHS_con=browser.find_element(By.ID,"__tab_TabPanel6")
PHS_con.click()
inv_done=browser.find_element(By.ID,"txtInvestigationDate")
inv_done.send_keys("22/08/2022")
inv_done.click()
inv_name=Select(browser.find_element(By.ID,"ddlclaimInvestigator"))
inv_name.select_by_visible_text('Ankit Patel (Ahmedabad)')
inv_matrix=Select(browser.find_element(By.ID,"ddlInvestigationMatrix"))
inv_matrix.select_by_visible_text('150-200 kms')
inv_result=Select(browser.find_element(By.ID,'ddlCaseResult'))
inv_result.select_by_visible_text('Clean')
inv_summary=browser.find_element(By.ID,'txtCaseSummary')
summary='''A)	Investigation Summary 
Post verification of this case with
Hospital authority (Name : parth prajapati  and Contact No : 6359622244
and
Patient Name:  A R ANISH   and Contact No : 9520236547 
we confirmed that:
1.	Patient   A R ANISH   was admitted at   CHHANI MULTISPECIALITY HOSPITAL / Vadodara /    from  30/07/2022   till   02/08/2022 
2.	Patient was admitted in a Semi dulex ward, under care of treating Dr. parth parajapati [ physician      ]
3.	Patient had complaints of headache finally diagnosed with Acute Viral Fever With Upper Respiratory Tract Infection .
4.	Patient was kept under medical management and has paid a total of Rs.37000/- in cash towards hospital final bill including Pharmacy bills, Lab bills and other bills.
5.	 CHHANI MULTISPECIALITY HOSPITAL / Vadodara /    consists of 39 beds with all in-house facility of pharmacy and pathology and we have also checked all pharmacy bills, lab bills and lab reports with respective pharmacy and laboratory of hospital.
6.	As per desktop verification, Insured KYC details and doctor registration details found to be genuine.
7.	Evidence :
Audio Recording
B)	Conclusion
The case seems to be clean and hence recommend to process as per policy terms and conditions
'''
inv_summary.send_keys(summary)
save_phs_con=browser.find_element(By.ID,"btnSavePatient")
save_phs_con.click()
WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
# end  of PHS conclusion
time.sleep(10)
get_url = browser.current_url
print("The current url is:"+str(get_url))
button = browser.find_element(By.ID,"anchrEWISE")
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(button).click(button).perform()
browser.get("https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==")
ccnnumber=browser.find_element(By.ID,"txtCcnSrch6")
ccnnumber.send_keys('5593992')
btnactive=browser.find_element(By.ID,"btnSearchActive")
btnactive.click()
time.sleep(60)
website_form='https://ewise.paramounttpa.com/ProductSelection.aspx'
response = requests.get(website_form, data={'name':name})
print("name is "+response.text)
response_got=response.text
file1=open('form_data.txt','w')
file1.write(response_got)
file1.close()
summary='''
    A)	Investigation Summary 
    Post verification of this case with
    Hospital authority (Name : parth prajapati  and Contact No : 6359622244
    and
    Patient Name:  A R ANISH   and Contact No : 9520236547 
    we confirmed that:
    1.	Patient   A R ANISH   was admitted at   CHHANI MULTISPECIALITY HOSPITAL / Vadodara /    from  30/07/2022   till   02/08/2022 
    2.	Patient was admitted in a Semi dulex ward, under care of treating Dr. parth parajapati [ physician      ]
    3.	Patient had complaints of headache finally diagnosed with Acute Viral Fever With Upper Respiratory Tract Infection .
    4.	Patient was kept under medical management and has paid a total of Rs.37000/- in cash towards hospital final bill including Pharmacy bills, Lab bills and other bills.
    5.	 CHHANI MULTISPECIALITY HOSPITAL / Vadodara /    consists of 39 beds with all in-house facility of pharmacy and pathology and we have also checked all pharmacy bills, lab bills and lab reports with respective pharmacy and laboratory of hospital.
    6.	As per desktop verification, Insured KYC details and doctor registration details found to be genuine.
    7.	Evidence :
    Audio Recording
    B)	Conclusion
    The case seems to be clean and hence recommend to process as per policy terms and conditions    
    '''
def fill_form(firnumber,precomplain,con_condition,modtreatment,hospital_auth_detail,pat_doa,pat_dod,room_cate,hos_bill,modeofpay,treat_doc,treat_qualf,treat_number,treat_reg,investigation_date,summary):
try:
    option=webdriver.ChromeOptions()
    name=["param patel"]
    browser=webdriver.Chrome(executable_path="C:\chromedriver.exe")
    browser.get("https://ewise.paramounttpa.com/")
    loginusername=browser.find_element("name","inpUserName")
    loginpassword=browser.find_element("name","inpPassword")
    submit=browser.find_element("name","btnLogin")
    loginusername.send_keys('11727')
    loginpassword.send_keys('Osho@2232')
    submit.click()
    # End of login
    # Start of getting to claim investigation page
    browser.get("https://ewise.paramounttpa.com/ProductSelection.aspx")
    time.sleep(3)
    ewise_button=browser.find_element(By.ID,"anchrEWISE")
    ewise_button.click()
    browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727")
    time.sleep(3)
    image=browser.find_element(By.ID,"dvRightArrow")
    image.click()
    time.sleep(3)
    investigation_btn=browser.find_element(By.ID,"anchrInvest")
    investigation_btn.click()
    browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727")
    time.sleep(3)
    claim_inv=browser.find_element(By.ID,"anchrFRD")
    claim_inv.click()
    browser.get("https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==")
    # End of getting to claim investigation page
    # Start of finding form fill up
    time.sleep(3)
    ccnnumber=browser.find_element(By.ID,"txtCcnSrch6")
    ccnnumber.send_keys(firnumber)
    btnactive=browser.find_element(By.ID,"btnSearchActive")
    btnactive.click()
    time.sleep(3)
    btninvestigate = browser.find_element(By.ID,"anchrInvestigate1")
    browser.implicitly_wait(10)
    ActionChains(browser).move_to_element(btninvestigate).click(btninvestigate).perform()
    time.sleep(5)
    btnfillform = browser.find_element(By.ID,"anchrEditFir")
    browser.implicitly_wait(10)
    ActionChains(browser).move_to_element(btnfillform).click(btnfillform).perform()
    time.sleep(5)
    p = browser.current_window_handle
    parent = browser.window_handles[0]
    chld = browser.window_handles[1]
    browser.switch_to.window(chld)
    print("Page title for browser tab:")
    print(browser.title)
    get_url = browser.current_url
    print("The current url is:"+str(get_url))
    time.sleep(5)
    browser.get(get_url)
    # End of finding form fill up
    # Start of form filling 
    # Start of patient detail
    browser.find_element(By.ID,"txtPresentingComplintPatient").clear()
    presenting_complain=browser.find_element(By.ID,"txtPresentingComplintPatient")
    presenting_complain.send_keys(precomplain)
    patient_vef = Select(browser.find_element(By.ID,'ddlPatientVerifiction'))
    # select by visible text
    patient_vef.select_by_visible_text('Yes')
    emp_vef=Select(browser.find_element(By.ID,'ddlEmployerVerification'))
    emp_vef.select_by_visible_text('Self Employed')
    browser.find_element(By.ID,"txtPatientcurrentcondition").clear()
    current_con=browser.find_element(By.ID,"txtPatientcurrentcondition")
    current_con.send_keys(con_condition)
    save_pat_detail=browser.find_element(By.ID,"btnSavePatient")
    save_pat_detail.click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # End of patient detail
    # Start of Ailment details
    aliment_detail=browser.find_element(By.XPATH,'//*[@id="__tab_TabPanel2"]')
    browser.implicitly_wait(10)
    ActionChains(browser).move_to_element(aliment_detail).click(aliment_detail).perform()
    aliment_detail.click()
    mode_treat=Select(browser.find_element(By.ID,'ddlModeTreatmen'))
    mode_treat.select_by_visible_text(modtreatment)
    time.sleep(2)
    save_pat_detail=browser.find_element(By.ID,"btnSaveMLCDetails")
    save_pat_detail.click()
    time.sleep(5)
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # End of Ailment details
    # Start of hospital details
    hospital_detail=browser.find_element(By.ID,"__tab_TabPanel3")
    hospital_detail.click()
    hospital_vef=Select(browser.find_element(By.ID,'ddlHospitalizationDetailsVerified'))
    hospital_vef.select_by_visible_text('Yes')
    browser.find_element(By.ID,"txtHospitalauthorityname").clear()
    hos_authority=browser.find_element(By.ID,"txtHospitalauthorityname")
    hos_authority.send_keys(hospital_auth_detail)
    doa=browser.find_element(By.ID,"txtDOA")
    doa.send_keys(pat_doa)
    doa.click()
    dod=browser.find_element(By.ID,"txtDOD")
    dod.send_keys(pat_dod)
    dod.click()
    time.sleep(5)
    roomcate=Select(browser.find_element(By.ID,'ddlRoomcategory'))
    roomcate.select_by_visible_text(room_cate)
    browser.find_element(By.ID,"txtHospitalBillAmt").clear()
    hos_amount=browser.find_element(By.ID,"txtHospitalBillAmt")
    hos_amount.send_keys(hos_bill)
    modeOfPayment=Select(browser.find_element(By.ID,'ddlModeofPayment'))
    modeOfPayment.select_by_visible_text(modeofpay)
    hos_visit=Select(browser.find_element(By.ID,'ddlhospitalvisit'))
    hos_visit.select_by_visible_text('No')
    phone_call=Select(browser.find_element(By.ID,'ddlPhoneCall'))
    phone_call.select_by_visible_text('Yes')
    response_hospital=Select(browser.find_element(By.ID,'ddlResFrmHospital'))
    response_hospital.select_by_visible_text('Cooperative')
    save_hos_detail=browser.find_element(By.ID,"btnSaveHospitalDetails")
    save_hos_detail.click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # End of hospital details
except TimeoutException as ex:
    print("this is ohk")
    print("Exception has been thrown. " + str(ex))
    # start of pharmacy 
    pharmy=browser.find_element(By.ID,"__tab_TabPanel4")
    pharmy.click()
    pharmy_save=browser.find_element(By.ID,"btnPharmacyPathologyRadiologyDetails")
    pharmy_save.click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # end of pharmacy
    # Start of treating doctor detail
    browser.find_element(By.ID,"__tab_TabPanel5").clear()
    treating_doctor_detail=browser.find_element(By.ID,"__tab_TabPanel5")
    treating_doctor_detail.click()
    browser.find_element(By.ID,"txtNameofTreatingDoctor").clear()
    trt_name=browser.find_element(By.ID,"txtNameofTreatingDoctor")
    trt_name.send_keys(treat_doc)
    browser.find_element(By.ID,'txtTreatingDoctorQualification').clear()
    trt_qua=browser.find_element(By.ID,'txtTreatingDoctorQualification')
    trt_qua.send_keys(treat_qualf)
    browser.find_element(By.ID,'txtConsultantContactNo').clear()
    trt_number=browser.find_element(By.ID,'txtConsultantContactNo')
    trt_number.send_keys(treat_number)
    browser.find_element(By.ID,'lblTreatingDoctorsRegistrationnumber').clear()
    trt_reg=browser.find_element(By.ID,'lblTreatingDoctorsRegistrationnumber')
    trt_reg.send_keys(treat_reg)
    save_trt_details=browser.find_element(By.ID,"btnTreatingDoctorDetails")
    save_trt_details.click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # End of treating doctor detail
    # start of PHS conclusion
    PHS_con=browser.find_element(By.ID,"__tab_TabPanel6")
    PHS_con.click()
    inv_done=browser.find_element(By.ID,"txtInvestigationDate")
    inv_done.send_keys(investigation_date)
    inv_done.click()
    inv_name=Select(browser.find_element(By.ID,"ddlclaimInvestigator"))
    inv_name.select_by_visible_text('Ankit Patel (Ahmedabad)')
    inv_matrix=Select(browser.find_element(By.ID,"ddlInvestigationMatrix"))
    inv_matrix.select_by_visible_text('150-200 kms')
    inv_result=Select(browser.find_element(By.ID,'ddlCaseResult'))
    inv_result.select_by_visible_text('Clean')
    browser.find_element(By.ID,'txtCaseSummary').clear()
    inv_summary=browser.find_element(By.ID,'txtCaseSummary')
    for i in summary:
        inv_summary.send_keys(i)
    save_phs_con=browser.find_element(By.ID,"btnSavePHSConclusion")
    save_phs_con.click()
    browser.implicitly_wait(10)
    ActionChains(browser).move_to_element(save_phs_con).click(save_phs_con).perform()
    time.sleep(5)
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # end  of PHS conclusion
    time.sleep(10)
    print("form fillied succesfully")



