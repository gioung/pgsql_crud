import psycopg2
import config

def test_insert():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("insert into pet values('똘똘이', '기웅이', '불가사리', 'm', '2015-09-09', null)")

    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_select():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("select * from pet")
        rs = cursor.fetchall()

        for record in rs:
            print(record, type(record))
    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_delete():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("delete from pet where name='뚱이'")

    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_update():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("update pet set name='뚱이' where name='Buffy'")

    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())

def main():
    test_insert()
    test_select()
    # print('=================================')
    # test_delete()
    # test_select()
    # print('=================================')
    # test_update()
    # test_select()

__name__=='__main__' and main()