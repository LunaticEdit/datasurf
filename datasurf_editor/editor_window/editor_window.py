import gi

from gi.repository import Gtk
from .project_treeview import ProjectTreeView

UI_DATA = """
<ui>
	<menubar name='MenuBar'>
		<menu action='FileMenu'>
			<menuitem action='FileQuit' />
		</menu>
		<menu action='EnvironmentMenu'>
			<menuitem action='EnvironmentConnect' />
		</menu>
	</menubar>
</ui>
"""


class EditorWindow(Gtk.Window):
	def __init__(self):
		super(EditorWindow, self).__init__()
		self.set_title("DataSurf Editor")
		self.set_default_size(350, 500)
		self.move(50, 50)
		self.connect("destroy", Gtk.main_quit)

		self.project_store = None
		self.project_store = None
		self.project_filter = None
		self.project_tree = None

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

		menubar = self.initialize_menus()

		self.project_store = Gtk.TreeStore(int, str, str)
		self.project_tree = ProjectTreeView(self.project_store)

		box.pack_start(menubar, False, False, 0)
		box.pack_start(self.project_tree, True, True, 0)

		self.add(box)
		self.show_all()

	def initialize_menus(self):
		action_group = Gtk.ActionGroup("my_actions")
		self.add_file_menu_actions(action_group)
		self.add_environment_menu_actions(action_group)

		uimanager = Gtk.UIManager()
		uimanager.add_ui_from_string(UI_DATA)
		self.add_accel_group(uimanager.get_accel_group())
		uimanager.insert_action_group(action_group)

		menubar = uimanager.get_widget("/MenuBar")
		return menubar

	def add_file_menu_actions(self, action_group):
		action_filemenu = Gtk.Action("FileMenu", "File", None, None)
		action_group.add_action(action_filemenu)

		action_quit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
		action_quit.connect("activate", self.on_menu_file_quit)
		action_group.add_action_with_accel(action_quit, None)

	def add_environment_menu_actions(self, action_group):
		action_environmentmenu = Gtk.Action("EnvironmentMenu", "Environment", None, None)
		action_group.add_action(action_environmentmenu)

		action_connect = Gtk.Action("EnvironmentConnect", "_Connect", None, Gtk.STOCK_CONNECT)
		action_connect.connect("activate", self.on_menu_environment_connect)
		action_group.add_action_with_accel(action_connect, None)

	def on_menu_file_quit(self, widget):
		Gtk.main_quit()

	def on_menu_environment_connect(self, widget):
		pass

	def run(self):
		Gtk.main()
