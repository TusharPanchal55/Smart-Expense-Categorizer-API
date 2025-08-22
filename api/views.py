from django.shortcuts import render # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
import joblib # type: ignore

model = joblib.load("expense_model.pkl")

class Expense_catogarizer(APIView):
    def post(self, request):
        expense_text = request.data.get("transaction")

        if not expense_text:
            return Response ({"Error: No transaction Available"}, status = 400)
        
        prediction = model.predict([expense_text])[0]

        return Response({"Transaction" : expense_text, "Category" : prediction})


