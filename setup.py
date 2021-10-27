from pymongo import MongoClient

def replica_sets():
    connectionStrings = (
        'mongodb://localhost:10000',    # configServer
        'mongodb://localhost:11000',    # shard1server
        'mongodb://localhost:12000',    # shard2server1
        'mongodb://localhost:13000',    # shard3server1
    )

    configs = (
        """
        {
            '_id': 'configrs',
            'configsvr': true,
            'members': [
                { '_id' : 0, 'host' : 'configServer1:27017' },
                { '_id' : 1, 'host' : 'configServer2:27017' },
                { '_id' : 2, 'host' : 'configServer3:27017' }
            ]
        }
        """,
        """
        {
            '_id': 'shard1rs',
            'members': [
                { '_id' : 0, 'host' : 'shard1server:27017' }
            ]
        }
        """,
        """
          {
            '_id': 'shard2rs',
            'members': [
                { '_id' : 0, 'host' : 'shard2server1:27017' },
                { '_id' : 1, 'host' : 'shard2server2:27017' }
            ]
        }
        """,
        """
          {
            '_id': 'shard3rs',
            'members': [
                { '_id' : 0, 'host' : 'shard3server1:27017' },
                { '_id' : 1, 'host' : 'shard3server2:27017' },
                { '_id' : 2, 'host' : 'shard3server3:27017' }
            ]
        }
        """
    )

    for index, string in enumerate(connectionStrings):
        print(f'Configuring {string} ...')
        client = MongoClient(string)
        client.admin.command('replSetInitiate', configs[index]);
        # print(client.admin.command('replSetGetStatus'))
        client.close()

    print('Done')

def add_shards():
    print('Adding shards to mongos...')
    client = MongoClient('mongodb://localhost:15000')   # istanza mongos
    client.admin.command('addShard', 'shard1rs/shard1server:27017');
    # client.admin.command('addShard', 'shard2rs/shard2server1:27017,shard2server2:27017');
    # client.admin.command('addShard', 'shard3rs/shard3server1:27017,shard3server2:27017,shard3server3:27017');
    # sh.status()
    print(client.admin.command('listShards'))
    # listShards
    client.close()
    print('Done')

if __name__ == "__main__":
    # inizializzazione replica sets
    # replica_sets()

    # aggiunta shards al mongos
    # add_shards()

    client = MongoClient('mongodb://localhost:12000')
    print(client.admin.command('replSetGetStatus')['members'])
    client.close()


 