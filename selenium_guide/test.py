#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print driver.current_url
