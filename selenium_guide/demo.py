#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import By
#引入鼠标事件模块
from selenium.webdriver.common.action_chains import ActionChains
#引入键盘事件模块
from selenium.webdriver.common.keys import Keys
#引入显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#通过id/name/class定位
driver.find_element_by_id("")
driver.find_element_by_name("")
driver.find_element_by_class_name("")

#link定位,定位文本链接
driver.find_element_by_link_text(u"新闻")
#超长文本
driver.find_element_by_partial_link_text(u"这是一个超长")

#xpath定位
#绝对路径
driver.find_element_by_xpath("/html/body/div/div[2]/div/input")
#利用元素属性定位,//表示当前某个标签下
driver.find_element_by_xpath("//input[@id='kw']")
#层级定位
driver.find_element_by_xpath("//span[@id='kw']/input")
#多个属性定位一个
driver.find_element_by_xpath("//input[@id='kw' and @class='su']/span/input")

#css定位
#通过class属性
driver.find_element_by_css_selector(".s_ipt")
#通过id属性
driver.find_element_by_css_selector("#kw")
#通过标签名
driver.find_element_by_css_selector("input")
#通过父子关系
driver.find_element_by_css_selector("span>input")
#通过属性
driver.find_element_by_css_selector("[name='kw']")
#组合定位
driver.find_element_by_css_selector("form.fm>span>input#kw")

#浏览器前进后退刷新
driver.back()
driver.forward()
driver.refresh()

#鼠标事件
#鼠标右击
right_click = driver.find_element_by_id("")
#perform()执行ActionChains中存储行为,提交动作
ActionChains(driver).context_click(right_click).perform()
#鼠标悬停
above = driver.find_element_by_id("")
ActionChains(driver).move_to_element(above).perform()
#鼠标双击
double_click = driver.find_element_by_link_text("")
ActionChains(driver).double_click(double_click).perform()
#鼠标拖放,source拖动的源元素,target拖动的目标元素
source = driver.find_element_by_link_text("")
target = driver.find_element_by_link_text("")
ActionChains(driver).drag_and_drop(source,target).perform()

#键盘事件
#输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
#删除多输入的m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#输入空格键+教程
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
#全选
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

#获得输入框尺寸
driver.find_element_by_id("kw").size
#获得元素的文本
driver.find_element_by_id("cp").text
#获取元素的属性,可以是id/name/type
driver.find_element_by_id("kw").get_attribute('type')
#返回元素是否可见,返回结果为true或false
driver.find_element_by_id("kw").is_displayed()

#获取当前页面title
driver.title
#获取当前页面url
driver.current_url

#显式等待
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_all_elements_located())

#隐式等待
driver.implicitly_wait(10)

#定位一组元素,和单个元素一样,也有8个,用于复选框
driver.find_elements_by_id()
#把页面上最后一个勾去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
#pop()或pop(-1) 默认获取一组元素中的最后一个;pop(0) 获取一组元素中的第一个

#多表单切换,frame/iframe表单嵌套页面,切换到iframe(id = if),默认取表单的id或者name定位,如果没有,则通过别的先取出,再赋值给它
driver.switch_to.frame("if")
#跳出当前一级的表单
driver.switch_to.parent_content()
#调回最外层的页面
driver.switch_to.default_content()

#多窗口切换
driver.switch_to.window()

#警告框处理



