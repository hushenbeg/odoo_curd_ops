# Run postgres database using docker image
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:10
# Run odoo using docker image
docker run -p 8069:8069 --name odoo --link db:db -t odoo
# start odoo docker instance
docker start -a odoo
# To Run and perform crud operation run the below test file
python docker_client_test.py
