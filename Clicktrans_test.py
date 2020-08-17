from selenium import webdriver

pageUrl = 'https://dev-1.clicktrans.pl/register-test/courier'
cdrvPath = 'D://Dokumenty//Scimitar//Chromedriver//chromedriver.exe' #Sciezka do chromedriver
driver = webdriver.Chrome(cdrvPath)

driver.get(pageUrl)
driver.fullscreen_window()
driver.find_element_by_id('user_register_company_name').send_keys('Abakus Sp. z o.o.')
driver.find_element_by_id('user_register_email').send_keys('email@domain.com')
driver.find_element_by_id('user_register_name').send_keys('Adam Kowalski')
driver.find_element_by_id('user_register_phone').send_keys('999888777')
driver.find_element_by_id('user_register_plainPassword').send_keys('123qweasd')
driver.find_element_by_id('user_register_settings_agreementRegulations').click()
driver.find_element_by_id('user_register_settings_agreementPersonalData').click()
driver.find_element_by_id('user_register_settings_agreementMarketing').click()
driver.find_element_by_id('user_register_submit').click()
msg = str(driver.find_element_by_css_selector('body > div.ui.container.flashmsg > div').text)
assert msg == 'OK - some registration logic is mocked!'
print('Formularz został wysłany poprawnie!!!')
driver.quit()
