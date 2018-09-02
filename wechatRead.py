#coding=utf8

import  os, time
print("执行微信读书自动翻页功能中！")
page = int(input("请输入书籍页数:"))
cur = int(input("请输入当前页数:"))
command = "adb shell input swipe 300 300 50 50"
while(page):
	if cur >= page :
		print("本书已经读完，正在退出...")
		os.system('adb shell input keyevent 4')
		os._exit(0)
	os.system(command)
	cur += 1
	print("当前页数:", cur)
	print("看书30s中。。。")
	time.sleep(30)