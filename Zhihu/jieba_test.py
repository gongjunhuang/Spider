import jieba
import jieba.posseg as posseg
import jieba.analyse
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
from collections import Counter
from scipy.misc import imread


data = pd.read_csv('C:\\Users\\JOE\\Desktop\\wwxd.csv', encoding='utf-8')
def plot_distribution(data):
    index = np.arange(5)
    star_counts = data['Star'].value_counts()
    values = (star_counts[0], star_counts[1], star_counts[2], star_counts[3], star_counts[4])
    bar_width = 0.35
    plt.figure(figsize=(20,10))
    plt.bar(index, values, bar_width, alpha=0.6, color='rgbym')
    plt.xlabel('Star', fontsize=16)
    plt.ylabel('Counts', fontsize=16)
    plt.title('Comments level', fontsize=18)
    plt.xticks(index, ('5-star', '4-star', '3-star', '2-star', '1-star'), fontsize=14, rotation=20)
    plt.ylim(0, 200)
    for idx, value in zip(index, values):
        plt.text(idx, value + 0.1, '%d' % value, ha='center', va='bottom', fontsize=14, color='black')
    plt.show()

def segment_words(stars):
    comments = None
    if stars == 'all':
        comments = data['Comments']
    else:
        comments = data[data['Star'] == stars]['Comments']
    comments_list = []
    for comment in comments:
        comment = str(comment).strip().replace('span', '').replace('class', '').replace('emoji', '')
        comment = re.compile('1f\d+\w*|[<>/=]').sub('', comment)
        if len(comment) > 0:
            comments_list.append(comment)

    text = ''.join(comments_list)
    # word_list = list(jieba.cut(text))
    jieba.suggest_freq("无问西东", True)
    word_list = jieba.analyse.extract_tags(text, topK=50, withWeight=False, allowPOS=())
    print(word_list)
    c = Counter(word_list)
    print(c)
    common_c = c.most_common(50)
    print(common_c)
    #words = ''.join(word_list)

    return common_c

def plot_word_cloud(words):
    coloring = np.array(Image.open('C:\\Users\\JOE\\Desktop\\zzy.jpeg'))
    pic = imread('C:\\Users\\JOE\\Desktop\\jzm.jpg')
    wc = WordCloud(background_color='white', max_words=50, mask=pic, max_font_size=60, random_state=42
                   , font_path='C:\\Users\\JOE\\Downloads\\DroidSansFallbackFull.ttf', scale=2)
    #image_color = ImageColorGenerator(pic)
    wc.generate_from_frequencies(dict(words))

    plt.figure()
    #plt.imshow(wc.recolor(color_func=image_color))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('1.jpg')

if __name__ == '__main__':
    all_words = segment_words('all')
    print(all_words)
    plot_word_cloud(all_words)