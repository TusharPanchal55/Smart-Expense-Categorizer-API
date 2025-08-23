from rest_framework.views import APIView
from rest_framework.response import Response
import joblib
import json

class ExpenseCategorizer(APIView):
    def post(self, request, *args, **kwargs):
        transaction_text = None

        # Try request.data first
        if "transaction" in request.data:
            transaction_text = request.data.get("transaction")
        else:
            # Try manual JSON parsing
            try:
                data = json.loads(request.body.decode("utf-8"))
                transaction_text = data.get("transaction") or data.get("Transaction")
            except Exception as e:
                print("JSON parse error:", e)

        if not transaction_text:
            return Response({"Error": "No transaction Available"}, status=400)

        category = categorize_transaction(transaction_text)
        return Response({
            "Transaction": transaction_text,
            "Category": category
        })
