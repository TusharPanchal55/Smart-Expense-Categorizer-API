import pandas as pd # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.naive_bayes import MultinomialNB # type: ignore
from sklearn.pipeline import Pipeline # type: ignore
import joblib # type: ignore

data = pd.read_csv("datset.csv")

x = data["transaction"]
y = data["category"]

model = Pipeline([('tfidf', TfidfVectorizer()), ('clf', MultinomialNB())])

model.fit(x,y)


test_input = ["Uber Ride", "Netflix Subscription", "Dominos Pizza"]
print(model.predict(test_input))

joblib.dump(model, "expense_model.pkl")
print("Model created successfully!")
# print(data.head())