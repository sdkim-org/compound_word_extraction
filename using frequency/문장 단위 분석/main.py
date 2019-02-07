from nltk import *

# line 단위의 sentence를 입력받아 빈도 분포 객체를 반환한다.
# @param sentence: 빈도 분포를 분석할 문장
# @param numTokens: 빈도 분포를 생성할 기준 토큰 수
def getFreqDist(sentence, numTokens):
    tokenList = word_tokenize(sentence)
    ngramList = ngrams(tokenList, numTokens)

    return FreqDist(ngramList)


# 빈도 분포를 생성할 기준 토큰 수
NUM_TOKENS = 3

# 출력할 빈도 분포의 임계값.
# 이 값보다 적은 수의 빈도를 가지는 분포는 출력되지 않는다.
FREQ_THRESHOLD = 5

# 텍스트 파일 열기
file = open("sample.txt", 'r', encoding='UTF8')

# 텍스트 파일을 라인 별로 분할하여 리스트로 저장
sentences = file.readlines()

# sentences의 모든 빈도 분포를 분석한 결과가 저장된다.
# 이 객체는 Map 객체이며, key는 복합어, value는 빈도 수이다.
globalFreqDist = {}

# sentences 내에 있는 모든 sentence에 대하여
for sentence in sentences:
    # 현재 sentence에 대한 빈도 분포 분석
    localDist = getFreqDist(sentence, NUM_TOKENS)

    # localDist에 존재하는 빈도 분포를 조사
    # key: 복합어 / value: 빈도 수
    for key, value in localDist.items():

        # 만약 globalFreqDist에 이미 존재하는 복합어라면
        if key in globalFreqDist:
            # 해당 복합어의 빈도 수에 value를 누적
            globalFreqDist[key] = globalFreqDist[key] + value
        # 처음 나타난 복합어라면
        else:
            # globalFreqDist 맵에 새로 추가
            globalFreqDist[key] = value

# globalFreqDist 내의 모든 key에 대해
for key in globalFreqDist:
    # value 값 얻기
    value = globalFreqDist[key]

    # value 값이 임계값보다 큰 경우만
    if value >= FREQ_THRESHOLD:
        # 출력
        print(key, value)
