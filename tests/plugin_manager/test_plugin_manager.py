
import unittest
import importlib

from python_toolbox.plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):
    '''
        Tests for python_toolbox.plugin_manager.plugin_manager
    '''
    def setUp(self):
        self.plugin_manager = PluginManager()
        self.mock_plugin = 'tests.plugin_manager.mock_plugin'

    def tearDown(self):
        pass

    def test_discover_plugins(self):
        '''
            Test that plugins are discovered correctly
        '''
        module = importlib.import_module(self.mock_plugin)
        self.assertEqual(module.__name__, self.mock_plugin)
        self.assertEqual(module.MockPlugin.__name__, 'MockPlugin')
        self.assertEqual(module.MockPlugin2.__name__, 'MockPlugin2')

        plugins = self.plugin_manager.discover_plugins(module)
        self.assertEqual(len(plugins), 2)
        self.assertEqual(set(plugins),
                         set([module.MockPlugin, module.MockPlugin2]))

    def test_plugins_can_be_registered(self):
        '''
            Test that plugins can be registered as expected
        '''
        self.plugin_manager.register_plugin(self.mock_plugin)
        self.assertEqual(self.plugin_manager.registered,
                         set(['MockPlugin', 'MockPlugin2']))
        self.assertTrue(
            'status_callback' in self.plugin_manager.callbacks.registered)

    def test_plugins_can_be_unregistered(self):
        '''
            Test that plugins are unregistered correctly and
        '''
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

        self.assertEqual(self.plugin_manager.MockPlugin, None)
        self.assertEqual(self.plugin_manager.callbacks.status_callback, None)
