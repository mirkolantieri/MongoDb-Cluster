# MongoDB-cluster

## Cluster configuration

**ConfigServer**
| Containers     | Port-forwarding |
| -------------- | ----------- |
| configServer1  | 10000:27017 |
| configServer2  | 10001:27017 |
| configServer3  | 10002:27017 |
Replica set name: _configrs_

#

**Shard1**
| Containers     | Port-forwarding |
| -------------- | ----------- |
| shard1server  | 11000:27017 |
Replica set name: _shard1rs_

#

**Shard2**
| Containers     | Port-forwarding |
| -------------- | ----------- |
| shard2server1  | 12000:27017 |
| shard2server2  | 12001:27017 |
Replica set name: _shard2rs_

#

**Shard3**
| Containers     | Port-forwarding |
| -------------- | ----------- |
| shard3server1  | 13000:27017 |
| shard3server2  | 13001:27017 |
| shard3server3  | 13002:27017 |
Replica set name: _shard3rs_

#

**Mongos**
| Container      | Port-forwarding |
| -------------- | ----------- |
| mongos         | 15000:27017 |
