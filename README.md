# Chatbot_Project
동국대학교 주변 맛집을 추천해주는 딥러닝 챗봇 개발 프로젝트

파일구성
Chatbot_Project
ㄴconfig(챗봇 개발에 필요한 설정)
  ㄴDatabaseCongfig
  ㄴGlobalParams
ㄴmodels(챗봇 엔징에서 사용하는 딥러닝 모델 관련 파일)
  ㄴintents(의도 분류 모델 관련 파일)
  ㄴner(개체 인식 모델 관련 파일)
  ㄴtest
ㄴtest(챗봇 개발에 필요한 테스트 코드)
  ㄴchatbot_client_test
  ㄴchatbot_data
  ㄴchatbot_dict_test
  ㄴchatbot_test
  ㄴmodel_intent_test
  ㄴmodel_ner_test
  ㄴpreprocess_test
ㄴtrain_tools(챗봇 학습툴 관련 파일)
  ㄴdict
    ㄴchatbot_dict.bin(단어사전)
    ㄴcorpus.txt(
    ㄴcreate_dict
    ㄴload_dict_test
  ㄴqna
    ㄴcreate_train_data_table
    ㄴload_train_data
    ㄴtrain_data
ㄴutils(챗봇 개발에 필요한 유틸리티 라이브러리)
  ㄴBotServer
  ㄴDatabase
  ㄴFindAnswer
  ㄴPreprocess
  ㄴuser_dict.tsv
