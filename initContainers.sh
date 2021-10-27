docker-compose -f ./docker-compose/configServerCompose.yaml up -d 
docker-compose -f ./docker-compose/mongosCompose.yaml up -d
docker-compose -f ./docker-compose/shard1Compose.yaml up -d
docker-compose -f ./docker-compose/shard2Compose.yaml up -d
docker-compose -f ./docker-compose/shard3Compose.yaml up -d