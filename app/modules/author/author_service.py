#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.dao.base_dao import BaseDao
from app.models.author import Author
import logging


class AuthorServive(BaseDao):
    def __init__(self):
        BaseDao.__init__(self)
        logging.basicConfig(format='''%(asctime)s %(levelname)s: %(message)s''',
            level=logging.INFO, datefmt='%d/%m/%Y %H:%M:%S')

    def get_authors(self):
        sql = """SELECT author_id,
        author_name
        FROM author"""

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return [Author(*row) for row in rows] if rows else None

    def get_author(self, author_id):
        sql = f"""SELECT author_id,
        author_name
        FROM author
        WHERE author_id='{author_id}'"""

        self.cursor.execute(sql)
        row = self.cursor.fetchone()

        return Author(*row) if row else None

    def insert_author(self, author_name):
        sql=f"""INSERT INTO author
        (
            author_name
        )
        VALUES
        (
            {author_name}
        )"""

        self.cursor.execute(sql)
        self.commit()

    def update_author(self, author_id, author_name):
        sql=f"""UPDATE author
        SET author_name='{author_name}'
        WHERE author_id='{author_id}'"""

        self.cursor.execute(sql)
        self.commit()

    def delete_author(self, author_id):
        sql=f"""DELETE FROM author
        WHERE author_id='{author_id}'"""

        self.cursor.execute(sql)
        self.commit()

    # def persist_author(self, author):
    #     data = self.get_author(author.id)
    #     if not data:
    #         logging.info(f"Inserindo {author.name} na base...")
    #         self._insert_author(author)
    #     else:
    #         logging.info(f"Atualizando registro do author {author.name} na base...")
    #         self._update_author(author)
