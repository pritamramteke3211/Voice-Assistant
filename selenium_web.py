from selenium import webdriver



class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

    def get_info(self,query=None):
        self.query=query
        self.driver.get(url='https://www.wikipedia.org')
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        # search.click()
        search.send_keys(query)
        find = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        find.click()

    def get_music(self,query):
        self.query = query
        self.driver.get(url='https://www.youtube.com')
        search = self.driver.find_element_by_xpath('//*[@id="search"]')
        search.send_keys(query)
        find = self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        find.click()
        play = self.driver.find_element_by_xpath('//*[@id="img"]')
        play.click()

    # def show_image(self,query):
    #     self.query = query
    #     self.driver.get(url='https://www.google.com')
    #     search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    #     search.send_keys(query)
    #     find = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li[1]')
    #     find.click()



# query = input("Enter info : ")
# assist = info()
# assist.get_info(query)
# assist.get_music(query)
# # assist.show_image(query)