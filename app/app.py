# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from flask import Flask
from app.modules.author.author_routes import author_routes
from app.modules.http_error_handler.http_error_handler import http_error_handler

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.register_blueprint(author_routes)
app.register_blueprint(http_error_handler)
