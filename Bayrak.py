"""
Bayrağımız üzerine İstiklal Marşımızın işlenmesidir.
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud


data = "Korkma, sönmez bu şafaklarda yüzen al sancak;Sönmeden yurdumun üstünde tüten en son ocak.O benim milletimin yıldızıdır, parlayacak;O benimdir, o benim milletimindir ancak.Çatma, kurban olayım çehreni ey nazlı hilâl!Kahraman ırkıma bir gül… ne bu şiddet bu celâl?Sana olmaz dökülen kanlarımız sonra helâl,Hakkıdır, Hakk’a tapan, milletimin istiklâl.Ben ezelden beridir hür yaşadım, hür yaşarım.Hangi çılgın bana zincir vuracakmış? Şaşarım!Kükremiş sel gibiyim; bendimi çiğner, aşarım;Yırtarım dağları, enginlere sığmam, taşarım.Garb’ın âfâkını sarmışsa çelik zırhlı duvar;Benim iman dolu göğsüm gibi serhaddim var.Ulusun, korkma! Nasıl böyle bir îmânı boğar,"

byrk_mask = np.array(Image.open("turkey.png"))

bayrak = WordCloud(mask=byrk_mask,background_color="white", contour_color="red",contour_width=3).generate(data)

plt.Figure(figsize=[10,10])
plt.imshow(bayrak)
plt.axis("off")
plt.show()
