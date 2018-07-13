""" 
selenium:自动化测试工具，支持多种浏览器，解决javascript渲染问题

安装：pip3 install selenium
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

browser=webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input=browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(ec.presence_of_element_located((By.ID,'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookie)
    # print(browser.page_source)

finally:
    browser.close()

# 声明浏览器对象
from selenium import webdriver
browser=webdriver.Chrome()
browser=webdriver.Firefox()
browser=webdriver.Edge()
browser=webdriver.PhantomJS()
browser=webdriver.Safari()

# 访问页面
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.page_source
browser.close()


##  查找元素
# 单个元素
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get("https://www.taobao.com")

# 以下输出结果完全相同
# 第一种方式
input_first=browser.find_element_by_id('q')
input_sencond=browser.find_element_by_css_selector('#q')
input_third=browser.find_element_by_xpath('//*[@id="q"]')

# 第二种方式
input_four=browser.find_element(By.CSS_SELECTOR,'#q')
input_five=browser.find_element(By.ID,'q')
print(input_first,input_sencond,input_third)

# 查找多个元素
input_six=browser.find_elements_by_css_selector('.J_Cat')

input_senven=browser.find_elements(By.CSS_SELECTOR,'.J_Cat')


# 元素的行为操作

from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
input=browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button=browser.find_element_by_css_selector('.btn-search')
button.click()


# 交互动作(将动作附加到动作链中串行执行)
from selenium import webdriver
from selenium.webdriver import ActionChains

browser =webdriver.Chrome()
url="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to_frame('iframeResult')
source=browser.find_element_by_id('draggable')
target=browser.find_element_by_id('droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()


# 执行javascript
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("to Bottom!")')


# 获取元素属性值
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
logo = browser.find_element_by_css_selector('#zu-top-link-logo')
print(logo.get_attribute('class')) # zu-top-link-logo
# 获取文本值
print(logo.text)  # 知乎

# 获取id、位置、标签名、大小
print(logo.id)          # 0.7782359378290884-1
print(logo.location)    # {'x': 32, 'y': 0}
print(logo.tag_name)    # a
print(logo.size)        # {'height': 45, 'width': 61}


# Frame
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser =webdriver.Chrome()
url="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to_frame('iframeResult')
source=browser.find_element_by_id('draggable')
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('no logo')
browser.switch_to.parent_frame()
logo=browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)


## 等待
# 隐式等待 在找不到元素时，继续等待，超出规定时间后抛出找不到元素异常
from selenium import webdriver
browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.zhihu.com/explore")
input=browser.find_element_by_class_name('zu-top-add-question')
print(input)


# 显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
wait=WebDriverWait(browser,10)
input=wait.until(ec.presence_of_element_located((By.ID,'q')))
button=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)

# 前进后退
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.baidu.com/")
browser.get("https://www.taobao.com/")
browser.get("https://www.python.org/")
browser.back()
time.sleep(1)
browser.forward()

# Cookies
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'nc'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

# 选项卡管理
import time 
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.python.org')


# 异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser=webdriver.Chrome()
try:
    browser.get('http://www.baidu.com')
except TimeoutException:
    print('time out')
try:
    browser.find_element_by_id('heee')
except NoSuchElementException:
    print('no element')
finally:
    browser.close()
