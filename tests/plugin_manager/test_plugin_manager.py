
import unittest
import importlib

from python_toolbox.plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):
  def setUp(self):
    self.plugin_manager = PluginManager()
    self.mock_plugin = 'tests.plugin_manager.mock_plugin'

  def tearDown(self):
    pass

  def test_discover_plugins(self):
    module = importlib.import_module(self.mock_plugin)
    self.assertEquals(module.__name__, self.mock_plugin)
    self.assertEquals(module.MockPlugin.__name__, 'MockPlugin')

    plugins = self.plugin_manager.discover_plugins(module)
    self.assertEquals(len(plugins), 1)
    self.assertEquals(plugins[0].__name__, 'MockPlugin')

  def test_plugins_can_be_registered(self):
    self.plugin_manager.register_plugin(self.mock_plugin)
    self.assertEquals(self.plugin_manager.registered, set(['MockPlugin']))
    self.assertTrue(
      'status_callback' in self.plugin_manager.callbacks.registered)

  def test_plugins_can_be_unregistered(self):
    self.plugin_manager.register_plugin(self.mock_plugin)

    self.assertTrue('MockPlugin' in self.plugin_manager.registered)
    self.assertTrue('MockPlugin' in self.plugin_manager.__dict__)
    self.assertTrue(
      'status_callback' in self.plugin_manager.callbacks.registered)
    self.assertTrue(
      'status_callback' in self.plugin_manager.callbacks.__dict__)

    self.plugin_manager.unregister_plugin('MockPlugin')

    self.assertTrue('MockPlugin' not in self.plugin_manager.registered)
    self.assertTrue('MockPlugin' in self.plugin_manager.__dict__)
    self.assertTrue(
      'status_callback' not in self.plugin_manager.callbacks.registered)
    self.assertTrue(
      'status_callback' in self.plugin_manager.callbacks.__dict__)

    self.assertEquals(self.plugin_manager.MockPlugin, None)
    self.assertEquals(self.plugin_manager.callbacks.status_callback, None)
    