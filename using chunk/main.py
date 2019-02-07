import nltk

# 로컬로부터 파일을 연다
file = open('sample.txt', 'r', encoding='UTF8')

# 텍스트를 읽음
rawContents = file.readline()

# 파일 닫기
file.close()

# 컨텐츠 내에 있는 모든 단어들을 공백 문자열 기준으로 Tokenizing
rawTokens = nltk.word_tokenize(rawContents)

# Part of Speech(POS) tagging
# rawTokens(list)내에 저장된 모든 Token들을 POS 별로 매핑
taggedTokens = nltk.pos_tag(rawTokens)

# Chunk 정규식 정의
# Chunk 정규식은 절대적인 기준이 없으며, 개발자가 직접 원문의 내용을 분석하고
# 상황에 따라 별도로 정의해주어야 한다.
regexes = """
    NP: {<DT|PP\$>?<JJ>*<NN.*>+} # noun phrase
    PP: {<IN><NP>}               # prepositional phrase
    VP: {<MD>?<VB.*><NP|PP>}     # verb phrase
"""

# 파서 생성
parser = nltk.RegexpParser(regexes)

# 파싱
parsedTree = parser.parse(taggedTokens)

for subtree in parsedTree:
    if isinstance(subtree, nltk.tree.Tree) and subtree.label() == "NP":
        print(subtree)




