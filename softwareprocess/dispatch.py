import softwareprocess.operations.adjust as adjust
import softwareprocess.operations.correct as correct
import softwareprocess.operations.locate as locate
import softwareprocess.operations.predict as predict

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        return adjust.adjust(values)    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return predict.predict(values)    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return correct.correct(values)    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return locate.locate(values)    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
