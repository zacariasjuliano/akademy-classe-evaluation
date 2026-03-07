# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields, Unique, Check
from trytond.pool import PoolMeta
from datetime import date, datetime


class LectiveYear(metaclass=PoolMeta):
    'Lective Year'
    __name__ ='akademy_configuration.lective.year'

    academic_calendars = fields.One2Many('akademy_classe_evaluation.academic.calendary', 
        'lective_year', 'Calendário académico')


class AcademicCalendary(ModelSQL, ModelView):
    'Academic Caldendary'
    __name__ = 'akademy_classe_evaluation.academic.calendary'

    code = fields.Char('Código', size=20,
        help="Código do ano calendário.\nEx: 25/26")
    name = fields.Char('Nome', required=True, 
        help="Nome do calendário.")     
    start = fields.Date('Início', required=True, 
        help="Data de início do calendário.")
    end = fields.Date('Fim', required=True,
        help="Data de fim de calendário.")
    description = fields.Text('Descrição')
    lective_year = fields.Many2One('akademy_configuration.lective.year', 
        'Ano letivo', required=True, ondelete="RESTRICT")    
    calendary_activites = fields.One2Many('akademy_classe_evaluation.academic.calendary.activite', 
        'academic_calendary', 'Atividades')
    calendary_avaliations = fields.One2Many('akademy_classe_evaluation.academic.calendary.avaliation', 
        'academic_calendary', 'Avaliações')
    
    @classmethod
    def __setup__(cls):
        super(AcademicCalendary, cls).__setup__()
        table = cls.__table__()
        cls._sql_constraints = [            
            ('date', Check(table, table.start < table.end),
            u'Não foi possível criar o calendário, por favor verificar se a data de início é menor que a data de término.')
        ]
        cls._order = [('start', 'ASC')]	 

    @classmethod
    def default_start(cls):
        return datetime.now().date()


class AcademicCalendaryActivite(ModelSQL, ModelView):
    'Academic Caldendary Activite'
    __name__ = 'akademy_classe_evaluation.academic.calendary.activite'

    code = fields.Char('Código', size=20,
        help="Código da atividade do calendário.\nEx: 25/26")
    name = fields.Char('Nome', required=True, 
        help="Nome da atividade do calendário.")     
    start = fields.Date('Início', required=True, 
        help="Data de início da atividade do calendário.")
    end = fields.Date('Fim', required=True,
        help="Data de fim da atividade do calendário.")
    description = fields.Text('Descrição')
    academic_calendary = fields.Many2One('akademy_classe_evaluation.academic.calendary', 'Calendário',
        required=True, ondelete="RESTRICT")
    quarter = fields.Many2One('akademy_configuration.quarter', 'Período letivo', 
        required=True, ondelete="RESTRICT", help="Escolha o período letivo para atividade.")
    
    @classmethod
    def __setup__(cls):
        super(AcademicCalendaryActivite, cls).__setup__()
        table = cls.__table__()
        cls._sql_constraints = [            
            ('date', Check(table, table.start < table.end),
            u'Não foi possível criar a atividade para calendário, por favor verificar se a data de início é menor que a data de término.')
        ]
        cls._order = [('start', 'ASC')]	 

    @classmethod
    def default_start(cls):
        return datetime.now().date()


class AcademicCalendaryAvaliation(ModelSQL, ModelView):
    'Academic Caldendary Avaliation'
    __name__ = 'akademy_classe_evaluation.academic.calendary.avaliation'

    code = fields.Char('Código', size=20,
        help="Código da avaliação do calendário.\nEx: 25/26")
    name = fields.Char('Nome', required=True, 
        help="Nome da avaliação do calendário.")     
    start = fields.Date('Início', required=True, 
        help="Data de início da avaliação do calendário.")
    end = fields.Date('Fim', required=True,
        help="Data de fim da avaliação do calendário.")
    description = fields.Text('Descrição')
    academic_calendary = fields.Many2One('akademy_classe_evaluation.academic.calendary', 'Calendário',
        required=True, ondelete="RESTRICT")
    quarter = fields.Many2One('akademy_configuration.quarter', 'Período letivo', 
        required=True, ondelete="RESTRICT", help="Escolha o período letivo para avaliação.")
    metric_avaliation = fields.Many2One('akademy_configuration.metric.avaliation', 'Avaliação',        
        required=True, help="Nome da avaliação.", ondelete="RESTRICT")
    
    @classmethod
    def __setup__(cls):
        super(AcademicCalendaryAvaliation, cls).__setup__()
        table = cls.__table__()
        cls._sql_constraints = [            
            ('date', Check(table, table.start < table.end),
            u'Não foi possível criar o calendário, por favor verificar se a data de início é menor que a data de término.')
        ]	
        cls._order = [('start', 'ASC')] 

    @classmethod
    def default_start(cls):
        return datetime.now().date()
