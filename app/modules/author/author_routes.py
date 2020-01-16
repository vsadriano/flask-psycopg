# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from app.modules.author.author_controller import AuthorController
from app.utils.utils import Utils
from flask import abort, Blueprint, jsonify, request, Response

author_routes = Blueprint("author", __name__)
author_controller = AuthorController()
utils = Utils()


@author_routes.route("/api/v1/authors")
def get_authors():
    authors = author_controller.get_authors()
    return jsonify(authors)


@author_routes.route("/api/v1/authors/<author_id>")
def get_author(author_id):
    author = author_controller.get_author(author_id)
    if author:
        return jsonify(author)
    return Response(status=204)


@author_routes.route("/api/v1/authors", methods=["POST"])
def save_author():
    author = utils.validate_new_data(request.get_json())
    res = author_controller.save_author(author)
    return jsonify(res), 201


@author_routes.route("/api/v1/authors", methods=["PUT"])
def update_author():
    author = utils.validate_update_data(request.get_json())
    res = author_controller.update_author(author)
    return Response(status=204)


@author_routes.route("/api/v1/authors/<author_id>", methods=["DELETE"])
def delete_author(author_id):
    author = author_controller.delete_author(author_id)
    return Response(status=204)
