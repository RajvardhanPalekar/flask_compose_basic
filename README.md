# flask_compose_basic

Very basic flask app deployment on docker compose

Requirements - Docker

#Steps for Running

1. Clone the repo
2. docker-compose build
3. docker-compose up -d

You can add and get quotes using curl
   e.g.
    curl -i -H "Content-Type: application/json" -X GET  http://0.0.0.0:3000/api/v1/get-quotes
    curl -i -H "Content-Type: application/json" -X POST -d '{"quote":"To find afault is easy; to do better may                  be difficult. -- Plutarch"}' http://0.0.0.0:3000/api/v1/add-quote
