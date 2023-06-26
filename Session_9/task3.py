# A spam comment is defined by following keywords: "make a lot of money", "buy now" , "subscribe this" , "click this"

text = input("Enter the text: ")

if("make a lot of money" in text):
    spam  = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("this text is spam")
else:
    print("not spam")