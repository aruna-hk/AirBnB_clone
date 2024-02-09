import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model1 = BaseModel()
        self.my_model2 = BaseModel()

    def tearDown(self):
        pass

    def test_init(self):
       self.assertIsInstance(self.my_model1, BaseModel)
       self.assertTrue(hasattr(self.my_model1,'id'))
       self.assertTrue(hasattr(self.my_model1,'updated_at'))
       self.assertTrue(hasattr(self.my_model1,'created_at'))
       self.assertNotEqual(self.my_model1, self.my_model2)
       self.assertIsInstance(self.my_model1, BaseModel)
       self.assertIsInstance(self.my_model1.id, str)
       self.assertIsInstance(self.my_model1.created_at, datetime)
       self.assertIsInstance(self.my_model1.updated_at, datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.my_model1.id,self.my_model1.__dict__)
        self.assertEqual(str(self.my_model1), expected_str)

    def test_to_dict(self):
        result = self.my_model1.to_dict()
        self.assertIsInstance(result, dict)
        self.assertIn('id',result)
        self.assertIn('updated_at',result)
        self.assertIn('created_at',result)
        self.assertIn('__class__',result)
        self.assertEqual(result['__class__'], 'BaseModel')
        self.assertEqual(result['updated_at'], self.my_model1.updated_at.isoformat())
        self.assertEqual(result['created_at'], self.my_model1.created_at.isoformat())
        self.assertEqual(result['id'], self.my_model1.id)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b1 = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b1.id, "345")
        self.assertEqual(b1.created_at, dt)
        self.assertEqual(b1.updated_at, dt)

class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        """Check save models"""
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_one_save(self):
        b1 = BaseModel()
        sleep(0.05)
        first_updated_at = b1.updated_at
        b1.save()
        self.assertLess(first_updated_at, b1.updated_at)

    def test_two_saves(self):
        b1 = BaseModel()
        sleep(0.05)
        first_updated_at = b1.updated_at
        b1.save()
        second_updated_at = b1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        b1.save()
        self.assertLess(second_updated_at, b1.updated_at)

    def test_save_with_arg(self):
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.save(None)

