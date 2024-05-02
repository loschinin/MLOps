## Start project

cd lab_3

npm run build

docker-compose up --build

open http://localhost:8080/ in browser

### Optional
docker-compose down && docker rmi -f $(docker images -q) && docker-compose up
