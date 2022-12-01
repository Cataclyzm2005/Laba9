import sqlite3

from sqlite3 import Error


# Функція для створення з'єднання до БД 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


# Вибір всіх значень в таблиці tasks
def select_all_tasks(conn):
    sql = 'SELECT t.task, t.data, p.prior_name FROM tasks t JOIN prior p ON t.prior = p.id'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Вибрати завдання з найвищим приорітетом
def select_high_pr_tasks(conn):
    sql = 'SELECT t.task, t.data, p.prior_name FROM tasks t JOIN prior p ON t.prior = p.id WHERE t.prior = 1'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Створення нового завдання
def create_task(conn, task):
    sql = ''' INSERT INTO tasks(task, data, prior)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


# Оновлення дати в завданні
def update_data_task(conn, data):
    sql = ''' UPDATE tasks
              SET data = ?
              WHERE task = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


# Видалення завдання за його текстом
def remove_task(conn, removed_task):
    sql = ''' DELETE FROM tasks WHERE task = ? '''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


# Головна функція, яка виконується під час запуску скрипта
def main():

    # Шлях до БД
    database = r"db.db" 
 
    # Встановлення з'єднання
    conn = create_connection(database)

    # Використовууючи встановлене з'єднання виконуються операції над БД
    with conn:
        print("\nВсі завдання (завдання, дата, приорітет)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nЗавдання з найвищим приорітетом (завдання, дата, приорітет)")
        select_high_pr_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nВставка нового рядка...")
        create_task(conn, ('Захистити попередні лабораторні','01-12-2020',1))
        print("\nВсі завдання (завдання, дата, приорітет)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nЗміна рядка...")
        update_data_task(conn, ('01-12-2019','Захистити попередні лабораторні'))
        print("\nВсі завдання (завдання, дата, приорітет)")
        select_all_tasks(conn)        
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nВставка нового рядка...")
        create_task(conn, ('Захистити лабораторну 11','01-01-2020',1))
        print("\nВсі завдання (завдання, дата, приорітет)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nВидалення рядка")
        remove_task(conn, ('Захистити лабораторну 11',))
        print("\nВсі завдання (завдання, дата, приорітет)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")
        
 
if __name__ == '__main__':
    main()
