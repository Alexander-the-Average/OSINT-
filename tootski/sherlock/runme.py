


# taking the email adress an input
def emailInput():
    global user
    email=str(input("enter your desired E-mail Address:"))
    print(email)

    f=email.find('@')
    s1=slice(f)
    user=email[s1]
    print("the taken username is ",user)




emailInput()


#executing the OSINT tool in shell 
def profileScraper():
    import os

    os.system('cls')

    cmd="sherlock.py " + user
    print(cmd)

    os.system(cmd)
    global a
    lookup = 'twitter'
    inline= user  + ".txt"
    with open(inline) as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                print ('found at line:', num )   

    with open(inline) as openfile:
        for line in openfile:
            if "twitter" in line:
                a= line
    print(a)            
    






profileScraper()




#extracting name from twitter handle

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os




options=Options()
#options.headless=True
#driver = webdriver.Chrome("chromedriver.exe",options=options)
driver = webdriver.Chrome("chromedriver.exe")
#driver.minimize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)
#user="https://twitter.com/mehuljindal18"
driver.get(a)
driver.implicitly_wait(10)

for elem in driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/h2/div/div/div/span[1]/span/span'):
    print (elem.text)
name=elem.text


#linkedin login with dummy account

driver.get("https://www.linkedin.com/")

driver.implicitly_wait(10)

loginID= driver.find_element_by_xpath('//*[@id="session_key"]')

loginID.send_keys("jkhsadfuygwehsejfvjsfvgdyvgehvrjwvseyrjhvasdfjhvasjh@outlook.com")

passwd= driver.find_element_by_xpath('//*[@id="session_password"]')

passwd.send_keys("Qwerty123hhhgggddttj")

passwd.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

searchBar=driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')

searchBar.send_keys(name)

searchBar.send_keys(Keys.RETURN)

viewProfile=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div/a/div/div[2]/a/div/span')

viewProfile.click()

contactTag= driver.find_element_by_xpath('//*[@id="top-card-text-details-contact-info"]')

contactTag.click()

url=driver.current_url

driver.maximize_window()


os.system('clear')

print("LinkedIn profile is : \n",url)









