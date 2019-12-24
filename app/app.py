# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from flask import Flask, render_template
from app.modules.author.author_routes import AuthorRoutes

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.register_blueprint(author_routes)

@app.route("/api/v1")
def index():
    return(render_template('index.html', titulo="API GUnicorn/Flask", cabecalho="CRUDE"))