# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from trytond.report import Report
from datetime import date


class AcademicCalendaryActiviteReport(Report):
    __name__ = 'akademy_classe_evaluation.academic.calendary.activite.report'

    @classmethod
    def get_context(cls, records, header, data):
        AcademicCalendary = Pool().get('akademy_classe_evaluation.academic.calendary')

        context = super().get_context(records, header, data)
        academic_calendary = AcademicCalendary.browse(data['ids'])

        context['academic_calendary'] = academic_calendary
        context['create_date'] = date.today()

        return context


class AcademicCalendaryAvaliationReport(Report):
    __name__ = 'akademy_classe_evaluation.academic.calendary.avaliation.report'

    @classmethod
    def get_context(cls, records, header, data):
        AcademicCalendary = Pool().get('akademy_classe_evaluation.academic.calendary')

        context = super().get_context(records, header, data)
        academic_calendary = AcademicCalendary.browse(data['ids'])

        context['academic_calendary'] = academic_calendary
        context['create_date'] = date.today()

        return context
	

class ClassesEvaluationReport(Report):
	__name__ ='akademy_classe_evaluation.classes.evaluation.report'

	@classmethod
	def get_context(cls, records, header, data):
		ClassesEvaluation = Pool().get('akademy_classe_evaluation.classes.evaluation')
		context = super().get_context(records, header, data)
		classes_evaluations = ClassesEvaluation.browse(data['ids'])
		
		context['classes_evaluations'] = classes_evaluations
		context['create_date'] = date.today()

		return context
