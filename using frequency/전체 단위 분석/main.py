from nltk import *

# 토큰 길이에 따른 빈도 수 분석 class
class FrequencyExtractor:

    # 추출할 복합어의 토큰 길이
    numTokens = 1

    # 추출할 복합어의 최소 빈도수
    freqThreshold = 1

    # 추출된 단위 토큰 (내부 변수)
    __tokenList = ''

    # 텍스트 파일을 읽은 뒤 단위 토큰을 로드하는 함수
    # textPath: 텍스트 파일 경로
    def load(self, textPath):
        # 파일 열기
        file = open(textPath, 'r', encoding='UTF8')

        # 텍스트 파일 읽기
        text = file.read()

        # 텍스트 파일을 토큰 리스트로 파싱
        self.__tokenList = word_tokenize(text)

    # 추출할 복합어의 토큰 길이를 설정하는 함수
    # numTokens: 추출할 복합어의 토큰 길이
    def setNumTokens(self, numTokens):
        self.numTokens = numTokens

    # 추출할 복합어의 최소 빈도수를 설정하는 함수
    # threshold: 추출할 복합어의 최소 빈도수
    def setFreqThreshold(self, threshold):
        self.freqThreshold = threshold

    # 설정되어 있는 토큰 길이 및 최소 빈도수를 기반으로 빈도 분포 맵을 반환한다.
    def getFreqDistribution(self):
        # ngram은 하나의 복합어를 의미한다.
        # 추출한 token list와, 설정된 토큰 길이 값을 기반으로 ngram list를 생성한다.
        ngramList = ngrams(self.__tokenList, self.numTokens)

        # 추출한 ngram list로부터 복합어 빈도수를 얻는다.
        # fdist는 복합어와 빈도수로 구성된 Map이다.
        fdist = FreqDist(ngramList)

        # 반환할 빈도 분포 맵은 fdist의 Map entry 중
        # 최소 빈도수를 만족하는 entry만 담기게 된다.
        retVal = {}

        # fdist의 모든 entry를 조사한다.
        for key, value in fdist.items():

            # 만약 빈도수가 최소 빈도수보다 크다면 반환할 빈도 분포 맵에 담는다.
            if value >= self.freqThreshold:
                retVal[key] = value

        return retVal


extractor = FrequencyExtractor()
extractor.load("sample.txt")
extractor.setNumTokens(3)
extractor.setFreqThreshold(5)

result = extractor.getFreqDistribution()

for key in result:
    print(key, result[key])

print("\ntotal length: " + str(len(result)))
