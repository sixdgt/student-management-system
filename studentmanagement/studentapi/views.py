from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def student_detail(request, pk):
    std = Student.objects.get(id=pk)
    serializer = StudentSerializer(std)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# query set - all student data
def student_list(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std, many=True)
    return JsonResponse(serializer.data, safe=False)