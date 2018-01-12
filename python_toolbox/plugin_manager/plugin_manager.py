
from importlib import import_module

from python_toolbox.utilities import dunder_check
from python_toolbox.utilities import not_lambda
from python_toolbox.registrar import Registrar
from .plugin import Plugin

class PluginManager(Registrar):
    '''
        The PluginManager class provides a way to register classes derived from
        the Plugin class. Registers any callbacks requested by the Plugin
        class, making them dynamically available via the
        plugin_manager.callbacks Registrar.

        Additionally, PluginManager provides the ability to register a python
        module which is imported and searched for any classes derived from
        the Plugin class which are then registered using the aforementioned
        register_plugin.

        The Plugin class and method used to discover callbacks shall be
        optionally assignable.
    '''
    def __init__(self):
        super().__init__()

        self.callbacks = Registrar()

    def discover_plugins(self, module):
        '''
            Searches module.__dict__ for values that are subclasses of the
            defined Plugin type.
        '''
        discovered_plugins = []
        item_names = list(filter(not_lambda(dunder_check), vars(module)))
        for item_name in item_names:
            item = vars(module)[item_name]
            if issubclass(item, Plugin):
                discovered_plugins.append(item)
        return discovered_plugins

    def register_plugin(self, plugin_module_name, package=None):
        '''
            Searches for a module registered with python (ex: using
            PYTHON_PATH), searches for any classes within the module that
            subclass Plugin, and registers them with this Registrar.
        '''
        imported_module = import_module(plugin_module_name, package)
        plugin_classes = self.discover_plugins(imported_module)

        for plugin_class in plugin_classes:
            plugin_instance = plugin_class()
            for callback in plugin_instance.callbacks.items():
                self.callbacks.register(callback[1], callback[0])
            self.register(plugin_instance, plugin_class.__name__)

    def unregister_plugin(self, plugin_name):
        '''
            Unregisters the chosen plugin by name.

            Any unregistered callables will throw an exception if called after
            a call to this method. Non-callables will be set to None.
        '''
        plugin_instance = self.__dict__[plugin_name]
        registered_callbacks = plugin_instance.callbacks.keys()

        for callback in registered_callbacks:
            self.callbacks.unregister(callback)

        self.unregister(plugin_name)
