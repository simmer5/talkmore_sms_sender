
from selenium import webdriver

#==========SELENIUM STARTS HERE================

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
 
driver = webdriver.Firefox(options=options)

driver.get("https://b.talkmore.no/talkmore3/servlet/SendSmsFromSelfcare")
usr = driver.find_element_by_name('username')
psw = driver.find_element_by_name('password')

usr.send_keys("12345678")#user numeris
psw.send_keys("12345678")#user slaptazodis

sub = driver.find_element_by_link_text('Logg inn')
sub.click()

sms = driver.find_element_by_link_text('Send SMS')
sms.click()

driver.switch_to_frame("ContactListFrame")

tel = driver.find_element_by_xpath('//*[@id="contact_list__phone_number_manual"]')
tel.send_keys("12345678")#gavejo telefono numeris numeris

add_tel = driver.find_element_by_id("addButton")
add_tel.click()

msg = driver.find_element_by_name('sms_templates__message') 
msg.send_keys("This is a message from Python!!! Yeeeeees!!!") #sms zinute
driver.switch_to_default_content()

snd_sms_btn = driver.find_element_by_xpath('//*[@id="content"]/div/form/table[1]/tbody/tr[2]/td/div/a')

snd_sms_btn.click()

print("Baigta!")
