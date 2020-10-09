import xmlrpc.client

class OdooClient():

    def __init__(self, config):

        # info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
        # info = xmlrpc.client.ServerProxy('http://localhost:8069/start').start()

        # db_response = info

        # print('-----------db_response---------', db_response)

        # json_map = {}

        # for key, value in db_response.items():

        #     if key == 'url':
        #         json_map['url'] = value
        #     if key == 'db':
        #         json_map['db'] = value
        #     if key == 'username':
        #         json_map['username'] = value
        #     if key == 'password':
        #         json_map['password'] = value
            
        # print('--------json_map------------', json_map)

        self.url, self.db, self.username, self.password = config['url'], config['db'], config['username'], config['password']

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))

        common.version()

        self.uid = common.authenticate(
            self.db, 
            self.username, 
            self.password, 
            {}
        )

        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        self.model_name = config['model_name']
    
    def execute_db(self):

        execute_result = self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password,
            self.model_name, 
            'check_access_rights',
            ['read'], 
            {'raise_exception': False}
        )

        print('------------models------------', execute_result)

        return execute_result

    def list_records(self):

        list_records = self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password,
            self.model_name, 
            'search',
            [[['is_company', '=', True]]]
        )

        return list_records
    

    def read_records(self):

        ids = self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password,
            self.model_name, 
            'search',
            [[['is_company', '=', True]]],
            {'limit': 1}
        )

        [record] = self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password,
            self.model_name, 
            'read', 
            [ids]
        )
        # count the number of fields fetched by default

        # return len(record)

        return [record]
    
    def create_records(self):

        id = self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password, 
            self.model_name, 
            'create', 
            [
                {
                    'name': "New Partner1",
                }
            ]
        )

        create_response = {"create":"record has inserted and id is {}".format(id)}

        return create_response
    
    def update_records(self, number):

        self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password, 
            self.model_name, 
            'write', 
            [
                [number], 
                {
                    'name': "Newer partner"
                }
            ]
        )
        # get record name after having changed it
        self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password, 
            self.model_name, 
            'name_get', [[number]]
        )

        update_res = {"result":"record updated"}

        return update_res

    def delete_records(self, number):

        self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password, 
            self.model_name, 
            'unlink', 
            [[number]]
        )
        # check if the deleted record is still in the database
        self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password,
            self.model_name, 
            'search', 
            [[['id', '=', number]]]
        )
        
        delete_res = {"result":"record deleted"}

        return delete_res
    
    def search_and_read(self):

        self.models.execute_kw(
            self.db, 
            self.uid, 
            self.password,
            self.model_name, 
            'search_read',
            [[['is_company', '=', True]]],
            {'fields': ['name', 'country_id', 'comment'], 'limit': 5}
        )