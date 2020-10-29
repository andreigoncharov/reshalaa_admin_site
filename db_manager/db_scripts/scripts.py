from pymysql import connect


def create_sync_con():
    con = connect(host='localhost', user='root', db='reshalaa_bot',
                  password='Andrei123009')
    cur = con.cursor()
    return con, cur

def sync_get_context():
        con, cur = create_sync_con()
        cur.execute('select context from user where tel_id = {0}'.format('420404892'))
        context = cur.fetchone()
        con.close()

        if context is None:
            return None

        return context[0]