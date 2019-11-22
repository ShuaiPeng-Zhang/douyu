#coding=utf-8
from selenium import webdriver
import json
import time

class Douyu(object):
    # 1.发送首页的请求
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.douyu.com/directory/all") #请求首页

    #获取没页面内容
    def get_content(self):
        time.sleep(3) #每次发送完请求等待三秒，等待页面加载完成
        li_list = self.driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
        contents = []
        for i in li_list: #遍历房间列表
            item = {}
            item["img"] = i.find_element_by_xpath("./div/a[1]/div[1]/div[1]/img").get_attribute("src") #获取房间图片
            item["title"] = i.find_element_by_xpath("./div/a[1]/div[2]/div[1]/h3").get_attribute("title") #获取房间名字
            item["category"] = i.find_element_by_xpath("./div/a[1]/div[2]/div[1]/span").text #获取房间分类
            item["name"] = i.find_element_by_xpath("./div/a[1]/div[2]/div[2]/h2").text #获取主播名字
            item["watch_num"] = i.find_element_by_xpath("./div/a[1]/div[2]/div[2]/span").text #获取观看人数
            print(item)
            print('*'*30)
            contents.append(item)
        return contents
    #保存本地
    def save_content(self,contents):
        f = open("douyu.txt","a",encoding='utf-8')
        for content in contents:
            # json.dump(content,f,ensure_ascii=False,indent=2)
            f.write(content)
            f.write("\n")
        f.close()

    def run(self):
        #1.发送首页的请求
        #2.获取第一页的信息
        contents = self.get_content()
            #保存内容
        self.save_content(contents)
        #3.循环  点击下一页按钮，知道下一页对应的class名字不再是"shark-pager-next"
        # while self.driver.find_element_by_class_name("dy-Pagination-item-custom"): #判断有没有下一页
        #     #点击下一页的按钮
        #     self.driver.find_element_by_class_name("dy-Pagination-item-custom").click() #
        #     # 4.继续获取下一页的内容
        #     contents = self.get_content()
        #     #4.1.保存内容
        #     self.save_content(contents)

    def __del__(self):
        self.driver.quit()

if __name__ == "__main__":
    douyu = Douyu()
    douyu.run()