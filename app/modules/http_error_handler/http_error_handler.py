from app.config.const import BAD_REQUEST_MSG, GENERIC_ERROR_MSG, INTERNAL_ERROR_MSG, NOT_FOUND_MSG
from flask import Blueprint, json
from werkzeug.exceptions import BadRequest, HTTPException, InternalServerError, NotFound
import logging

http_error_handler = Blueprint("http_error_handler", __name__)
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s",
                    level=logging.INFO)


@http_error_handler.app_errorhandler(HTTPException)
def generic_error_handler(err):
    logging.error("Falha na operação!")
    logging.error(err)
    res = err.get_response()
    res.data = json.dumps(GENERIC_ERROR_MSG)
    res.content_type = "application/json"
    return res


@http_error_handler.app_errorhandler(BadRequest)
def bad_request_handler(err):
    logging.error("Falha na operação!")
    logging.error(err)
    res = err.get_response()
    res.data = json.dumps(BAD_REQUEST_MSG)
    res.content_type = "application/json"
    return res


@http_error_handler.app_errorhandler(NotFound)
def not_found_handler(err):
    logging.error("Falha na operação!")
    logging.error(err)
    res = err.get_response()
    res.data = json.dumps(NOT_FOUND_MSG)
    res.content_type = "application/json"
    return res
