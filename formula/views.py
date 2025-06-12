from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

SUGGESTIONS = ["Revenue", "Cost", "Profit", "Margin", "Expenses", "Sales"]

@api_view(['GET'])
def suggestion_api(request):
    query = request.GET.get("q", "").lower()
    results = [ {"label": item} for item in SUGGESTIONS if query in item.lower() ]
    return Response(results)

def editor_page(request):
    return render(request, 'formula/editor.html')
