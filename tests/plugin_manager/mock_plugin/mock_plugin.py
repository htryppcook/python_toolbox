
from python_toolbox.plugin_manager import Plugin
from python_toolbox.plugin_manager import CallbackProvider

class MockPlugin(Plugin):

  value = 0

  def __init__(self):
    super().__init__()

  def run(self):
    self.value += 1

  @CallbackProvider.callback
  def status_callback(self):
    please_continue = True
    while please_continue:
      please_continue = yield self.value
