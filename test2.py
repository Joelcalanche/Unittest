
import unittest
import main 


class TestMain(unittest.TestCase):
    # Esto  ejecuta un codigo antes de los test
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        # tiene que estar en la misma linea para mostrarse el comentario
        """ HIIII !!"""
        

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
    def tearDown(self):
        print("cleaning up")


# esta linea de codigo me permite ejecutar diferentes test files de un hit 
if __name__ == '__main__':


        


# los asertionError vienen del test hay que corregir algo
# esto ejecuta todos los test
# ojo este main no tiene nda que ver con el main.py
    unittest.main()





# python -m unittest para correr todos los test de una
# podemos agregarle  -v (verbose) para hacer el desgloce de cada test
# Puedo agregar comentarios a los unit test





