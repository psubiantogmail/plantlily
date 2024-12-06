from ._anvil_designer import MainLayoutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import AppModule
from .. import Home
from .. import Indoor
from .. import Outdoor
from .. import Data


class MainLayout(MainLayoutTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        self.navigation_link_indoor.selected = False
        self.navigation_link_data.selected = False
        self.navigation_link_data.visible = False

    def navigation_link_login_click(self, **event_args):
        if self.navigation_link_login.text == 'Login':
            AppModule.user = anvil.users.login_with_form()
            self.navigation_link_data.visible = True
            self.navigation_link_login.icon = 'mi:logout'
            self.navigation_link_login.text = 'Logout'
        else:
            anvil.users.logout()
            self.navigation_link_data.visible = False
            self.navigation_link_login.icon = 'mi:login'
            self.navigation_link_login.text = 'Login'

    def link_home_click(self, **event_args):
        open_form('Home')

    def navigation_link_indoor_click(self, **event_args):
        open_form('Indoor')

    def navigation_link_outdoor_click(self, **event_args):
        open_form('Outdoor')

    def navigation_link_data_click(self, **event_args):
        open_form('Data')
