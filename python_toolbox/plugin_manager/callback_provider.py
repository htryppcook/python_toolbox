
from functools import wraps

class CallbackProvider:

  callbacks = {}

  def __init__(self):
    super().__init__()
    self.initialize_callbacks()

  def initialize_callbacks(self):
    for callback in self.callbacks.keys():
      gen = getattr(self, callback)()
      gen.send(None)
      self.callbacks[callback] = gen

  @classmethod
  def callback(cls, func):
    cls.callbacks[func.__name__] = None
    return func
