
import abc

from .runnable import Runnable
from .callback_provider import CallbackProvider

class Plugin(Runnable, CallbackProvider, abc.ABC):
    '''
        Abstract base class created by combining plugin_manager.Runnable with
        plugin_manager.CallbackProvider.
    '''
    # pylint: disable=W0223,
    pass
