filename=r"D:\Python-Toolkit\_Projects\sample.txt"
with open(filename) as file:
    text=file.read()
words=text.lower().split()
word_freq={}
for word in words:
    word=word.strip(".,!?;:[]{}()/\"'")
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1
sorted_words=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
print("\nTop 10 most frequent words:")
for word,freq in sorted_words[:10]:
    print(f"{word}: {freq}")