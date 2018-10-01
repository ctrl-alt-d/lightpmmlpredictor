lightpmmlpredictor
==================

Light python module for predictions trhough pmml

Sample:

    from lightpredictor import utils

    values = {}
    values['level'] = 'high'
    values['start_time'] = '09:15:00'
    values['need_refrigeration'] = 'Yes'
    values['has_milk'] = 'N/A'

    must_to_check = utils.predict('pmml-models/my-model.pmml', values)
    
    ### ToDo:
    
    * Migrate to Python3.
    * Check PMML versions.
