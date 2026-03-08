from trytond.tests.test_tryton import ModuleTestCase, with_transaction

class ClasseTestCase(ModuleTestCase):
    "Classe Test Case"
    module = 'akademy_classe_evaluation'

    @with_transaction()
    def test_method(self):
        "Test method"
        self.assertTrue(True)

del ModuleTestCase
