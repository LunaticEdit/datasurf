import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


UI_MENU = """
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
		self.connect("destroy", Gtk.main_quit)

		action_group = Gtk.ActionGroup("my_actions")
		self.add_file_menu_actions(action_group)
		self.add_environment_menu_actions(action_group)

		uimanager = Gtk.UIManager()
		uimanager.add_ui_from_string(UI_MENU)
		self.add_accel_group(uimanager.get_accel_group())
		uimanager.insert_action_group(action_group)

		menubar = uimanager.get_widget("/MenuBar")
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		box.pack_start(menubar, False, False, 0)
		
		self.project_store = Gtk.TreeStore(int, str)
		self.project_filter = self.project_store.filter_new()
		self.project_tree = Gtk.TreeView.new_with_model(self.project_filter)
		self.project_tree.set_headers_visible(False)
		
		self.project_tree_workflows = self.project_store.append(None, [0, "Workflows"])
		self.project_tree_sources = self.project_store.append(None, [0, "Sources"])
		self.project_tree_targets = self.project_store.append(None, [0, "Targets"])
		self.project_tree_file_formats = self.project_store.append(None, [0, "File Formats"])
		self.project_tree_variables = self.project_store.append(None, [0, "Variables"])

		self.project_tree.append_column(Gtk.TreeViewColumn("Name", Gtk.CellRendererText(), text=1))
		scroll_window = Gtk.ScrolledWindow()
		scroll_window.set_vexpand(True)
		scroll_window.add(self.project_tree)
		box.pack_start(scroll_window, True, True, 0)

		self.add(box)
		self.show_all()

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
