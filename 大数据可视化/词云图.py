from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import imageio

with open("E:\\study\\大数据可视化\\2.txt", 'r', encoding="utf-8") as f:
    text = f.read()
    cut_text = " ".join(jieba.cut(text))
heart_mask = imageio.imread('E:\\study\\大数据可视化\\heart.jfif')
cloud = WordCloud(
    font_path="C:\\Windows\\Fonts\\STXINGKA.TTF",
    mask=heart_mask,
    background_color="white",
    max_words=4000,
    max_font_size=60
)
wCloud = cloud.generate(cut_text)
wCloud.to_file("E:\\study\\大数据可视化\\result.png")
plt.imshow(wCloud, interpolation='bilinear')
plt.axis('off')
plt.show()


