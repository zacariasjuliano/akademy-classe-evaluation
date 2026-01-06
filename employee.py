# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import PoolMeta


class Employee(metaclass=PoolMeta):
    'Employee'
    __name__ = 'company.employee'
       
    institution_help = fields.Boolean(
        'Vigilante', 
        help="A entidade será tratada como vigilante da instituição.")       
    institution_support = fields.Boolean(
        'Auxiliar', 
        help="A entidade será tratada como auxiliar da instituição.")
