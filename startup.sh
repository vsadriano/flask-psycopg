# Inicialização local
# Comentar as linhas do serviço backend no docker-compose.yml
# export DB_HOST=0.0.0.0
# export DB_NAME=crude_db
# export DB_USER=postgres
# export DB_PASSWORD=password
# export DB_PORT=5432
# export DB_SCHEMA=public

# gunicorn -w 2 --threads 4 -b 0.0.0.0:8080 main:app

# Inicialização pelo docker-compose.yml
pip install -r requirements.txt
gunicorn -b 0.0.0.0:8080 main:app