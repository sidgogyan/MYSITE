from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import subprocess


def run_java(code):
    # f = open("Main.java", "a")
    # f.write("")
    # f.write(code)
    # f.close()
    
    with open('Main.java', "w") as myfile:
         myfile.write(code)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    print(ROOT_DIR)
    try:
        compile= subprocess.check_output(
        "javac Main.java", stderr=subprocess.STDOUT, timeout=10,
        universal_newlines=True,shell=True)

    

        output= subprocess.check_output("java Main",stderr=subprocess.STDOUT, timeout=10,
        universal_newlines=True,shell=True)
        return output
     
    except subprocess.CalledProcessError as exc:
      print("Status : Compilation Error", exc.returncode, exc.output)
      return exc.output
    
    

@api_view(['POST'])
def run_code(request):
       code=request.data.get('code')
       langauge=request.data.get('len')
       if(code==None):
           code=""
       if(langauge=='java'):
           output=run_java(code) 
           context={
            'output':output
           }
       return Response(context)
       

# Create your views here.



