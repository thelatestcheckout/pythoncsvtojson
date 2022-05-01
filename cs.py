import csv
import json
from time import process_time

from outputData import outputData


def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            id = rows.get('#id')
            argumentative = rows.get('argumentative').split()[0]
            quality = rows.get('overall quality')
            if not quality == '':
                quality = quality.split()[0]
            effectiveness = rows.get('effectiveness')
            if not effectiveness == '':
                effectiveness = effectiveness.split()[0]
            if not (any(x.get('id') == id for x in data)):
                issue = rows.get('issue')
                stance = rows.get('stance')
                argument = rows.get('argument')
                od = outputData(id, issue, stance, argument)
                od.setArgumentative(argumentative)
                od.setQuality(quality)
                od.setEffectiveness(effectiveness)
                data.append(od.__dict__)
            else:
                for index, item in enumerate(data):
                    if item.get('id') == id:
                        data[index].get('argumentative').append(argumentative)
                        data[index].get('quality').append(quality)
                        data[index].get('effectiveness').append(effectiveness)
                        break
                    else:
                        index = -1

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


csvFilePath = r'input.csv'
jsonFilePath = r'Output.json'

make_json(csvFilePath, jsonFilePath)
