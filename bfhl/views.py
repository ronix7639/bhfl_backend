from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BFHLAPIView(APIView):
    def get(self, request):
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.get("data", [])
        user_id = "rohit_patiballa_17091999"  # Replace with your actual details
        email = "rohit@xyz.com"  # Replace with your actual details
        roll_number = "ABCD123"  # Replace with your actual details

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lower_case_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lower_case_alphabets) if lower_case_alphabets else None

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return Response(response, status=status.HTTP_200_OK)
