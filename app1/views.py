
# n=7
# for i in range(1,n-2):
#     k=i
#     for j in range(1,8):
#         if (j>=5-i and j<=3+i):
#             print(k,end=' ')
#             if j<4:
#                 k=k+1
#             else:
#                 k=k-1
#         else:
#             print('  ', end='')
#     print()
# z=[]
# s='OneTwo'
# f=''
# l=''
# for i,x in enumerate(s):
#     if x.isupper():
#         if f=='':
#             f=i
#         elif type(f)==int and l=='':
#             l=i
#             z.append(s[f:l])
#             try:
#                 if
#             except:
#                 pass
#             f,l=l,''
# print(z)



# input='OneTwoEight'
# js=re.findall('[A-Z][a-z]+', inp)
# a=''
# print(js)
# for i in js:
#     a=a+str(numbers.index(i))
# print(a)


import re

# numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

# def my_converter():
#     numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
#     user_input = input("Give Input Here :  ")
#     list_of_num = re.findall('[a-zA-Z][a-z]+', user_input)
#     output = ''
#     for num in list_of_num:
#         val=num.title()
#         output = output + str(numbers.index(val))
#     print(output)
# my_converter()



# user_input = input("Give Input Here :  ")
# l=[]
# word=user_input[0]
# for i,v in enumerate(user_input[1:]):
#     if i == len(user_input) - 2:
#         word = word + v
#         l.append(word)
#     elif ord(v) in range(ord('a'), ord('z')+1):
#         word=word+v
#     else:
#         l.append(word)
#         word=v
# l1=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# for j in l:
#     for i,v in enumerate(l1):
#         if v==j:
#             print(i,end='')




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
import requests
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}

        return Response(content)


def form(request):
    if  request.POST.get('username'):
        username=request.POST['username']
        password=request.POST['password']
        response=requests.post('http://127.0.0.1:8000/api/token/',data={'username':username,'password':password})
        refresh=response.json()['refresh']
        access=response.json()['access']
        return render(request,'get_token.html',context={'refresh':refresh,'access':access},)

    elif request.POST.get('access'):
        access=request.POST['access']
        refresh=request.POST['refresh']

        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(access)}
        response = requests.get('http://127.0.0.1:8000/hello/',headers=headers)
        data=response.json()
        if response.status_code==401:
            headers = {'refresh': '{}'.format(refresh)}
            response = requests.post('http://127.0.0.1:8000/api/token/refresh/', data=headers)
            print(response.status_code)
            return render(request, 'get_token.html', {'data': data, 'refresh': refresh, 'access': access,
                                    'new':response.json().get('access')})
        return render(request, 'get_token.html',{'data':data,'refresh':refresh,'access':access})

    elif request.method=='GET':
        return render(request, 'get_token.html')




def my_function(request):
    # print(1/0)
    return HttpResponse('<h1>HELLO WORLD</h1>')


@csrf_exempt
def template(request):
    msg=request.POST['msg']
    title=request.POST['title']
    name=request.POST['name']
    data={'name':name,'title':title,'msg':msg}
    # return render(request,'page1.html',context=data)
    return TemplateResponse(request,'page1.html',context=data)
