from ._anvil_designer import MainLayoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import AppModule


class MainLayout(MainLayoutTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        self.navigation_link_indoor.selected = False
        self.navigation_link_data.selected = False
        self.navigation_link_data.visible = False

    def navigation_link_login_click(self, **event_args):
        if self.navigation_link_login.text == 'Login':
            AppModule.user = {
                'name': 'peter',
                'security': 9
            }
            self.navigation_link_data.visible = True
            self.navigation_link_login.icon = 'mi:logout'
            self.navigation_link_login.text = 'Logout'
        else:
            AppModule.user = {
                'name': '',
                'security': 0
            }
            self.navigation_link_data.visible = False
            self.navigation_link_login.icon = 'mi:login'
            self.navigation_link_login.text = 'Login'

