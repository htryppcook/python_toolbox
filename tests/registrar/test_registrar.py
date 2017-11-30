import unittest

from python_toolbox.registrar import Registrar
from python_toolbox.registrar import UnregisteredItemException

class TestRegistrar(unittest.TestCase):
  
  def setUp(self):
    self.registrar = Registrar()

    def sample_callback(x, max_range=5):
      for _ in range(max_range):
        yield x

    self.sample_callback = sample_callback

  def tearDown(self):
    pass

  def test_callable_items_can_be_registered(self):
    callback_name = self.sample_callback.__name__
    result = self.registrar.register(self.sample_callback)
    self.assertTrue(result)

    # Shows up in registered as expected
    self.assertTrue(
      callback_name in self.registrar.registered)

    # Actually exists in registrar's dict
    self.assertTrue(callback_name in self.registrar.__dict__)

    # The correct callback was registered
    self.assertTrue(
      self.sample_callback == self.registrar.__dict__[callback_name])


  def test_items_can_be_registered_with_alternative_names(self):
    alt_name = 'alternate_name'
    result = \
      self.registrar.register(self.sample_callback, alt_name)
    self.assertTrue(result)

    # Shows up in registered with the correct name
    self.assertTrue(alt_name in self.registrar.registered)

    # Actually exists in registrar's dict with the correct name
    self.assertTrue(alt_name in self.registrar.__dict__)

    # The correct callback was registered
    self.assertTrue(
      self.sample_callback == self.registrar.__dict__[alt_name])

  def test_items_without_names_cannot_be_registered(self):
    self.assertFalse(self.registrar.register(32))

  def test_registering_an_existing_item_returns_false(self):
    # setup
    self.assertTrue(
      self.registrar.register(self.sample_callback))

    # Ensure registering an existing callback returns False
    self.assertFalse(
      self.registrar.register(self.sample_callback))

  def test_removing_nonexistent_item_returns_false(self):
    self.assertFalse(self.registrar.unregister('sample_callback'))

  def test_items_can_be_removed(self):
    self.registrar.register(self.sample_callback)
    self.assertTrue(self.registrar.unregister('sample_callback'))

  def test_cannot_delete_misc_items_from_dict(self):
    msg = "don't delete me"
    self.registrar.misc = msg
    self.assertFalse(self.registrar.unregister('misc'))

  def test_unregistered_items_are_none(self):
    msg = 'msg'
    self.assertTrue(self.registrar.register(msg, name=msg))
    self.assertTrue(self.registrar.unregister(msg))
    self.assertEquals(self.registrar.msg, None)

  def test_unregistered_callable_items_throw_an_exception(self):
    self.assertTrue(self.registrar.register(self.sample_callback))
    self.assertTrue(self.registrar.unregister('sample_callback'))

    try:
      self.registrar.sample_callback()
    except UnregisteredItemException as e:
      self.assertEquals(str(e), 'sample_callback was previously unregistered '
        + 'and is no longer available!')
