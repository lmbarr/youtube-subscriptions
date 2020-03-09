from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import opml
from secrets import username, password


class YoutubeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.youtube.com/')

        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer/a/paper-button')
        btn.click()

        email_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        email_in.send_keys(username)

        next_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
        next_btn.click()

        sleep(2)

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw_in.send_keys(password)

        next_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
        next_btn.click()

        sleep(1)

    def start_to_subscribe(self):
        outline = opml.parse('subscription_manager')

        for x in outline[0]:
            channel = x.title
            # clean search box input
            search_for_input = self.driver.find_element_by_xpath('//*[@id="search"]')
            search_for_input.send_keys(Keys.CONTROL + "a")
            search_for_input.send_keys(Keys.DELETE)

            search_for_input.send_keys(channel)

            search_btn = self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            search_btn.click()

            sleep(1)

            button_msg = self.driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string').text

            print(button_msg)

            if button_msg == 'SUBSCRIBE':

                subscribe_btn = self.driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button')
                subscribe_btn.click()
                print(f"Processed {channel}")
                sleep(1)


bot = YoutubeBot()
bot.login()
bot.start_to_subscribe()
