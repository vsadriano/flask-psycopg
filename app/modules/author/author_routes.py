# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from app.modules.author.author_controller import AuthorController
from flask import Blueprint, jsonify
import logging

author_routes = Blueprint("author", __name__)
author_controller = AuthorController()
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO)


@author_routes.route("/api/v1/authors")
def get_authors():
    try:
        authors = author_controller.get_authors()
        return jsonify(authors)
    except Exception as err:
        logging.error("Falha na coleta dos autores!")
        logging.error(f"Erro: {err}")
        if(type(err).__name__ == "BadRequest"):
            res = {
                "message": "Formato da data inválido.",
                "error": err.description,
                "success": False
            }
            return jsonify(res),err.code
        else:
            if hasattr(err, "message"):
                msg = err.message
            else:
                msg = err

            res = {
                "message": "Falha interna da aplicação.",
                "error": str(msg),
                "success": False
            }
            return jsonify(res),500

@author_routes.route("/api/v1/authors/<author_id>")
def get_author(author_id):
    try:
        author = author_controller.get_author(author_id)
        return jsonify(author)
    except Exception as err:
        logging.error("Falha na coleta do autor!")
        logging.error(f"Erro: {err}")
        if(type(err).__name__ == "BadRequest"):
            res = {
                "message": "Formato da data inválido.",
                "error": err.description,
                "success": False
            }
            return jsonify(res),err.code
        else:
            if hasattr(err, "message"):
                msg = err.message
            else:
                msg = err

            res = {
                "message": "Falha interna da aplicação.",
                "error": str(msg),
                "success": False
            }
            return jsonify(res),500