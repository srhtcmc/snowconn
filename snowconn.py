import snowflake.connector as sf
import config as config

class snow():
    
    
    
    def __init__(self):
        
        self.conn = sf.connect(
            user= config.user,
            password= config.password,
            account= config.account,
            warehouse = config.warehouse,
            database = config.database,
            role = config.role
            )
    
    def execute_query(self,connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        
    def get_df(self,sf_query):
        sf_query = sf_query
        cursor = self.conn.cursor()
        cursor.execute(sf_query)   
        df = cursor.fetch_pandas_all()     
        cursor.close()
        
        return df
        
    def PULL(self,sf_query): 
    
        try:
            sql = 'use role {}'.format(config.role)
            self.execute_query(self.conn,sql)
                        
            sql = 'use {}'.format(config.database)
            self.execute_query(self.conn,sql)
            
            sql = 'use warehouse {}'.format(config.warehouse)
            self.execute_query(self.conn,sql)
            
            try:
                sql ='alter warehouse {} resume'.format(config.warehouse)
                self.execute_query(self.conn,sql)
            except :
                pass
            
            
        except Exception as exp :
            print(exp)
        
        return self.get_df(sf_query)
 
    
        
