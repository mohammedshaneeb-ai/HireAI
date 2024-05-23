from django.shortcuts import render
from llm.llm_chains import get_sql_result
from .helper import format_user_question,connect_database,convert_2_list,generate_html_table
from django.http import JsonResponse
from adminapp.models import CompanyProfile
# Create your views here.

def chat(request,job_id):
    company = CompanyProfile.objects.get(user=request.user)
    if request.method == 'POST':
        print(job_id)
        msg = request.POST.get("msg")
        formated_query = format_user_question(msg,job_id)
        print(f"Formatted Query: {formated_query}")
        db = connect_database()
        result = get_sql_result(formated_query,db)
        if result == '':
            print('working from none answer')
            return JsonResponse({'content':result})
        print(f"Answer: {result}")
        result = convert_2_list(result)
        content,is_html = generate_html_table(result)
        print(f"content:{content}, is_html:{is_html}")

        return JsonResponse({'content':content,'is_html':is_html})

        
        
        
    return render(request,'chatapp/chat.html',{'job_id':job_id,'company':company})


