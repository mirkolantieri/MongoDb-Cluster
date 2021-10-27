docker-compose -f ./docker-compose/configServerCompose.yaml start
docker-compose -f ./docker-compose/mongosCompose.yaml start
docker-compose -f ./docker-compose/shard1Compose.yaml start
docker-compose -f ./docker-compose/shard2Compose.yaml start
docker-compose -f ./docker-compose/shard3Compose.yaml start