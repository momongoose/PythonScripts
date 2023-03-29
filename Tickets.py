import time
import re
import smtplib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "http://url")
    test = driver.find_element(by=By.CSS_SELECTOR, value='input.form-control')
    test.send_keys("user")
    test1 = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    test1.send_keys("password")
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/form/div/div[1]/div[5]/button")
    driver.execute_script("arguments[0].click();", element)
    driver.get(
        "http://url")
    title = ""
    OldTicketCount = 0

    sender_email = "sender@mail.com"
    receiver_email1 = "receiver1@mail.com"
    receiver_email2 = "receiver2@mail.com"
    #/html/body/div[1]/div/div/main/div[2]/div[2]/div/form/div/div[2]/table/tbody/tr[2]/td[3]/a
    while True:
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login("mail@mail.com", "password")
        time.sleep(3)
        driver.refresh()
        # driver.get(
        #    "http://10.90.1.7/front/ticket.php?criteria%5B0%5D%5Bfield%5D=12&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=1&reset=reset")
        # time.sleep(5)
        try:
            text = driver.find_element(by=By.XPATH, value=
                "/html/body/div[1]/div/div/main/div/div[2]/div/form/div/div[3]/div/p[1]")
        except:
            OldTicketCount = 0
            continue
        TicketCount = int(re.findall(r'\d+', text.text)[-1])
        print(TicketCount)
        if check_exists_by_xpath(
                "/html/body/div[1]/div/div/main/div/div[2]/div/form/div/div[2]/table/tbody/tr[1]/td[3]/a") == True and TicketCount > OldTicketCount:
            # print("New ticket")
            OldTicketCount = TicketCount
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[2]/div/form/div/div[2]/table/tbody/tr[1]/td[3]/a").click()
            time.sleep(5)
            titleCheck = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/span/div/div[2]/div[1]")
            # print(titleCheck.text)
            if title != titleCheck:
                textdoc = driver.find_element(by=By.CSS_SELECTOR, value='div.card-body')
                # print(textdoc.text)
                title = titleCheck
                Betreff = titleCheck.text.encode('ascii', 'ignore').decode('ascii')
                Text = textdoc.text.encode('ascii', 'ignore').decode('ascii')
                print(Betreff)
                print(Text)
                message = 'Subject: {}\n\n{}'.format(Betreff, Text)
                s.sendmail(sender_email, receiver_email1, message)
                s.sendmail(sender_email, receiver_email2, message)
                driver.get(
                    "http://url")
            else:
                driver.get(
                    "http://url")
                continue
        else:
            OldTicketCount = TicketCount