# -*- coding: utf-8 -*-
"""
365 study
"""
from splinter.browser import Browser
from time import sleep
import traceback
import time, sys

class huoche(object):
	driver_name = ''
	executable_path = ''
	#用户名，密码
	username = u"xxx"
	passwd = u"xxx"
	

	c"
	
	def __init__(self):
		self.driver_name = 'chrome'
		self.executable_path = 'D:/chromedriver'

	def login(self):
		self.driver.visit(self.login_url)
		self.driver.fill("loginUserDTO.user_name", self.username)

			else:
				break

	def start(self):
		self.driver = Browser(driver_name=self.driver_name,executable_path=self.executable_path)
		self.driver.driver.set_window_size(1400, 1000)
		self.login()
		# sleep(1)
	
			self.driver.reload()

			count = 0
			if self.order != 0:
				while self.driver.url == self.ticket_url:
					self.driver.find_by_text(u"查询").click()
					count += 1
					print(u"循环点击查询... 第 %s 次" % count)
					# sleep(1)
					try:
						self.driver.find_by_text(u"预订")[self.order - 1].click()
					except Exception as e:
						print(e)
						print(u"还没开始预订")
						continue
			else:
				while self.driver.url == self.ticket_url:
					self.driver.find_by_text(u"查询").click()
					count += 1
					print(u"循环点击查询... 第 %s 次" % count)
					# sleep(0.8)
					try:
						for i in self.driver.find_by_text(u"预订"):
							i.click()
							sleep(1)
					except Exception as e:
						print(e)
						print(u"还没开始预订 %s" % count)
						continue
			print(u"开始预订...")
			# sleep(3)
			# self.driver.reload()
			sleep(1)
			print(u'开始选择用户...')
			for user in self.users:
				self.driver.find_by_text(user).last.click()


		except Exception as e:
			print(e)

if __name__ == '__main__':
	huoche = huoche()
	huoche.start()