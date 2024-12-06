import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_data(data):
  if data.get('name') and data.get('description') and data.get('added') and data.get('type'):
      app_tables.plant.add_row(**data)