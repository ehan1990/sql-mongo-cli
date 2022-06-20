
db-up:
	docker run --name db -p 27017:27017 -d mongo mongod

db-ssh:
	docker exec -it db bash

install:
	python3 setup.py install

uninstall:
	pip3 uninstall sql-mongo-cli -y

clean:
	rm -r build dist sql_mongo_cli.egg-info

purge:
	make clean
	make uninstall
