import json
purchases = {}
file = open('purchase_log.txt', encoding='utf-8')
file.readline()
for line in file:
    param = json.loads(line)
    purchases.update({param['user_id']: param['category']})

file2 = open('funnel.csv', 'w', encoding='cp1251')
file1 = open('visit_log.csv', encoding='utf-8')
for line in file1:
    if line.split(',')[0] in purchases:
        file2.write((line.strip() + ',' + purchases[line.split(',')[0]] + '\n'))