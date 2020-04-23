import sqlite3
from typing import Dict


class SQLiteContext:
    def __init__(self):
        self.path = 'base.db'

    def __enter__(self):
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.connect.rollback()
        else:
            self.connect.commit()
        self.connect.close()


def create_db():
    with SQLiteContext() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT  EXISTS class(name TEXT PRIMARY  KEY)""")

        cursor.execute(
            """CREATE TABLE IF NOT  EXISTS animal(id INTEGER PRIMARY KEY, nickname TEXT, class TEXT, eating TIMESTAMP, certificat INTEGER, chip TEXT, box INTEGER NOT NULL, FOREIGN KEY(box) REFERENCES box(number), FOREIGN KEY(class) REFERENCES class(name))"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT  EXISTS box (number INTEGER PRIMARY KEY, personal TEXT, FOREIGN KEY(personal) REFERENCES personal(name))"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT  EXISTS personal (fullname TEXT PRIMARY KEY, zoo TEXT, FOREIGN KEY(zoo) REFERENCES zoo(address))"""
        )
        cursor.execute("""CREATE TABLE IF NOT  EXISTS zoo (address TEXT)""")


def create_classes():
    with SQLiteContext() as cursor:
        for item in ['tiger', 'chiken']:
            cursor.execute(f"""INSERT INTO class(name) VALUES("{item}")""")


def get_addresses():
    with SQLiteContext() as cursor:
        cursor.execute("""SELECT address FROM zoo""")
        return cursor.fetchall()


def get_boxes():
    with SQLiteContext() as cursor:
        cursor.execute("""SELECT number FROM box""")
        return cursor.fetchall()


def get_classes():
    with SQLiteContext() as cursor:
        cursor.execute("""SELECT name FROM class""")
        return cursor.fetchall()


def get_animals():
    with SQLiteContext() as cursor:
        cursor.execute("SELECT  FROM animals")
        return cursor.fetchall()


def get_animal(animal_id: int):
    with SQLiteContext() as cursor:
        cursor.execute(
            f"""SELECT id, box, class, nickname, box.personal, chip  FROM animal INNER JOIN box ON box.number = box WHERE id = '{animal_id}'"""
        )
        return cursor.fetchone()


def get_personal(personal: str):
    with SQLiteContext() as cursor:
        cursor.execute(
            f"""SELECT id, box, class, nickname  FROM animal INNER JOIN box ON box.number= box WHERE box.personal='{personal}'"""
        )
        return cursor.fetchone()


def add_animal(data: Dict):
    with SQLiteContext() as cursor:
        # cursor.execute(f"""INSERT OR IGNOR INTO class(name) VALUES("{data['animal']}") """)
        cursor.execute(
            f"""INSERT OR IGNORE INTO zoo(address) VALUES("{data['address']}")"""
        )
        cursor.execute(
            f"""INSERT OR IGNORE INTO personal(fullname, zoo) VALUES("{data['personal']}", "{data['address']}")"""
        )
        cursor.execute(
            f"""INSERT OR IGNORE INTO box(number , personal) VALUES("{data['box']}", "{data['personal']}")"""
        )
        cursor.execute(
            f"""INSERT INTO animal(id, nickname, class, eating, certificat, chip, box) VALUES(
"{int(data['id'])}", "{data['nickname']}", "{data['animal']}", "{data['eating']}", "{data['certificat']}","{data['chip']}", "{data['box']}") """
        )
