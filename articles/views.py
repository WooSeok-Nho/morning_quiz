from rest_framework.response import Response
from rest_framework.views import APIView
from articles import serializers
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method =='GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
