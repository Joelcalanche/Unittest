
import unittest
import main 


class TestMain(unittest.TestCase):

    def test_do_stuff(self):

        test_param = 10

        result = main.do_stuff(test_param)

       # lo que me devulve la funcion que estoy probando, el resultado
        # isintance pregunta si algo es intancia de otra clase(hijo, padre)
        self.assertEqual(result, 15)


    def test_do_stuff_2(self):

        test_param = "dadsad"
        result = main.do_stuff(test_param)
        # isintance pregunta si algo es intancia de otra clase(hijo, padre)
        
        # self.assertTrue(isinstance(result, ValueError))
        
        self.assertIsInstance(result, ValueError)


    def test_do_stuff3(self):
        test_param = None
        
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


    def test_do_stuff4(self):
        test_param = ''
        
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')



if __name__ == '__main__':


        


# los asertionError vienen del test hay que corregir algo
# esto ejecuta todos los test
# ojo este main no tiene nda que ver con el main.py
    unittest.main()





# python -m unittest para correr todos los test de una


