from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver')
driver.get('http://newtours.demoaut.com/')
userName_input = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input'
password_input = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input'
login_submit = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input'
Flight_continue = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td/input'
driver.find_element_by_xpath(userName_input).send_keys("mercury")
driver.find_element_by_xpath(password_input).send_keys("mercury")
driver.find_element_by_xpath(login_submit).click()
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]").click()
FromPort = Select(driver.find_element_by_name("fromPort"))
FromPort.select_by_visible_text('Paris')
FromMonth = Select(driver.find_element_by_name("fromMonth"))
FromMonth.select_by_visible_text('March')
FromDay = Select(driver.find_element_by_name("fromDay"))
FromDay.select_by_visible_text('25')
ToPort = Select(driver.find_element_by_name("toPort"))
ToPort.select_by_visible_text('New York')
ToMonth = Select(driver.find_element_by_name("toMonth"))
ToMonth.select_by_visible_text('April')
ToDay = Select(driver.find_element_by_name("toDay"))
ToDay.select_by_visible_text('3')
Airlines = Select(driver.find_element_by_name('airline'))
Airlines.select_by_visible_text('Unified Airlines')
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]").click()
driver.find_element_by_xpath(Flight_continue).click()
DepartFlight = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input'
driver.find_element_by_xpath(DepartFlight).click()
DepartFlightContinue = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/p/input'
driver.find_element_by_xpath(DepartFlightContinue).click()
FirstName = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[1]/input'
LastName = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input'
MealPrefernce = Select(driver.find_element_by_name('pass.0.meal'))
MealPrefernce.select_by_visible_text('Vegetarian')
CardType = Select(driver.find_element_by_name('creditCard'))
CardType.select_by_visible_text('Visa')
CardNumber = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[6]/td/table/tbody/tr[2]/td[2]/input'
driver.find_element_by_xpath(CardNumber).send_keys("1234123412341234")
CardExpMonth = Select(driver.find_element_by_name('cc_exp_dt_mn'))
CardExpMonth.select_by_visible_text('11')
CardExpYear = Select(driver.find_element_by_name('cc_exp_dt_yr'))
CardExpYear.select_by_visible_text('2010')
SecurePurchase = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[23]/td/input'
driver.find_element_by_xpath(SecurePurchase).click()
Logout = '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[3]/a/img'
driver.find_element_by_xpath(Logout).click()

