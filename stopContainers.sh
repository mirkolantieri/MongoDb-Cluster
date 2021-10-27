docker-compose -f ./docker-compose/configServerCompose.yaml stop
docker-compose -f ./docker-compose/mongosCompose.yaml stop
docker-compose -f ./docker-compose/shard1Compose.yaml stop
docker-compose -f ./docker-compose/shard2Compose.yaml stop
docker-compose -f ./docker-compose/shard3Compose.yaml stop