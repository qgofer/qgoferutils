# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_db.ipynb.

# %% auto 0
__all__ = ['QGoferDBWrapper']

# %% ../nbs/01_db.ipynb 3
import sqlite3

# %% ../nbs/01_db.ipynb 4
class QGoferDBWrapper:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Create a table in the database
        :param table_name: name of the table to create
        :param columns: list of columns to create wih their data type
        :return: None
        """
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, columns, values):
        """
        Insert a row into the database
        :param table_name: name of the table to insert into
        :param columns: a string of comma seperated values to insert into
        :param values: a string of comma seperated values to insert into the table. Noe that each word should be single quoted eg "'max', 'min'"
        :return: None
        """
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_many(self, table_name, columns, values):
        """
        Insert multiple rows into the database
        :param table_name: name of the table to insert into
        :param columns:  a string of comma seperated values to insert into
        :param values:  a string of comma seperated values to insert into the table. Noe that each word should be single quoted eg "'max', 'min'"
        :return: None
        """
        self.cursor.executemany(
            f"INSERT INTO {table_name} ({columns}) VALUES ({values})", values
        )
        self.conn.commit()

    def select(self, table_name, columns, where=None):
        """
        Select rows from the database
        :param table_name: name of the table to select from
        :param columns: list of columns to select
        :param where: where clause to filter rows
        :return: list of rows
        """
        if where is None:
            self.cursor.execute(f"SELECT ({columns}) FROM {table_name}")
        else:
            self.cursor.execute(f"SELECT ({columns}) FROM {table_name} WHERE {where}")
        return self.cursor.fetchall()

    def search(self, table_name, column_name, q):
        """
        Search rows from the database
        :param table_name: name of the table to search from
        :param column_name: name of the column to search
        :param q: search query
        :return: list of rows
        """
        self.cursor.execute(
            f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%{q}%'"
        )
        return self.cursor.fetchall()

    def update(self, table_name, set_clause, where):
        """
        Update rows in the database
        :param table_name: name of the table to update
        :param set_clause: set clause to update rows
        :param where: where clause to filter rows
        :return: None
        """
        self.cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {where}")
        self.conn.commit()

    def delete(self, table_name, where):
        """
        Delete rows from the database
        :param table_name: name of the table to delete from
        :param where: where clause to filter rows
        :return: None
        """
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {where}")
        self.conn.commit()

    def drop_table(self, table_name):
        """
        Drop a table from the database
        :param table_name: name of the table to drop
        :return: None
        """
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()
