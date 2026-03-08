from trytond.tests.test_tryton import ModuleTestCase, with_transaction

class EmployeeTestCase(ModuleTestCase):
    "Employee Test Case"
    module = 'akademy_classe_evaluation'

    @with_transaction()
    def test_method(self):
        "Test method"
        self.assertTrue(True)

del ModuleTestCase
