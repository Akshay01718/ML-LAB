senetence=input("Enter the sentence:")

words=senetence.lower().split()

word_count={}

for word in words:
    word=word.strip('.,!/;:"()')

    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print("\nWords in sentence:")
for word,count in word_count.items():
    print(f"{word}:{count}")