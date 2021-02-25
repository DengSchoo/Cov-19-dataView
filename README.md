# 成果展示

## 界面UI1

中国地区的疫情数据可视化。

![image-20210225153553303](https://gitee.com/DengSchoo374/img/raw/master/images/image-20210225153553303.png) 

## 界面UI2

疫情资讯快速预览：点击要查看的标题即可新开空白页面跳转到对应网页。

![image-20210225153606032](https://gitee.com/DengSchoo374/img/raw/master/images/image-20210225153606032.png)

## 界面UI3

这里在导入指定格式的csv文件后，会自动产生动态排名情况直到导入的数据文件结束。

![img](https://gitee.com/DengSchoo374/img/raw/master/images/image-20210225153623191.png) ![image-20210225153629209](https://gitee.com/DengSchoo374/img/raw/master/images/image-20210225153629209.png)

完整动态结果参照演示视频



# 作品概览

## 1.设计内容

基于Python3.7版本的web网页的数据可视化平台设计，将疫情数据制作成图表内容，抓取疫情相关资讯，并提供对外的可视化功能。

## **2.** 设计目的

通过疫情数据可视化的平台设计体现计算机科学工作的社会责任感，效仿大厂为群众设计的疫情数据网站，让人们动动手就能知晓疫情，从而更科学的做好防护工作。

## **3.** 技术栈概览

前端：JQuery、Bootstrap、echarts、d3、html/css/js

后端：Flask框架、Python爬虫技术相关(selenium等)、MySQL数据持久化、json

前后端交互：ajax实现前后端交互

## **4.** 实现思路

借助Flask轻量级Python网站框架，搭建可视化平台，在后端使用selenium获取数据并持久化到MySQL数据库中，前端使用ajax请求与后端flask交互数据，局部动态刷新的实现实时可视化，网站的可视化图表采用echarts等开源框架。

## **2.** 数据来源

### 5.1腾讯疫情历史和详细数据接口

 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
 "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"

### 5.2 百度热搜数据

"https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"

### 5.3 疫情辟谣

"http://www.piyao.org.cn/2020yqpy/"

### 5.4 最新资讯

"http://www.chinanews.com/m/34/2020/0127/1364/feiyan.html"

### 5.5 海外资讯

"https://news.ifeng.com/c/special/7uLj4F83Cqm"

