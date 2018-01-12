
class CallbackProvider:
    '''
        The CallbackProvider class provides a way to register generator methods
        on a chosen class as callbacks. These callbacks can then be called
        without access to the originating instance.
    '''
    callbacks = dict()

    def __init__(self):
        super().__init__()
        self.callbacks = dict(self.callbacks)
        self.initialize_callbacks()

    def initialize_callbacks(self):
        '''
            Iterate through the list of registered callbacks for this instance,
            priming each using None as a starting value.
        '''
        # pylint: disable=C0201
        for callback in self.callbacks.keys():
            if callback and hasattr(self, callback):
                gen = getattr(self, callback)()
                gen.send(None)
                self.callbacks[callback] = gen

    @classmethod
    def callback(cls, func):
        '''
            Decorator method used to register a method on your class as a
            callback. Callbacks should be generator functions that can
            optionally return a value using yield.

            -- Example:
            from python_toolbox.plugin_manager import CallbackProvider

            @CallbackProvider.callback
            def status_callback(self):
                """ Loops """
                please_continue = True

                while please_continue:
                    please_continue = yield self.value
        '''
        cls.callbacks[func.__name__] = None
        return func
