# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, config, os, sys, db, addtask, assertresult, deletetask

class Cronping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(30)
        self.base_url = config.baseurl
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cronping(self):
        #登陆
        #driver = webdriver.Firefox()
        driver = self.driver
        #driver.get(config.baseurl + "/")
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(config.user)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(config.passwd)
        driver.find_element_by_id("sign").click()
        driver.implicitly_wait(30)
        driver.find_element_by_link_text(u"监控配置").click()
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_link_text(u"监控图管理").click()
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_link_text(u"报表管理").click()
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])
        #判断ip管理中是否存在此ip,不存在新增
        if db.readip(config.cronip) == 0:
            driver.find_element_by_link_text("IP管理").click()
            driver.find_element_by_id("ip_name").clear()
            driver.find_element_by_id("ip_name").send_keys(config.cronip)
            driver.find_element_by_css_selector("div.pull-right > button.btn.btn-default").click()
        #新增定时任务
        if addtask.addping('{"dst":"'+config.cronip+'"}',"60","ping",config.cronhost1) == False or addtask.addping('{"dst":"'+config.cronip+'"}',"60","ping",config.cronhost2) == False:
            print "post pingcrontask fail"
            driver.quit()
            os._exit(0)
        else:
            print "post pingcrontask suss"
        time.sleep(5)
        #判断定时任务新增是否成功
        if len(db.readtaskid(config.cronip)) < 2:
            print "add pingcrontask fail"
            driver.quit()
            os._exit(0)
        else:
            print "add pingcrontask suss"
        #新增监控图
        datas = db.readtaskid(config.cronip)
        data = ''
        counts = ''
        for i in range(0, len(datas)):
            if i < len(datas)-1:
                data += "metric="+config.cronip+" metric="+str(datas[i])+"\n"
            if i == len(datas)-1:
                data += "metric="+config.cronip+" metric="+str(datas[i])+""
            if i < len(datas)-1:
                counts +="metric="+config.cronip+" metric="+str(datas[i])+"|"
            if i == len(datas)-1:
                counts +="metric="+config.cronip+" metric="+str(datas[i])+""
        if addtask.addmonitor(config.pingname,config.dashhost,"3600",data,"h","true") ==False:
            print "post pingmonitortask fail"
            driver.quit()
            os._exit(0)
        else:
            print "post pingmonitortask suss"
        time.sleep(5)
        #判断监控图任务是否新增成功
        if db.readmonitor(counts) == config.pingname:
            print "add pingmonitortask suss"
        else:
            print "add pingmonitortask fail"
            driver.quit()
            os._exit(0)
        time.sleep(300)
        #查看报表展现
        driver.switch_to_window(driver.window_handles[3])
        driver.find_element_by_xpath("//div[@id='container']/div/div/ul/li/div/button").click()
        driver.find_element_by_css_selector("li.screen > a > small").click()
        driver.find_element_by_xpath("//div[@id='container']/div/div/ul/li[2]/div/button").click()
        driver.find_element_by_css_selector("div.btn-group.open > ul.dropdown-menu > li.screen > a > small").click()
        assertresult.graphget()
        time.sleep(2)
        #删除监控图管理
        driver.switch_to_window(driver.window_handles[2])
        time.sleep(2)
        driver.find_element_by_id("g_name").clear()
        driver.find_element_by_id("g_name").send_keys(config.pingname)
        driver.find_element_by_css_selector("button.btn.btn-info").click()
        time.sleep(2)
        driver.find_element_by_name("btSelectAll").click()
        time.sleep(2)
        driver.find_element_by_css_selector("button.btn.btn-warning").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"确认删除1个图表配置?")
        #删除定时任务
        deletetask.crondel(config.cronip)
        time.sleep(2)
        #退出登录
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(2)
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
