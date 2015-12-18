#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ip页面test

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, config

class Ip(unittest.TestCase):
    def test_ip(self):
        #登陆
        driver = webdriver.Firefox()
        driver.get(config.baseurl + "/")
        driver.implicitly_wait(30)
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_link_text(u"用户登录/退出").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(config.user)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(config.passwd)
        driver.find_element_by_id("sign").click()
        driver.implicitly_wait(30)
        driver.find_element_by_link_text(u"首页").click()
        #监控portal页面
        driver.find_element_by_link_text(u"监控配置").click()
        driver.implicitly_wait(30)
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_link_text("IP管理").click()
        #新建IP,自动获取对应地区isp信息
        driver.find_element_by_id("ip_name").clear()
        driver.find_element_by_id("ip_name").send_keys(config.ip)
        driver.find_element_by_css_selector("div.pull-right > button.btn.btn-default").click()
        #精确搜索ip
        driver.find_element_by_link_text("Ip").click()
        time.sleep(2)
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(config.ip)
        driver.find_element_by_css_selector("div.form-inline > button.btn.btn-default").click()
        driver.implicitly_wait(30)
        #判断搜索结果
        try:
            value = driver.find_element_by_xpath("html/body/div[1]/table").text
            value.index(config.ip)
            value.index(u"中国")
            print "insert and search suss"
        except Exception, e:
            print e
            print "insert and search fail"
        #修改ip信息
        driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[9]/a/span").click()
        driver.find_element_by_id("isp").clear()
        driver.find_element_by_id("isp").send_keys(u"华数")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        time.sleep(2)
        driver.find_element_by_link_text("Ip").click()
        time.sleep(2)
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(config.ip)
        driver.find_element_by_css_selector("div.form-inline > button.btn.btn-default").click()
        driver.implicitly_wait(30)
        try:
            value = driver.find_element_by_xpath("html/body/div[1]/table").text
            value.index(config.ip)
            value.index(u"华数")
            print "alert suss"
        except Exception, e:
            print e
            print "alert fail"
        #删除ip
        driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr[1]/td[9]/a[2]/span").click()
        driver.find_element_by_link_text(u"确定").click()
        time.sleep(2)
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(config.ip)
        driver.find_element_by_css_selector("div.form-inline > button.btn.btn-default").click()
        driver.implicitly_wait(30)
        try:
            value = driver.find_element_by_xpath("html/body/div[1]/table").text
            value.index("no records")
            print "delete suss"
        except Exception, e:
            print e
            print "delete fail"
        #退出登录
        driver.switch_to_window(driver.window_handles[0])
        driver.implicitly_wait(30)
        driver.find_element_by_link_text(u"用户登录/退出").click()
        driver.find_element_by_link_text(u"退出").click()
        driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

if __name__ == "__main__":
    unittest.main()
