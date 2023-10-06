import io

from django.http import HttpResponse
from django.views import View
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from blog.models import Post
from blog_Api.models import Student
from .serializers import PostSerializer, StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass


class PostDitails(generics.RetrieveAPIView):
    pass


class student_info(generics.ListCreateAPIView):
    def get(self, request):
        queryset = Student.objects.all()

        serializer_class = StudentSerializer(queryset,many=True)

        json_Data = JSONRenderer().render(serializer_class.data)

        return HttpResponse(json_Data)


@csrf_exempt
def Student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)

        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'successfully insert the data to the model '}

            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(stream)
        pythondata = JSONParser().parse(stream)
        print(pythondata)
        id = pythondata.get('id')
        stdnt = Student.objects.get(id=id)
        serializers = StudentSerializer(stdnt, data=pythondata, partial=True)
        print(serializers)
        if serializers.is_valid():
            serializers.save()

            res = {'msg': 'successfully updated the data to the model '}

            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data)
