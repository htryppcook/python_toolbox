
from python_toolbox.plugin_manager import Plugin
from python_toolbox.plugin_manager import CallbackProvider

class MockPlugin2(Plugin):
    '''
        MockPlugin2 looks just like MockPlugin, but registers another callback,
        status_callback2.
    '''
    value = 0
    value2 = 0

    def run(self):
        self.value += 1
        self.value2 += 3

    @CallbackProvider.callback
    def status_callback(self):
        '''
            Return the number of times run is executed. Stop tracking when
            passed in False.
        '''
        please_continue = True
        while please_continue:
            please_continue = yield self.value

    @CallbackProvider.callback
    def status_callback2(self):
        '''
            Return value2. Stop tracking when passed in False
        '''
        please_continue = True
        while please_continue:
            please_continue = yield self.value2
