from ._anvil_designer import IndoorTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import AppModule


class Indoor(IndoorTemplate):
    def __init__(self, page='collections', selected_item=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.page=page
        self.sort=self.dropdown_menu_sort.selected_value
        self.layout.layout.show_sidesheet = False
        self.display_items()

        # Any code you write here will run before the form opens.


    def display_items(self, order='Alphabetical'):
        if self.page == 'plants':
            items = app_tables.plants.search()
            self.page_heading.text = 'Indoor Plants'
            self.layout.plants_link.selected = True
            self.layout.accessories_link.selected = False