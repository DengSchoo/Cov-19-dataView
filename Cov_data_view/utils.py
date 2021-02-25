import time
import pymysql

def get_time(): # 获取前端时间
    time_str = time.strftime("%Y{}%m{}%d{} %X") #格式化
    return time_str.format("年","月","日") # 填充



def get_conn(): # 建立连接
    # 建立连接
    conn = pymysql.connect(host="localhost", user="root", password="dsh123", db="cov", charset="utf8")
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor): # 关闭数据库 释放资源
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args): # 查询sql语句 *args是多个参数
    """

    :param sql:
    :param args:
    :return:
    """
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res

def test(): # 查看所有细节
    sql = "select * from details"
    res = query(sql)
    return res[0]

def get_c1_data():
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal),sum(dead) from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) "
    res = query(sql)
    return res[0] #返回第一条数据

def get_c1_time(): # 获取前端时间
    sql = "select max(update_time) from details"
    res = query(sql)
    update_time = res[0][0].strftime("%Y-%m-%d %H:%M:%S")
    return update_time # 返回最晚更新时间

def get_c2_data(): #获取最新的数据
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res

def get_l1_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res

def get_l2_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_r1_data(): #获取非湖北省内的top5的城市疫情数据
    # 非湖北和直辖市 并把直辖市内的数据作累加
    sql = 'select city,confirm from ' \
          '(select city,confirm from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆","香港","澳门","台湾") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆","香港","澳门","台湾") group by province) as a ' \
          'order by confirm desc limit 7'

    res = query(sql)
    return res

def get_r2_data():
    sql = "select content from hotsearch order by id desc limit 20"
    res = query(sql)
    return res

def get_recent():
    sql = "select title,href from recent_news limit 20"
    res = query(sql)
    return res

def get_fakes():
    sql = "select title,href from fakes limit 20"
    res = query(sql)
    return res

def get_oversea():
    sql = "select title,href from oversea limit 20"
    res = query(sql)
    return res



if __name__ == "__main__":


    print(get_c1_time())
    print(type(get_c1_time()[0]))