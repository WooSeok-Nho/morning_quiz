from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article
from articles.serializers import ArticleSerializer
# Create your views here.
class index(APIView):
    def get(self, request, format = None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many =True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)