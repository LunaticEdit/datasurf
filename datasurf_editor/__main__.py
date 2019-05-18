import logging
import gi
gi.require_version('Gtk', '3.0')
from editor_window import EditorWindow

if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
	logging.info('DataSurf Editor is starting')
	window = EditorWindow()
	window.run()
