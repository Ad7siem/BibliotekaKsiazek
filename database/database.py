import sqlite3
from treebase import Parser

# database = 'database/database.db'
database = str(Parser().get_parser('database', 'directory')) + '/database.db'

def create_table():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("""CREATE TABLE if not exists listofbook (
                title text,
                author text,
                position text,
                category text,
                date_rental text,
                person_rental text, 
                other text
            )""")

    c.execute("""CREATE TABLE if not exists personrental(
                firstname text,
                lastname text,
                team text,
                contact text
            )""")

    c.execute("""CREATE TABLE if not exists categories(
                category text
            )""")

    conn.commit()
    conn.close()


def show_database(name):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM {name}")

    items = c.fetchall()

    conn.commit()
    conn.close()

    return items

def add_records_listofbook(records):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.executemany("INSERT INTO listofbook VALUES (?,?,?,?,?,?,?)", (records))

    conn.commit()
    conn.close()

def add_records_personrental(record):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("INSERT INTO personrental VALUES (?,?,?,?)", (record))

    conn.commit()
    conn.close()

def add_records_categories(record):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("INSERT INTO categories VALUES (?)", (record))

    conn.commit()
    conn.close()

def delete_record(name, ID):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"DELETE FROM {name} WHERE rowid = (?)", (ID,))

    conn.commit()
    conn.close()

def delete_records(ID):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.executemany("DELETE FROM listofbook WHERE rowid = ?", [(a,) for a in ID])

    conn.commit()
    conn.close()

def update_record(record, ID): #, name, newRecord, column, key):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # c.execute(f"UPDATE {name} SET {column} = {newRecord} WHERE {column} = (?)", key)
    c. execute("""UPDATE listofbook SET 
            title = :title,
            author = :author,
            position = :position,
            category = :category,
            date_rental = :date_rental,
            person_rental = :person_rental,
            other = :other

            WHERE oid = :oid""",
            {
                'title': record[0],
                'author': record[1],
                'position': record[2],
                'category': record[3],
                'date_rental': record[4],
                'person_rental': record[5],
                'other': record[6],
                'oid': ID
            }
        )
    conn.commit()
    conn.close()


def lookup_records(name):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"""SELECT rowid, * FROM listofbook WHERE rowid LIKE '%{name}%' OR title LIKE '%{name}%' OR author LIKE '%{name}%' OR category LIKE '%{name}%' OR person_rental LIKE '%{name}%'""")

    records = c.fetchall()

    conn.commit()
    conn.close()

    return records


def lookup_records_person(name):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"""SELECT rowid, * FROM personrental WHERE rowid LIKE '%{name}%' OR firstname LIKE '%{name}%' OR lastname LIKE '%{name}%' OR team LIKE '%{name}%'""")

    records = c.fetchall()

    conn.commit()
    conn.close()

    return records

    