from pymysql import connect


def create_sync_con():
    con = connect(host='localhost', user='root', db='reshalaa_bot',
                  password='Andrei123009')
    cur = con.cursor()
    return con, cur


def sync_get_context():
    con, cur = create_sync_con()
    cur.execute('select username from user where tel_id = {0}'.format('420404892'))
    context = cur.fetchone()
    con.close()
    print(context)

    if context is None:
        return None

    return context[0]


def send_price_c(ord_id, auth):
    con, cur = create_sync_con()

    cur.execute('select * from reshalaa_bot.db_manager_ord_auth_price where ord_id = %s and tel_id = %s',
                (ord_id, auth))
    info = cur.fetchone()
    info = info
    print(info)

    new_price = 0
    price = info[2]

    if int(price) <= 50:
        new_price = int(price) + 50
    elif int(price) > 50 and int(price) < 99:
        new_price = int(price) + 70
    elif int(price) > 99 and int(price) <= 500:
        new_price = int(price) + 100
    elif int(price) > 500:
        new_price = int(price) + (int(price) * (20 / 100))
    new_price = round(int(new_price))

    cur.execute('select username from reshalaa_bot.db_manager_order where ord_id = %s', (ord_id))
    username = cur.fetchone()

    cur.execute('insert into reshalaa_bot.db_manager_cust_pri values (%s, %s, %s, %s, %s, %s, %s)',
                (info[0], info[1], info[2], info[3], info[4], new_price, username))
    con.commit()

    cur.execute('select * from reshalaa_bot.db_manager_order where ord_id = %s', ord_id)
    order = cur.fetchone()
    order = order

    cur.execute(
        'insert into reshalaa_bot.db_manager_priceo values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (order[0], order[1], order[2], order[3], order[4], order[5], order[6],
         order[7], order[8], order[9], order[10], order[11], order[12], '0'))
    con.commit()

    cur.execute('delete from reshalaa_bot.db_manager_ord_auth_price where ord_id = %s', ord_id)
    con.commit()

    cur.execute('delete from reshalaa_bot.db_manager_order where ord_id = %s', ord_id)
    con.commit()

    cur.execute('select tel_id from reshalaa_bot.user where username = %s', (username))
    tel_id = cur.fetchone()

    con.close()

    return tel_id


def get_new_cost(tel_id, ord_id):
    con, cur = create_sync_con()

    cur.execute('SELECT customer_pr FROM reshalaa_bot.db_manager_cust_pri where ord_id = %s', ord_id)
    orders = cur.fetchone()

    cur.execute('SELECT count_b FROM reshalaa_bot.bonuses where tel_id = %s', tel_id)
    bonuses = cur.fetchone()

    con.close()
    return orders[0], bonuses[0]


def check_and_send_order(ord_id):
    con, cur = create_sync_con()

    cur.execute('SELECT payment FROM reshalaa_bot.db_manager_waito where ord_id = %s', ord_id)
    payment = cur.fetchone()
    payment = int(payment[0])

    cur.execute('SELECT customer_pr FROM reshalaa_bot.db_manager_customer_price where ord_id = %s', ord_id)
    customer_price = cur.fetchone()
    customer_price = int(customer_price[0])

    cur.execute('SELECT customer_username FROM reshalaa_bot.db_manager_customer_price where ord_id = %s', ord_id)
    username = cur.fetchone()

    cur.execute('SELECT tel_id FROM reshalaa_bot.user where username = %s', username)
    tel_id = cur.fetchone()

    cur.execute('SELECT author_links FROM reshalaa_bot.db_manager_waito where ord_id = %s', ord_id)
    files = cur.fetchone()

    cur.execute('SELECT author FROM reshalaa_bot.db_manager_waito where ord_id = %s', ord_id)
    author = cur.fetchone()

    cur.execute('SELECT * FROM reshalaa_bot.authors where username = %s', author[0])
    author_info = cur.fetchone()

    cur.execute('SELECT price FROM reshalaa_bot.db_manager_customer_price where ord_id = %s', ord_id)
    cost = cur.fetchone()

    cur.execute(
        'insert into reshalaa_bot.db_manager_dpo values (%s, %s, %s, %s, %s)',
        (ord_id, author_info[9], cost, author_info[6], author_info[2]))
    con.commit()

    cur.execute('delete from reshalaa_bot.db_manager_waito where ord_id = %s', ord_id)
    con.commit()

    con.close()

    if payment >= customer_price:
        return 1, tel_id[0], files[0]
    else:
        return customer_price - payment, tel_id[0], files[0]

def payok_db(ord_id):
    con, cur = create_sync_con()

    cur.execute('delete from reshalaa_bot.db_manager_dpo where ord_id = %s', ord_id)
    con.commit()

    con.close()

def add_dpo(ord_id):
    con, cur = create_sync_con()

    cur.execute('SELECT author FROM reshalaa_bot.db_manager_waito where ord_id = %s', ord_id)
    author = cur.fetchone()

    cur.execute('SELECT * FROM reshalaa_bot.authors where username = %s', author[0])
    author_info = cur.fetchone()

    cur.execute('SELECT price FROM reshalaa_bot.db_manager_customer_price where ord_id = %s', ord_id)
    cost = cur.fetchone()

    cur.execute(
        'insert into reshalaa_bot.db_manager_dpo values (%s, %s, %s, %s, %s)',
        (ord_id, author_info[9], cost, author_info[6], author_info[2]))
    con.commit()

    con.close()
