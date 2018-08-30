from wordcloud import WordCloud
txt = 'I like python. I am learning python'
wordcloud = WordCloud().generate(txt)
wordcloud.to_file('testcloud.png')