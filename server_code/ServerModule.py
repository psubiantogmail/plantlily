import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_data(data):
    print(data)
    if data.get('name') and data.get('description') and data.get('added') and data.get('type'):
        #app_tables.plants.add_row(**data)
        app_tables.plants.add_row(name=data.get('name'),
                                 description=data.get('description'),
                                 added=data.get('added'),
                                 type=data.get('type'))