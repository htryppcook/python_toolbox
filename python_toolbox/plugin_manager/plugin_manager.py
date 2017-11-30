
from importlib import import_module

from python_toolbox.registrar import Registrar
from .plugin import Plugin

# The PluginManager provides a way to register classes derived from the Plugin
#   class. Registers any callbacks requested by the Plugin class, making them
#   dynamically available via the plugin_manager.callbacks Registrar.
# Additionally, PluginManager provides the ability to register a python module
#   which is imported and searched for any classes derived from the Plugin
#   class which are then registered using the aforementioned register_plugin.
# The Plugin class and method used to discover callbacks shall be optionally
#   assignable.

class PluginManager(Registrar):

  def __init__(self):
    super().__init__()

    self.callbacks = Registrar()
    self.not_dunder = lambda x : not x.startswith('_')

  def discover_plugins(self, module):
    discovered_plugins = []
    item_names = list(filter(self.not_dunder, module.__dict__))
    for item_name in item_names:
      item = vars(module)[item_name]
      if issubclass(item, Plugin):
        discovered_plugins.append(item)
    return discovered_plugins

  def register_plugin(self, plugin_module_name, package=None):
    imported_module = import_module(plugin_module_name, package)
    plugin_classes = self.discover_plugins(imported_module)

    for PluginClass in plugin_classes:
      plugin_instance = PluginClass()
      for callback in plugin_instance.callbacks.items():
        self.callbacks.register(callback[1], callback[0])
      self.register(plugin_instance, PluginClass.__name__)

  def unregister_plugin(self, plugin_name):
    plugin_instance = self.__dict__[plugin_name]
    registered_callbacks = plugin_instance.callbacks.keys()

    for callback in registered_callbacks:
      self.callbacks.unregister(callback)

    self.unregister(plugin_name)
