from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

#inputs
    
links = []
email = ''
name = 'mohd rizwan akhtar'
summary = ""
experience = ""
recommendation = ""
profile_overview_content = ""



def is_element_present(by,what):
    try:
        driver.find_element(by = by,value = what)
    except NoSuchElementException:
        return False
    return True

def fetchDataFromlinkdin(url):
    driver.get(url)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'profile-overview')))
    if is_element_present(By.CLASS_NAME,'profile-overview'):
       profile_overview_content = driver.find_element_by_xpath("//div[@class='profile-overview']")
       print(profile_overview_content.text)
    if is_element_present(By.ID,'summary'):
      summary = driver.find_element_by_xpath("//section[@id='summary']")
      print(summary.text)
    if is_element_present(By.ID,'experience'):
      experience = driver.find_element_by_xpath("//section[@id='experience']")
      print(experience.text)
    if is_element_present(By.ID,'recommendations'):
      recommendation = driver.find_element_by_xpath("//section[@id='recommendations']")
      print(recommendation.text)
    #print(profile_overview_content,summary,experience,recommendation)

#codes
username ,attherate, domain = email.partition('@')
compName, dot, com = domain.partition('.')
driver = webdriver.Chrome(executable_path = '/Users/standarduser/Downloads/chromedriver')
driver.get('https://www.google.com/')
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(email)    
driver.find_element_by_xpath("//input[@value='Google Search']").click()
while True :
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'g')))
    div_container = driver.find_elements_by_xpath("//div[@class='g']")  
    for div in div_container:
         #print(div.text)
         domain_exist = div.text.replace(" ",'').lower().find(compName)
         name_exist = div.text.replace(" ",'').lower().find(name.replace(" ","").lower())
         if domain_exist> -1 and name_exist > -1 :
             head,sep,tail = div.text.partition('https')
             link,seperator,rest = tail.partition("\n")
             links.append(sep+link)
    if is_element_present(By.ID,'pnnext'):
        driver.find_element_by_xpath("//a[@id = 'pnnext']").click()
    else :
        break


for url in links:
    if(url.__str__().find('linkedin')>0):
        fetchDataFromlinkdin(url.__str__())
    else:
        pass
