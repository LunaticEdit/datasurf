import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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
		self.project_tree_workflows = None
		self.project_tree_sources = None
		self.project_tree_targets = None
		self.project_tree_file_formats = None
		self.project_tree_variables = None

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

		menubar = self.initialize_menus()
		treeview = self.initialize_project_tree()

		box.pack_start(menubar, False, False, 0)
		box.pack_start(treeview, True, True, 0)

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

	def initialize_project_tree(self):
		self.project_store = Gtk.TreeStore(int, str, str)
		self.project_filter = self.project_store.filter_new()
		self.project_tree = Gtk.TreeView.new_with_model(self.project_filter)
		self.project_tree.set_headers_visible(False)

		project_tree_project = self.project_store.append(None, [0, "gtk-home", "Untitled Project"])
		self.project_tree_workflows = self.project_store.append(project_tree_project, [0, "gtk-directory", "Workflows"])
		self.project_tree_sources = self.project_store.append(project_tree_project, [0, "gtk-directory", "Sources"])
		self.project_tree_targets = self.project_store.append(project_tree_project, [0, "gtk-directory", "Targets"])
		self.project_tree_file_formats = self.project_store.append(project_tree_project, [0, "gtk-directory", "File Formats"])
		self.project_tree_variables = self.project_store.append(project_tree_project, [0, "gtk-directory", "Variables"])

		self.project_tree.append_column(Gtk.TreeViewColumn("", Gtk.CellRendererPixbuf(), icon_name=1))
		self.project_tree.append_column(Gtk.TreeViewColumn("Name", Gtk.CellRendererText(), text=2))

		scroll_window = Gtk.ScrolledWindow()
		scroll_window.set_vexpand(True)
		scroll_window.add(self.project_tree)
		self.project_tree.expand_all()
		return scroll_window

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
