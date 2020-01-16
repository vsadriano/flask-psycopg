#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.dao.base_dao import BaseDao
from app.models.author import Author


class AuthorService(BaseDao):
    def __init__(self):
        BaseDao.__init__(self)

    def get_authors(self):
        sql = """SELECT author_fname,
        author_lname,
        author_email,
        author_id
        FROM author"""

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [Author(*row) for row in rows] if rows else None

    def get_author(self, author_id):
        sql = f"""SELECT author_fname,
        author_lname,
        author_email,
        author_id
        FROM author
        WHERE author_id = %s"""

        self.cursor.execute(sql, (author_id,))
        row = self.cursor.fetchone()
        return Author(*row) if row else None

    def insert_author(self, author):
        sql = f"""INSERT INTO author
        (
            author_fname,
            author_lname,
            author_email
        )
        VALUES
        (
            %s, %s, %s
        )"""

        self.cursor.execute(sql, (author.first_name,
                                  author.last_name,
                                  author.email))
        self.commit()

    def update_author(self, author):
        sql = f"""UPDATE author
        SET author_fname = %s,
        author_lname = %s,
        author_email = %s
        WHERE author_id = %s"""

        self.cursor.execute(sql, (author.first_name,
                                  author.last_name,
                                  author.email,
                                  author.id))
        self.commit()

    def delete_author(self, author_id):
        sql = f"""DELETE FROM author
        WHERE author_id = %s"""

        self.cursor.execute(sql, (author_id))
        self.commit()
