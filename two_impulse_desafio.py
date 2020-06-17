from Utils.Generic_Web_Testing_Methods import *
from Utils.Generic_reporting import *
from selenium import webdriver



browser = webdriver.Chrome(executable_path='C:\selenium_drivers\chromedriver.exe')

browser.get('https://dev.hiringcue.com')

# create the html report file
#
date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
report_file_name = 'Output\\Two_Impulse_desafio_Report%s.html' % date_time_string
report_file_stream = open (report_file_name, mode = 'w')

page_title = "Two Impulse Desafio Técnico Test Case"

write_the_report_header(report_file_stream, page_title)


# introduce the email

send_keys_to_element_by_xpath(browser,"//input[@id='username']","wilson.edgar@twoimpulse.com",report_file_stream)

time.sleep(5)

# introduce the password

send_keys_to_element_by_xpath(browser,"//input[@id='password']","kopfy2-ruprym-tYcweb",report_file_stream)

time.sleep(5)

# click on login

click_on_element_by_xpath(browser,"//button[@id='btn-login']",report_file_stream)

time.sleep(5)

# click on skip tour

click_on_element_by_xpath(browser,"//*[(text() = 'Skip tour' or . = 'Skip tour')]",report_file_stream)

time.sleep(5)

# click on buy credits

click_on_element_by_xpath(browser,"//button[@id='link-buy-credits ']",report_file_stream)

time.sleep(5)

# introduce the number of credits to buy

send_keys_to_element_by_xpath(browser,"//input[@id='credits-input']","10",report_file_stream)

time.sleep(5)

# press twice on "pay with card"


click_on_element_by_xpath(browser,"//*[(text() = 'Pay with Card' or . = 'Pay with Card')]",report_file_stream)

time.sleep(5)


click_on_element_by_xpath(browser,"//*[(text() = 'Pay with Card' or . = 'Pay with Card')]",report_file_stream)


# This text is the closing line of the report file
report_file_stream.write("</div></div></div></body></html>")