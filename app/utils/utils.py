from app.config.const import REGISTRY_SUCCEEDED_MSG
from app.models.author import Author
from werkzeug.exceptions import BadRequest


class Utils():
    def __init__(self):
        pass

    def validate_new_data(self, author_data):
        if "first_name" in author_data:
            if "last_name" in author_data:
                if "email" in author_data:
                    return Author(author_data["first_name"],
                                  author_data["last_name"],
                                  author_data["email"])
        raise BadRequest()

    def validate_update_data(self, author_data):
        if "id" in author_data:
            if "first_name" in author_data:
                if "last_name" in author_data:
                    if "email" in author_data:
                        return Author(author_data["first_name"],
                                      author_data["last_name"],
                                      author_data["email"],
                                      author_data["id"])
        raise BadRequest()

    def registry_suceeded(self):
        return REGISTRY_SUCCEEDED_MSG
