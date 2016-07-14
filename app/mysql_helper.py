import pymysql


def get_main_connection():
    """
    连接主数据库
    :return:
    """
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='test',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn


def close_connection(conn):
    """
    关闭数据库连接
    :param conn:
    :return:
    """
    conn.close()


def select_username_password(username):
    """
    根据factory_id修改厂家信息
    :param username:
    :return:
    """
    conn = get_main_connection()
    try:
        cursor = conn.cursor()
        sql = "select password from ebf_flask where username=%s"
        cursor.execute(sql, username)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(e)
    finally:
        close_connection(conn)
