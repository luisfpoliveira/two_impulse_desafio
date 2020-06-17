import time

from datetime import datetime


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def click_on_element_by_xpath (browser, xpath, report_file_stream, timeout = 30):
    """
    Clicks on one element defined by xpath of the web-page displayed on a given browser instance

    :param browser: browser instance created by the selenium webdriver
    :param xpath: xpath of the element to be clicked
    :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
    :param timeout: maximum time during which the script will wait for the to be loaded
            after the time out the action will fail
    :return: returns the element.
    """
    try:
        element = WebDriverWait (browser,timeout).until(expected_conditions.presence_of_element_located((By.XPATH,xpath)))
        print (element)
        element.click()
    except:
        report_file_stream.write('<font color=#800080>%s</font>: Clicking on the element defined defined by the following XPath "%s": <font color=#FF0000>FAILED</font><br />' % (datetime.now().strftime("%H:%M:%S.%f") ,xpath))
        date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
        filename = "failure_screen_shot_%s.png" % date_time_string
        browser.get_screenshot_as_file(filename)
        report_file_stream.write("Screen shot saved on file: %s<br />" % filename)
        exit(1)
    else:
        report_file_stream.write('<font color=#800080>%s</font>: Clicking on the element defined defined by the following XPath "%s": <font color=#00FF00>PASSED</font><br />' % (datetime.now().strftime("%H:%M:%S.%f") ,xpath))
        return element

def sequence_of_clicks (browser, input_file_name, report_file_stream):
    """
    performs a sequence of clicks on a set of elements defined by a list of xpaths read from a file

    :param browser: browser instance where the actions will be performed
    :param input_file_name: list of the xpaths to be clicked
    :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
    """
    clicks_file = open (input_file_name, mode = 'r')
    for xpath in clicks_file:
        time.sleep (5)
        click_on_element_by_xpath(browser, xpath, report_file_stream)

def send_keys_to_element_by_xpath (browser, xpath, keys, report_file_stream, timeout = 30):
    """
    Fills text in one form element defined by xpath in the web-page displayed on a given browser instance

    :param browser: browser instance created by the selenium webdriver
    :param xpath: xpath of the element to be filled in
    :param keys: text to be entered in the form element
    :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
    :param timeout: maximum time during which the script will wait for the to be loaded
            after the time out the action will fail
    :return: returns the element

    """

    try:
        element = WebDriverWait(browser, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        # print (element)
        element.send_keys (keys)
    except:
        report_file_stream.write("<font color=#800080>%s</font>: Sending keys to the element defined defined by the following XPath '%s': <font color=#FF0000>FAILED</font><br />" % (datetime.now().strftime("%H:%M:%S.%f") ,xpath))
        date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
        filename = "failure_screen_shot_%s.png" % date_time_string
        browser.get_screenshot_as_file(filename)
        report_file_stream.write("Screen shot saved on file: %s<br />" % filename)
        exit(1)
    else:
        report_file_stream.write("<font color=#800080>%s</font>: Sending keys to the element defined defined by the following XPath '%s': <font color=#00FF00>PASSED</font><br />" % (datetime.now().strftime("%H:%M:%S.%f") ,xpath))
        return element

def fill_in_text_form (browser, xpath_list, input_data, list_of_fields, report_file_stream):
    """
    Fills text in a list of form element defined by xpath

    :param browser: browser instance where the actions will be performed
    :param xpath_list: list of the xpaths of the web elements to be filled in
    :param input_data: list of the strings to be entered in each element
    :param list_of_fields: list of fields to be filled in
    :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
    """

    for individual_field in list_of_fields:
        send_keys_to_element_by_xpath(browser, xpath_list['xpath'][individual_field],keys=input_data['purchaser_information'][individual_field], report_file_stream= report_file_stream)

def get_text_by_xpath (browser, xpath):
    """
    Reads the text contained in a given web element defined by xpath

    :param browser: browser instance where the actions will be performed
    :param xpath:  xpath of the element
    """
    return(browser.find_element_by_xpath(xpath).text)

def get_text_to_dictionary_from_a_page (browser, xpath_list):
    """
    Reads the text from a series of web elements defined by xpath and stores it in a dictionary

    :param browser: browser instance where the actions will be performed
    :param xpath_list: list of the xpath of the elements to be read
    :return: dictionary with the text read
    """

    data_dictionary = {}

    for individual_data in xpath_list['xpath']:
        colected_text = get_text_by_xpath(browser, xpath_list['xpath'][individual_data])
        data_dictionary.update({individual_data: colected_text})

    return data_dictionary
