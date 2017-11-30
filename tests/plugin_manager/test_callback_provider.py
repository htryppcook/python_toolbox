
import unittest

from .mock_plugin import MockPlugin

class TestCallbackProvider(unittest.TestCase):
  def setUp(self):
    self.callback_provider = MockPlugin()

  def tearDown(self):
    pass

  def test_callbacks_are_callable(self):
    self.callback_provider.run()
    self.assertEquals(
      self.callback_provider.callbacks['status_callback'].send(True), 1)
    self.callback_provider.run()
    self.assertEquals(
      self.callback_provider.callbacks['status_callback'].send(True), 2)
