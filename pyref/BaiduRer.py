import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RunError(Exception):
    def __init__(self):
        Exception.__init__(self)
    def __str__(self):
        return repr('No Phamtonjs in PATH')

class BaiduRer(object):
    def __init__(self, phamtonjs_path=""):
        try:
            if(phamtonjs_path):
                self.driver = webdriver.PhantomJS(executable_path=phamtonjs_path)
            else:
                self.driver = webdriver.PhantomJS()
        except:
            raise RunError()
        # default open url of baidu researcher
        self.driver.get("http://xueshu.baidu.com/")

    def single_article_bib(self,title):
        self.driver.find_element_by_id("kw").send_keys(title)
        self.driver.find_element_by_id("su").click()

        article_links = []
        for i in self.driver.find_elements_by_xpath('//h3[@class="t c_font"]/a'):
            article_links.append(i.get_attribute('href'))
        self.driver.get(article_links[0]) # default get the first one 

        button=self.driver.find_elements_by_xpath('//a[@class="paper_q"]')
        if(button[0].get_attribute("href") is not None and "javascript:;" in button[0].get_attribute("href")):
            self.driver.execute_script('arguments[0].click();', button[0])
            
        # get bib ref
        bib_ref=self.driver.find_elements_by_xpath('//div[@class="sc_quote_citi"]/a')
        self.driver.get(bib_ref[0].get_attribute("href"))
        bib_text=self.driver.find_elements_by_xpath('//pre[@style="word-wrap: break-word; white-space: pre-wrap;"]')
        print(bib_text[0].text)

if __name__ == '__main__':
    getter = BaiduRer("/Users/kylinchan/phantomjs/bin/phantomjs")
    getter.single_article_bib("你是")
