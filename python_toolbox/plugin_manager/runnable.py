
import abc

class Runnable(abc.ABC):

  def __init__(self):
    super().__init__()

  @abc.abstractmethod
  def run(self):
    """ Run method """
