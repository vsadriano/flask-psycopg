BAD_REQUEST_MSG = {
    "status": 400,
    "message": "Falha na formação da requisição.",
    "error": "Bad Request",
    "success": False
}
GENERIC_ERROR_MSG = {
    "status": None,
    "message": "Falha não prevista.",
    "error": "Server Exception",
    "success": False
}
INTERNAL_ERROR_MSG = {
    "status": 500,
    "message": "Falha interna da aplicação.",
    "error": "Internal Server Error",
    "success": False
}
NO_CONTENT_MSG = {
    "status": 204,
    "message": "Nenhum conteúdo a ser retornado.",
    "success": True
}
NOT_FOUND_MSG = {
    "status": 404,
    "message": "Endpoint não encontrado.",
    "error": "Not Found",
    "success": False
}
REGISTRY_SUCCEEDED_MSG = {
    "status": "201: Created",
    "message": "Registro realizado com sucesso!",
    "success": True
}
