import pickle

count_vectorizer = pickle.load(open('count_vectorizer_v2.pickle','rb'))
spam_mail = pickle.load(open('spam_detector_v2.pickle','rb'))

tra = count_vectorizer.transform([input("Email : ")])
ans = spam_mail.predict(tra)

if ans == 1:
    print(f"It's spam Mail. Be careful.")
else:
    print(f"It's not spam Mail :) ")
