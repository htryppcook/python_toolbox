
from python_toolbox.plugin_manager import Plugin
from python_toolbox.plugin_manager import CallbackProvider

class MockPlugin(Plugin):
    '''
        Simple MockPlugin increments a counter whenever the run method is
        called. The current count is discoverable by calling the registered
        callback function on CallbackProvider.
    '''
    value = 0

    def run(self):
        self.value += 1

    @CallbackProvider.callback
    def status_callback(self):
        '''
            Return the number of times run is executed. Stop tracking when
            passed in False.
        '''
        please_continue = True
        while please_continue:
            please_continue = yield self.value
