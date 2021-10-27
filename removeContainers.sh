docker-compose -f ./docker-compose/configServerCompose.yaml down
docker-compose -f ./docker-compose/mongosCompose.yaml down
docker-compose -f ./docker-compose/shard1Compose.yaml down
docker-compose -f ./docker-compose/shard2Compose.yaml down
docker-compose -f ./docker-compose/shard3Compose.yaml down