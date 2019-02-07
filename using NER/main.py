import nltk
import os
from nltk.tag.stanford import StanfordNERTagger

# 환경 변수 설정
os.environ['JAVAHOME'] = "C:/Program Files/Java/jre1.8.0_191/bin/java.exe"

# 텍스트 파일 경로
textPath = 'sample.txt'

# ner 파일 경로
nerPath = 'stanford-ner-3.9.2.jar'

# model 경로
modelPath = 'english.all.3class.distsim.crf.ser'

# 추출할 NER 타입 (ORGANIZATION, PERSON, LOCATION, ...)
nerType = 'ORGANIZATION'

# NER Tagger 객체 생성
nerTagger = StanfordNERTagger(modelPath, nerPath, encoding='UTF8')

# 텍스트 파일 로드
file = open(textPath, 'r', encoding='UTF8')
sentence = file.readlines()

# 텍스트의 각 라인에 대하여
for line in sentence:
    # 단어(토큰) 단위로 분할
    words = nltk.word_tokenize(line)

    # 분할한 단어들에 Tagging
    tags = nerTagger.tag(words)

    # Tagged 된 단어들 중
    for tag in tags:

        # 현재 설정한 nerType과 동일한 단어만 출력
        if tag[1] == nerType:
            print(tag)
