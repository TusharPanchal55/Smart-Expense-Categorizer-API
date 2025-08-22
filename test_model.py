import joblib # type: ignore

model = joblib.load("expense_model.pkl")

test_input = ["Uber Ride",
    "Swiggy Order",
    "Electricity Bill",
    "Movie Ticket",
    "Amazon Shopping",]
print(model.predict(test_input))