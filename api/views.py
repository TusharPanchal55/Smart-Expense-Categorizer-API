from rest_framework.views import APIView
from rest_framework.response import Response
import joblib

# Load your model
model = joblib.load("expense_model.pkl")

class ExpenseCategorizer(APIView):
    def post(self, request):
        print("DEBUG request.data:", request.data)  # 👈 log incoming data

        # Get the transaction text safely
        expense_text = request.data.get("transaction") or request.POST.get("transaction")


        if not expense_text:
            return Response({"error": "No transaction provided"}, status=400)

        # Predict category
        prediction = model.predict([expense_text])[0]

        return Response({
            "Transaction": expense_text,
            "Category": prediction
        })
