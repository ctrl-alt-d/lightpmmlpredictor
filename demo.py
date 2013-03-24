'''
Created on Mar 24, 2013

@author: ctrl-alt-d
'''

from lightpredictor import utils

if __name__ == '__main__':
    
    values = {}
    values['nom_nivell'] = 'ESO'
    values['hora_inici'] = '09:15:00'
    values['assistenciaMateixaHora1WeekBefore'] = 'Present'
    values['assistenciaMateixaHora2WeekBefore'] = 'NA'
    values['assistenciaMateixaHora3WeekBefore'] = 'NA'
    values['assistenciaaHoraAnterior'] = 'Present'
    
    prediccio = utils.predict('pmml-models/dt.pmml', values)
    print prediccio

    values = {}
    values['nom_nivell'] = 'CFGM Infor'
    values['hora_inici'] = '11:30:00'
    values['assistenciaMateixaHora1WeekBefore'] = 'Absent'
    values['assistenciaMateixaHora2WeekBefore'] = 'Absent'
    values['assistenciaMateixaHora3WeekBefore'] = 'Absent'
    values['assistenciaaHoraAnterior'] = 'Absent'
        
    prediccio = utils.predict('pmml-models/dt.pmml', values)
    print prediccio
    