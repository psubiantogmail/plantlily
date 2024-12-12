from ._anvil_designer import DataTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..DataEdit import DataEdit


class Data(DataTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.repeating_panel.items = app_tables.plants.search()

    def button_add_click(self, **event_args):
        item = {}
        editing_form = DataEdit(item=item)
        if alert(content=editing_form, large=True):
            anvil.server.call('add_data', item)
            self.repeating_panel.items = app_tables.plants.search()
