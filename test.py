import unittest
import function



class TestMultiplication(unittest.TestCase):

    def setUp(self):
        print('Начало тестов')
    

    def tearDown(self):
        print('Конец тестов')
    
    
    def test_number1(self):
        print('тест №1 Получение имени владельца документа')
        self.assertEqual(function.check_document_existance('11-2'), True)


    def test_number2(self):
        print('тест №2 Получение имени владельца документа')
        self.assertEqual(function.get_doc_owner_name('11-2'), 'Геннадий Покемонов')


    def test_number3(self):
        print('тест №3 Вывод имен всех владельцев документов')
        self.assertEqual(function.get_all_doc_owners_names(), {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})


    def test_number4(self):
        print('тест №4 Список всех документов')
        self.assertEqual(function.show_all_docs_info(), [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}, {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}, {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}])
    

    def test_number5(self):
        print('тест №5 Выводит полку , где находится документ')
        self.assertEqual(function.get_doc_shelf('11-2'), '1')


    def test_number6(self):
        print('тест №6 Добавления документа')
        self.assertEqual(function.add_new_doc('id','1111','Слободан','1'), {'type': 'id', 'number': '1111', 'name': 'Слободан'})

    def test_number7(self):
        print('тест №7 Удаление документа')
        self.assertEqual(function.delete_doc('11-2'), True)


if __name__ == '__main__':
    unittest.main()