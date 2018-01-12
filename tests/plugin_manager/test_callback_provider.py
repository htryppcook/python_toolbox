
import unittest

from .mock_plugin import MockPlugin
from .mock_plugin import MockPlugin2

class TestCallbackProvider(unittest.TestCase):
    ''' tests for python_toolbox.plugin_manager.callback_provider '''
    def setUp(self):
        self.callback_provider = MockPlugin()

    def tearDown(self):
        pass

    def test_callbacks_are_callable(self):
        '''
            Test that we can call registered callbacks on.
        '''
        self.callback_provider.run()
        self.assertEqual(
            self.callback_provider.callbacks['status_callback'].send(True), 1)
        self.callback_provider.run()
        self.assertEqual(
            self.callback_provider.callbacks['status_callback'].send(True), 2)


    def test_callback_multi_registration(self):
        '''
            Test that callbacks are not registered multiple times.
        '''
        # pylint: disable=C0103
        self.callback_provider.run()
        self.assertEqual(
            self.callback_provider.callbacks['status_callback'].send(True), 1)

        callback_provider2 = MockPlugin()
        callback_provider2.value = 33
        callback_provider2.run()
        self.assertEqual(
            callback_provider2.callbacks['status_callback'].send(True), 34)

        mockplugin2 = MockPlugin2()
        mockplugin2.value = 100
        mockplugin2.run()
        self.assertEqual(
            mockplugin2.callbacks['status_callback'].send(True), 101)
        self.assertEqual(
            mockplugin2.callbacks['status_callback2'].send(True), 3)

        self.callback_provider.run()
        self.assertEqual(
            self.callback_provider.callbacks['status_callback'].send(True), 2)
