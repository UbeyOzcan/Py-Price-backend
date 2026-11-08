from db.reader import get_data
from db.analytic import EDA

data = get_data()


model = {"Frequency" :
             {'y' : 'ClaimNb',
              'offset' : 'Exposure'},
        "Severity" :
            {'y' : 'ClaimAmount',
              'offset' : 'ClaimNb'}}

for i in model.keys():
    E = EDA(data = data, y = model[i]['y'], offset = model[i]['offset'])
    result = E.response()
    print(result)
    print(E.univariate(var = ['VehGas', 'Area']))
