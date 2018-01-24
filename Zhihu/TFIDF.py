import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities

stop_words = 'C:\AndroidProject\Spider\stopwords.txt'
stopwords = codecs.open(stop_words, 'r', encoding='utf-8').readlines()
stopwords = [w.strip() for w in stopwords]
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']

# 对一篇文章进行分词、去停用词
def tokenization(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        words = pseg.cut(text)

    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

filenames = [
    'E:\BaiduNetdiskDownload\源码\第7周\盗墓笔记.txt',
    'E:\BaiduNetdiskDownload\源码\第7周\血尸.txt'
]

corpus = []
for file in filenames:
    corpus.append(tokenization(file))
# print(len(corpus))

# 建立词袋模型
dictionary = corpora.Dictionary(corpus)
doc_vec = [dictionary.doc2bow(text) for text in corpus]
print(doc_vec)

# 建立TF-IDF模型
tfidf = models.TfidfModel(doc_vec)
tfidf_vec = tfidf[doc_vec]
print(len(tfidf_vec[0]))

# 再构建一个query文本，是盗墓笔记主题
query = tokenization('E:\BaiduNetdiskDownload\源码\第7周\血尸.txt')
query_bow = dictionary.doc2bow(query)

index = similarities.MatrixSimilarity(tfidf_vec)

sims = index[query_bow]
print(list(enumerate(sims)))