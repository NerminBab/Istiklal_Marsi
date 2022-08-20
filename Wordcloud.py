"""
İstiklal Marşımızın kelimelerinin Wordcloud çalışmasıdır.
"""

from matplotlib import pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.tokenize import word_tokenize

data = "Korkma, sönmez bu şafaklarda yüzen al sancak;Sönmeden yurdumun üstünde tüten en son ocak.O benim milletimin yıldızıdır, parlayacak;O benimdir, o benim milletimindir ancak.Çatma, kurban olayım çehreni ey nazlı hilâl!Kahraman ırkıma bir gül… ne bu şiddet bu celâl?Sana olmaz dökülen kanlarımız sonra helâl,Hakkıdır, Hakk’a tapan, milletimin istiklâl.Ben ezelden beridir hür yaşadım, hür yaşarım.Hangi çılgın bana zincir vuracakmış? Şaşarım!Kükremiş sel gibiyim; bendimi çiğner, aşarım;Yırtarım dağları, enginlere sığmam, taşarım.Garb’ın âfâkını sarmışsa çelik zırhlı duvar;Benim iman dolu göğsüm gibi serhaddim var.Ulusun, korkma! Nasıl böyle bir îmânı boğar,"


def data_processing(data):
    data = data.lower()
    data_tokens = word_tokenize(data)
    processed_words = [k for k in data_tokens]
    return " ".join(processed_words)


data_processed = data_processing(data)

plt.figure(figsize=(10, 10), facecolor='none')
wordcloud = WordCloud().generate(data_processed)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
