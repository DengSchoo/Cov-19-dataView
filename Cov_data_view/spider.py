import sys
import time
import pymysql
import json
import traceback
import requests
from selenium.webdriver import Chrome,ChromeOptions


def get_tencent_data():
    """
    :return: 返回历史数据和当日详细数据
    """
    url1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    url2 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
        'Referer':' https://news.qq.com/zt2020/page/feiyan.htm'
    }
    r1 = requests.get(url1, headers)
    r2 = requests.get(url2, headers)

    res1 = json.loads(r1.text)
    res2 = json.loads(r2.text)

    data_all1 = json.loads(res1["data"])
    data_all2 = json.loads(res2["data"])

    history = {}
    for i in data_all2["chinaDayList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data_all2["chinaDayAddList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    details = []
    update_time = data_all1["lastUpdateTime"]
    data_country = data_all1["areaTree"]
    data_province = data_country[0]["children"]
    for pro_infos in data_province:
        province = pro_infos["name"]
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details





def get_conn():
    # 建立连接
    conn = pymysql.connect(host="localhost", user="root", password="dsh123", db="cov", charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


#定义更新细节函数
def update_details():
    cursor = None
    conn = None
    try:
        li = get_tencent_data()[1]#1代表最新数据
        conn,cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select update_time from details order by id desc limit 1)'
        #对比当前最大时间戳
        cursor.execute(sql_query,li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新数据")
            for item in li:
                cursor.execute(sql,item)
            conn.commit()
            print(f"{time.asctime()}更新到最新数据")
        else:
            print(f"{time.asctime()}已是最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)


#插入历史数据
def insert_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]#0代表历史数据字典
        print(f"{time.asctime()}开始插入历史数据")
        conn,cursor = get_conn()
        sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k,v in dic.items():
            cursor.execute(sql,[k, v.get("confirm"),v.get("confirm_add"),v.get("suspect"),
                           v.get("suspect_add"),v.get("heal"),v.get("heal_add"),
                           v.get("dead"),v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)


#更新历史数据
def update_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]#0代表历史数据字典
        print(f"{time.asctime()}开始更新历史数据")
        conn,cursor = get_conn()
        sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds=%s"
        for k,v in dic.items():
            if not cursor.execute(sql_query,k):
                cursor.execute(sql,[k, v.get("confirm"),v.get("confirm_add"),v.get("suspect"),
                               v.get("suspect_add"),v.get("heal"),v.get("heal_add"),
                               v.get("dead"),v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)


#爬取百度热搜数据
def get_baidu_hot():
    option = ChromeOptions()
    option.add_argument("--headless")#隐藏游览器
    option.add_argument("--no--sandbox")
    browser =  Chrome(chrome_options = option)#,executable_path="chromedriver-dev.exe"

    url = "https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"
    browser.get(url)
    #print(browser.page_source)
    but = browser.find_element_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/div') # 按照xpath去选择
    ##ptab-0 > div > div.VirusHot_1-5-6_32AY4F.VirusHot_1-5-6_2RnRvg > section > div
    #点击加载更多
    but.click()
    time.sleep(1)
    #爬虫与反爬，模拟人等待1秒
    c = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/a/div/span[2]') # 根据xpath去选取
    context = [i.text for i in c] # 获取selenium内容

    browser.close()
    return context

#更新热搜
def update_hotsearch():
    cursor = None
    conn = None
    try:
        context = get_baidu_hot()
        print(f"{time.asctime()}开始更新百度热搜数据")
        conn,cursor = get_conn()
        cout = 1
        #sql = "insert into hotsearch(id,dt,content) values(%s,%s,%s)" # 第一次需要插入数据
        sql = "update hotsearch set dt = %s, content = %s  where id = %s"
        ts = time.strftime("%Y-%m-%d %X") # 时间戳
        for i in context:
            cursor.execute(sql,(ts,i,cout))
            cout = cout + 1
        conn.commit()
        print(f"{time.asctime()}百度热搜数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

#获取虚假消息
def get_fakes():
    url = "http://www.piyao.org.cn/2020yqpy/" #中国互联网辟谣平台
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")

    browser = Chrome(chrome_options=option)
    browser.get(url)
    button = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div')
    button.click()
    time.sleep(1)

    fakes = browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li/a')

    t = []
    l = []
    for i in range(0, len(fakes)):
        t.append(fakes[i].text)
        l.append(fakes[i].get_attribute('href'))

    # for j in range(0,len(links)):
    #    l.append(links[j].get_attribute('href'))

    fake_data = {}
    for i in range(0, len(fakes)):
        fake_data[t[i]] = l[i]
    browser.close()
    return fake_data

#更新虚假消息
def update_fakes():
    cursor = None
    conn = None
    try:
        context = get_fakes()

        print(f"{time.asctime()}开始更新虚假新闻数据")
        conn, cursor = get_conn()
        cout = 1
        #sql = "insert into fakes(title,href,id) values(%s,%s,%s)" # 第一次需要插入数据
        sql = "update fakes set title = %s, href = %s  where id = %s"
        for key,value in context.items():
            cursor.execute(sql, ( key, value,cout))
            cout = cout + 1
        conn.commit()
        print(f"{time.asctime()}虚假新闻数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

#获取最近资讯
def get_recent_news():
    url = "http://www.chinanews.com/m/34/2020/0127/1364/feiyan.html"
    # 无头浏览器模式
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")

    browser = Chrome(chrome_options=option)
    browser.get(url)
    titles = browser.find_elements_by_xpath('//*[@id="news"]/div/a/div/div')
    links = browser.find_elements_by_xpath('//*[@id="news"]/div/a')
    # browser.close()

    t = []
    l = []
    for i in range(0, len(titles)):
        t.append(titles[i].text)

    for j in range(0, len(links)):
        l.append(links[j].get_attribute('href'))

    rencent_search = {}
    for i in range(0, len(titles)):
        rencent_search[t[i]] = l[i]
    # 字典测试

    browser.close()
    return rencent_search

def update_rencent():
    cursor = None
    conn = None
    try:
        context = get_recent_news()
        print(f"{time.asctime()}开始更新最近资讯数据")
        conn, cursor = get_conn()
        cout = 1
        #sql = "insert into recent_news(title,href,id) values(%s,%s,%s)" # 第一次需要插入数据
        sql = "update recent_news set title = %s, href = %s  where id = %s"
        for key, value in context.items():
            cursor.execute(sql, (key, value, cout))
            cout = cout + 1
        conn.commit()
        print(f"{time.asctime()}最近资讯数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

#获取海外消息
def get_oversea_news():
    url = "https://news.ifeng.com/c/special/7uLj4F83Cqm"
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")

    browser = Chrome(chrome_options=option)
    browser.get(url)

    button = browser.find_element_by_css_selector('#root > div > div.info_box1_3OVvE4C_ > div.morebox_3CILjrCW > a')
    button.click()

    news = browser.find_elements_by_xpath('//*[@id="root"]/div/div[11]/div[1]/div/div/div[1]/a')

    t = []
    l = []
    for i in range(0, len(news)):
        t.append(news[i].text)
        l.append(news[i].get_attribute('href'))
    # for j in range(0,len(links)):
    #    l.append(links[j].get_attribute('href'))
    overseas = {}
    for i in range(0, len(news)):
        overseas[t[i]] = l[i]

    browser.close()
    return overseas

def update_oversea():
    cursor = None
    conn = None
    try:
        context = get_oversea_news()
        print(f"{time.asctime()}开始更新Oversea数据")
        conn, cursor = get_conn()
        cout = 1
        #sql = "insert into oversea(title,href,id) values(%s,%s,%s)"  # 第一次需要插入数据
        sql = "update oversea set title = %s, href = %s  where id = %s"
        for key, value in context.items():
            cursor.execute(sql, (key, value, cout))
            cout = cout + 1
        conn.commit()
        print(f"{time.asctime()}Oversea数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    # l = len(sys.argv)
    # if l == 1:
    #     s = """
    #     请输入参数
    #     参数说明，
    #     up_his 更新历史记录表
    #     up_hot 更新实时热搜
    #     up_det 更新详细表
    #     """
    #     print(s)
    # else:
    #     order = sys.argv[1]
    #     if order == "up_his":
    #         update_history()
    #     elif order == "up_det":
    #         update_details()
    #     elif order == "up_hot":
    #         update_hotsearch()

    update_fakes()      # 更新辟谣
    update_oversea()    # 更新海外
    update_rencent()    # 更新最近
    update_details()    # 更新细节
    update_history()    # 更新历史
    update_hotsearch()  # 更新热搜


