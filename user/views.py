from django.shortcuts import render
from django.http import HttpResponse, response
from . import ctrack

def user(request):

    rp = ctrack.Track('carloosxdd','BQCBYd9IA9b-YUsJeDtIKL9igyywjMZHgcAID_RXfoTJCuI3BfgAQPDEKz1mx9GmwjfQ_UOWZsz1_c8BIobpjX-PSY37oj_6Dmlq7tBt7C1iCubTVrgAeCMCMkd5qdr5UNOikSvKB1cTbG7Jjxm0XLkczYtIF8u9ZCdRjwKUhK2uCM0yq6H7DIx8NXwVSjEyu0XQ_0zg2wWwK2AWuad_oXZofyxAHebR4SqkTh4jU__HVtDmJi94Aq92Vj2eFdrc6dKB86IJsKicJqaxZJeDnrOD', 'a', 'a')

    user = rp.user()

    return render(request, 'user.html', user)
