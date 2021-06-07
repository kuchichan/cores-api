# cores-api

## Installation:
1. In main folder:
``` console
git submodule init
git submodule update
```
2. build & run docker compose
``` console
docker-compose --env-file=.env.example build
docker-compose --env-file=.env.example up 
```
3. To populate `users` and `cores` in database run:
``` console
docker-compose --env-file=.env.example run --rm  core-api python load_users.py
docker-compose --env-file=.env.example run --rm  core-api python load_cores.py
```
4. You can navigate api via http://127.0.0.1:8000/docs

### NOTE:
	Due to problematic API limits, pagination are omitted (offset in graph with sorting will result in overlapping core_id sets) 
