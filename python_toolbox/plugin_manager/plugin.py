
import abc

from .runnable import Runnable
from .callback_provider import CallbackProvider

class Plugin(Runnable, CallbackProvider, abc.ABC):

  def __init__(self):
    super().__init__()
