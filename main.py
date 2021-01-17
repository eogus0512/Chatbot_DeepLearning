import pandas as pd

# 데이터 읽어오기
train_file = "total_train_data.xlsx"
data = pd.read_excel(train_file, sheet_name='Sheet1')
queries = data['query'].tolist()
intents = data['intent'].tolist()
print(data)

f = open("corpus.txt", 'w', encoding='utf-8')
for i in range(1, len(queries)):
    line = '0000\t{}\t{}\n'.format(queries[i], intents[i])
    print(line)
    f.write(line)
f.close()