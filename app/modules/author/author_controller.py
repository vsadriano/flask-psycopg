#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.modules.author.author_service import AuthorService
from app.utils.utils import Utils
from werkzeug.exceptions import BadRequest
import logging


class AuthorController():
    def __init__(self):
        self.author_svc = AuthorService()
        logging.basicConfig(format='''%(asctime)s %(levelname)s: %(message)s''',
                            level=logging.INFO, datefmt='%d/%m/%Y %H:%M:%S')
        self.utils = Utils()

    def get_authors(self):
        logging.info("Obtendo lista de autores...")
        authors = []
        data = self.author_svc.get_authors()
        if data:
            logging.info("Lista de autores obtida com sucesso!")
            authors = self._build_authors_json(data)
        return {"authors": authors}

    def get_author(self, author_id):
        logging.info(f"Consultando dados do autor {author_id}...")
        data = self.author_svc.get_author(author_id)
        if not data:
            logging.info(f"Autor {author_id} não consta na base!")
            return None
        logging.info("Dados obtidos com sucesso!")
        return {"id": data.id,
                "first_name": data.first_name,
                "last_name": data.last_name,
                "email": data.email}

    def save_author(self, author):
        logging.info("Inserindo novo registro na base...")
        self.author_svc.insert_author(author)
        logging.info("Novo autor registrado com sucesso!")
        return self.utils.registry_suceeded()

    def update_author(self, author):
        logging.info("Atualizando registro na base...")
        exists = self.get_author(author.id)
        if not exists:
            logging.error(f"Autor {author.id} não consta na base!")
            raise BadRequest()
        self.author_svc.update_author(author)
        logging.info(f"Dados do autor {author.id} atualizados com sucesso!")

    def delete_author(self, author_id):
        logging.info("Removendo registro da base...")
        exists = self.get_author(author_id)
        if not exists:
            logging.error(f"Autor {author_id} não consta na base!")
            raise BadRequest()
        self.author_svc.delete_author(author_id)
        logging.info(f"Dados do autor {author_id} removidos com sucesso!")

    def _build_authors_json(self, data):
        json = []
        for d in data:
            author = {
                "id": d.id,
                "first_name": d.first_name,
                "last_name": d.last_name,
                "email": d.email
            }
            json.append(author)
        return json
