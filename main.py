from db.reader import get_data
from db.analytic import EDA

data = get_data()

model = {"Frequency" :
             {'res' : 'ClaimNb',
              'w' : 'Exposure'},
        "Severity" :
            {'res' : 'ClaimAmount',
              'w' : 'ClaimNb'}}

for i in model.keys():
    E = EDA(data = data, res = model[i]['res'], w = model[i]['w'])
    result = E.response()
    print(result)
    print('done')
