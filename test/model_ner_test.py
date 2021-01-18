from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')


ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
query = '에 부대찌개 먹고싶어'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)

