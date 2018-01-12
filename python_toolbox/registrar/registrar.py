
from ..utilities import isnamed

class UnregisteredItemException(Exception):
    '''
        Exception thrown when trying to call an item that has been previously
        unregistered.
    '''
    pass

class Registrar:
    '''
      Usage examples:
      >>> from python_toolbox.registrar import Registrar
      >>> registrar = Registrar()

      >>> registrar.register(my_coroutine_a)
      True
      >>> registrar.register(my_coroutine_b, 'my_special_coroutine')
      True
      >>> registrar.my_coroutine_a()
      'did some stuff'
      >>> registrar.my_special_coroutine()
      'did some other stuff'

      >>> registrar.unregister('my_coroutine_a')
      >>> registrar.my_coroutine_a()
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      UnregisteredItemException

      >>> registrar.register(my_coroutine_b, 'my_special_coroutine')
      False
    '''
    def __init__(self):
        self.registered = set()
        self.unregister_format_string = \
          '{} was previously unregistered and is no longer available!'

    def register(self, item, name=None):
        '''
            Register an item with this Registrar instance. Name is a required
            parameter if item.__name__ doesn't exist.
        '''
        if name is None:
            if isnamed(item):
                name = item.__name__
            else:
                # Cowardly refuse
                return False

        if name in self.__dict__:
            return False

        self.__setattr__(name, item)
        self.registered.add(name)
        return True

    # Cannot raise from a lambda so we have to build a function to do it for us.
    def build_unregistered(self, name):
        ''' Build a function to replace unregistered callables. '''
        def unregistered(*args, **kwargs):
            ''' Function that replaces an unregistered callable. '''
            # pylint: disable=unused-argument
            raise UnregisteredItemException(
                self.unregister_format_string.format(name))
        return unregistered

    def unregister(self, name):
        ''' Unregister an item by name. '''
        if name in self.registered:
            if callable(self.__dict__[name]):
                self.__setattr__(name, self.build_unregistered(name))
            else:
                self.__setattr__(name, None)

            self.registered.remove(name)
            return True

        return False
