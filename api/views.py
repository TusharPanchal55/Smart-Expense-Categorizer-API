from rest_framework.views import APIView
from rest_framework.response import Response
import json
import joblib
import os

# Load your trained model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "expense_model.pkl")  # ✅ new path (root)
model = joblib.load(model_path)

class ExpenseCategorizer(APIView):
    def post(self, request, *args, **kwargs):
        transaction_text = None

        # Try request.data first
        if "transaction" in request.data:
            transaction_text = request.data.get("transaction")
        elif "Transaction" in request.data:
            transaction_text = request.data.get("Transaction")
        else:
            # Try manual JSON parsing
            try:
                data = json.loads(request.body.decode("utf-8"))
                transaction_text = data.get("transaction") or data.get("Transaction")
            except Exception as e:
                print("JSON parse error:", e)

        if not transaction_text:
            return Response({"Error": "No transaction Available"}, status=400)

        # Predict category using ML model
        category = model.predict([transaction_text])[0]

        return Response({
            "Transaction": transaction_text,
            "Category": category
        })
