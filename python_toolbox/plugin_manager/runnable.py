
import abc

class Runnable(abc.ABC):
    '''
        Abstract base class providing one method, run.
    '''

    @abc.abstractmethod
    def run(self):
        """ Run method """
