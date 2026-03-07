# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import fields, ModelSQL, ModelView
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.pool import PoolMeta, Pool
from trytond.pyson import Eval, Not


class ClassesEvaluationCreateWizardStart(ModelView):
    'ClassesStateCreate State'
    __name__ = 'akademy_classe.wizclassesevaluation.create.start'
    
    lective_year = fields.Many2One('akademy_configuration.lective.year', 'Ano letivo',
        required=True, help="Informa o nome do ano letivo.")


class ClassesEvaluationCreateWizard(Wizard):
    'ClassesState Create'
    __name__ = 'akademy_classe.wizclassesevaluation.create'

    start_state = 'start'
    start = StateView(
        'akademy_classe.wizclassesevaluation.create.start',
        'akademy_classe_evaluation.act_classesevaluation_wizard_from', [
            Button(string=u'Cancelar', state='end', icon='tryton-cancel'),
            Button(string=u'Processar', state='classes_evaluation', icon='tryton-save')
        ]
    )

    classes_evaluation = StateTransition()

    def transition_classes_evaluation(self):
        ClassesEvaluationCreateWizard.generate_lective_year_report(self.start.lective_year)

        return 'end'
    
    @classmethod
    def generate_lective_year_report(cls, lective_year):
        ClassesEvaluation = Pool().get('akademy_classe.classes.evaluation')
        classes_evaluations = ClassesEvaluation.search([('lective_year', '=', lective_year)])
        Student = Pool().get('company.student')
        ClasseStudent = Pool().get('akademy_classe.classe.student')
        ClasseStudentDiscipline = Pool().get('akademy_classe.classe.student.discipline')

        student_matriculation_approveds = 0
        student_matriculation_repproveds = 0
        student_matriculation_others = 0

        student_gender_males = 0
        student_gender_females = 0
        student_gender_others = 0
        teacher_gender_males = 0
        teacher_gender_females = 0
        teacher_gender_others = 0
        lective_years = 0
                        
        for classe in lective_year.classes:
            if classe.state == False:
                for classe_student in classe.classe_student:
                    student_matriculation_approveds = 0
                    student_matriculation_repproveds = 0
                    student_matriculation_others = 0
                   
                    if classe_student.student.party.gender == 'masculino':
                        student_gender_males += 1
                    elif classe_student.student.party.gender == 'feminino':
                        student_gender_females += 1
                    else:
                        student_gender_others += 1                            

                for classe_teacher in classe.classe_teacher:
                    if classe_teacher.employee.party.gender == 'masculino':
                        teacher_gender_males += 1
                    elif classe_teacher.employee.party.gender == 'feminino':
                        teacher_gender_females += 1
                    else:
                        teacher_gender_others += 1                

                if len(classes_evaluations) <= 0:                        
                    classes_evaluation_report = ClassesEvaluation(
                        name = lective_year.name,
                        lective_year = lective_year,
                        student_gender_male = student_gender_males,
                        student_gender_female = student_gender_females,
                        student_gender_other = student_gender_others,
                        teacher_gender_male = teacher_gender_males,
                        teacher_gender_female = teacher_gender_females,
                        teacher_gender_other = teacher_gender_others,
                        #student_matriculation_approved = student_matriculation_approveds,
                        #student_matriculation_repproved = student_matriculation_repproveds,
                        #student_matriculation_other = student_matriculation_others,
                        classes = classe
                    )

                    classes_evaluation_report.save()

                classe.state = True
                classe.save()


class ClassesEvaluation(ModelSQL):
    'Classes Evaluation Report'
    __name__ = 'akademy_classe.classes.evaluation'
	  
    name = fields.Char('Nome', help="Nome Exe:Estado da Matrícula.")
    student_gender_male = fields.Integer('Masculino') 
    student_gender_female = fields.Integer('Femenino')
    student_gender_other = fields.Integer('Outros gêneros')    
    teacher_gender_male = fields.Integer('Masculino') 
    teacher_gender_female = fields.Integer('Femenino')
    teacher_gender_other = fields.Integer('Outros gêneros')
    #student_matriculation_approved = fields.Integer('Aprovados')
    #student_matriculation_repproved = fields.Integer('Reprovados')
    #student_matriculation_other = fields.Integer('Outros estados')
    lective_year = fields.Many2One('akademy_configuration.lective.year', 
        'Ano letivo', required=True, ondelete="RESTRICT")
    classes = fields.Many2One('akademy_classe.classes', 
        'Turmas', ondelete="RESTRICT")