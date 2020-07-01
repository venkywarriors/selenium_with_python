'''
Created on 01-Jul-2020

@author: venkateshwara D
'''
from jproperties import Properties
import os 

path = os.path.dirname(__file__) +"\\resources\\app-config.properties"
print( path ) 
 
configs = Properties()
with open(path, 'rb') as config_file:
    configs.load(config_file)
    
print(configs.get("DB_User"))  
# PropertyTuple(data='root', meta={})
 
print(f'Database User: {configs.get("DB_User").data}')  
# Database User: root
 
print(f'Database Password: {configs["DB_PWD"].data}')  
# Database Password: root@neon
 
db_configs_dict = {}
list_keys = [] 
items_view = configs.items() 

for item in items_view:
    db_configs_dict[item[0]] = item[1].data
    list_keys.append(item[0])
#Getting List of Keys from the Properties File 
print("Output as List ",list_keys)
print("Dictionary ",db_configs_dict)
    
 