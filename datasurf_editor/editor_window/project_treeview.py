import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ProjectTreeView(Gtk.ScrolledWindow):
	def __init__(self, project_store):
		super(ProjectTreeView, self).__init__()
		self.project_store = project_store
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

		self.set_vexpand(True)
		self.add(self.project_tree)
		self.project_tree.expand_all()

