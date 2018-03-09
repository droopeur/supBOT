# -*-coding:utf-8 -*

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
import time

categorie = 'accessories'
Keywords = ['20L','SIGG']
size = 'Large'
adress = { 'street' : '132 Rue des plantes en pot', 'city' : 'Meudon', 'zip': '80000', 'country': 'FRANCE'}
card = { 'number': '5467 8767 0321 4532', 'month' : '07', 'year' : '2020', 'ccv' : '994'}
userInfos = { 'email': 'droopeur@outlook.com', 'name' : 'Droopeur Rx', 'phoneNumber' : '0623771287', 'adress' : adress, 'card' : card}


def launchDriver():
    global browser
    browser = webdriver.Firefox()
    browser.get(('http://www.supremenewyork.com/shop/all/'))

def goToCat():
    browser.find_element_by_xpath('//*[@href="/shop/all/'+categorie+'"]').click()
    test = True
    while test:
        time.sleep(1)
        print('diff')
        loc = browser.find_element_by_xpath('//*[@class="current"]').text
        if loc  == 'accessories':
            test= False
            break
def selectArticle():
    print(browser.current_url)
    while browser.current_url == 'http://www.supremenewyork.com/shop/all/'+categorie :
        try:
            art= None
            ind = 0
            for kw in Keywords:
                print(kw)
                try:
                    art = browser.find_element_by_xpath("//*[text()[contains(.,'"+kw+"')]]")
                    art.click()
                    ActionChains(browser).move_to_element(art).click()
                    print(art.text)
                    break
                except:
                    pass

        except:
            print("No matches, item hasn't dropped yet or you have to select by yourself")
            try:
                WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'"+Keywords[0]+"')]]"))
                )
            except:
                pass
            browser.refresh()
def selectSize():
    try:
        WebDriverWait(browser, 2).until(
          EC.presence_of_element_located((By.ID, 'size'))
     )
        elt = Select(browser.find_element_by_id('size'))
        elt.select_by_visible_text(size)
    except:
        print('size not aviable or item is unisize, default size as been selected')



def monitor():
    print('Monitor Mode')
    soldOut=True
    while soldOut :

        try:
            WebDriverWait(browser, 15).until(
                    EC.presence_of_element_located((By.NAME, 'commit'))
                    )
            soldOut=False
        except:
            browser.refresh()
    browser.find_element_by_name('commit').click()
    browser.find_element_by_xpath('//*[@class="button checkout"]').click()




def checkout():
    while True:
        try:
            if browser.find_element_by_name('credit_card[vval]').get_attribute("value")=='':

                browser.find_element_by_id('order_email').send_keys(userInfos['email'])
                browser.find_element_by_id('order_billing_name').send_keys(userInfos['name'])
                browser.find_element_by_id('order_tel').send_keys(userInfos['phoneNumber'])
                browser.find_element_by_name('order[billing_address]').send_keys(userInfos['adress']['street'])
                browser.find_element_by_id('order_billing_city').send_keys(userInfos['adress']['city'])
                browser.find_element_by_id('order_billing_zip').send_keys(userInfos['adress']['zip'])
                selectcountry = Select(browser.find_element_by_id('order_billing_country'))
                selectcountry.select_by_visible_text(userInfos['adress']['country'])
                browser.find_element_by_name('credit_card[cnb]').send_keys(userInfos['card']['number'])
                selectMonth = Select(browser.find_element_by_name('credit_card[month]'))
                selectMonth.select_by_visible_text(userInfos['card']['month'])
                selectYear = Select(browser.find_element_by_name('credit_card[year]'))
                selectYear.select_by_visible_text(userInfos['card']['year'])
                browser.find_element_by_name('credit_card[vval]').send_keys(userInfos['card']['ccv'])
                selectBox = browser.find_element_by_id('order_terms')
                ActionChains(browser).move_to_element(selectBox).click().perform()
                browser.find_element_by_name('commit').click()
        except:
            pass

launchDriver()
goToCat()
selectArticle()
selectSize()
monitor()
checkout()