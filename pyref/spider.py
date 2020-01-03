from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path="/Users/kylinchan/phantomjs/bin/phantomjs")

driver.get("http://xueshu.baidu.com/")
data = driver.title
# driver.save_screenshot('qq.png')
# print(data)


driver.find_element_by_id("kw").send_keys(u"我")

driver.find_element_by_id("su").click()
# x=driver.find_elements_by_xpath('//h3[@class="t c_font"]/a')

article_links = []
for i in driver.find_elements_by_xpath('//h3[@class="t c_font"]/a'):
    article_links.append(i.get_attribute('href'))
print(article_links)

driver.get(article_links[0])

x=driver.find_elements_by_xpath('//a[@class="paper_q"]')
print(x)
print(x[0].get_attribute("href"))
if(x[0].get_attribute("href") is not None and "javascript:;" in x[0].get_attribute("href")):
    driver.execute_script('arguments[0].click();', x[0])
    time.sleep(2)
    print('1')
    driver.save_screenshot("qq.png")

x=driver.find_elements_by_xpath('//div[@class="sc_quote_citi"]/a')
print(x)
print(x[0].get_attribute("href"))

driver.get(x[0].get_attribute("href"))
driver.save_screenshot("qq.png")
x=driver.find_elements_by_xpath('//pre[@style="word-wrap: break-word; white-space: pre-wrap;"]')
print(x[0].text)

driver.quit()