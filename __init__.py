# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import calendary
from . import employee
from . import classe
from . import report

def register():
    Pool.register(
        calendary.LectiveYear,
        calendary.AcademicCalendary,
        calendary.AcademicCalendaryActivite,
        calendary.AcademicCalendaryAvaliation,
        classe.ClassesEvaluationCreateWizardStart,
        employee.Employee,

        module='akademy_classe_evaluation', type_='model'
    )
    
    Pool.register(
        classe.ClassesEvaluationCreateWizard,

        module='akademy_classe_evaluation', type_='wizard'
    )

    Pool.register(
        report.AcademicCalendaryActiviteReport,
        report.AcademicCalendaryAvaliationReport,
        report.ClassesEvaluationReport,

        module='akademy_classe_evaluation', type_='report'
    )

