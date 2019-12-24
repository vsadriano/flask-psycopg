#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.modules.author.author_service import AuthorService
from werkzeug.exceptions import BadRequest
import logging


class AuthorController():
    def __init__(self):
        self.author_svc = AuthorService()
        logging.basicConfig(format='''%(asctime)s %(levelname)s: %(message)s''',
            level=logging.INFO, datefmt='%d/%m/%Y %H:%M:%S')

    def get_authors(self):
        logging.info("Consultando lista de autores...")
        authors = []
        data = self.author_svc.get_authors()
        if data:
            authors = self._build_authors_json(data)
        return {"authors": authors}

    def get_author(self, author_id):
        logging.info(f"Consultando dados do autor {author_id}...")
        data = self.author_svc.get_author(author_id)
        if not data:
            logging.error(f"Autor {author_id} não consta na base!")
            raise BadRequest(f"Autor {author_id} não consta na base!")
        return {"author_id": data.id, "author_name": data.name}

    def save_author(self, author_name):
        self.author_svc.insert_author(author_name)
        logging.info(f"Autor {author_name} cadastrado com sucesso!")

    def update_author(self, author_id, author_name):
        exists = self.get_author(author_id)
        if not exists:
            logging.error(f"Autor {author_id} não consta na base!")
            raise BadRequest(f"Autor {author_id} não consta na base!")
        self.author_svc.update_author(author_id, author_name)
        logging.info(f"Dados do autor {author_id} atualizados com sucesso!")

    def delete_author(self, author_id):
        exists = self.get_author(author_id)
        if not exists:
            logging.error(f"Autor {author_id} não consta na base!")
            raise BadRequest(f"Autor {author_id} não consta na base!")
        self.author_svc.delete_author(author_id)
        logging.info(f"Dados do autor {author_id} removidos com sucesso!")

    def _build_authors_json(self, data):
        json = []
        for d in data:
            author = {
                "author_id": d.id,
                "author_name": d.name
            }
            json.append(author)
        return json
