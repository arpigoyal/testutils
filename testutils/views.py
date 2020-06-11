# i hav ecreated this new file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params={'name':'harry','place':'mars'}
    return render(request,'index.html')
    # return HttpResponse('<h1>hello harry</h1> <a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">GO TO full playlist<a/>')

def about(request):
    return HttpResponse('about arpit goyal')
def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')
    # check the checkbox values
    removepunc= request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc=="on":

        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
             analyzed = analyzed + char
        params={'purpose':'removed puncatuations','analyzed_text':analyzed}
        djtext=analyzed

        #return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
            # analyze the text
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char.upper()
        params = {'purpose': 'New line reomever', 'analyzed_text': analyzed}
                # analyze the text
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
                # analyze the text
        djetxt=analyzed
        #return render(request, 'analyze.html', params)
    if charcount == "on":
        analyzed = ""
        result=0
        for i in djtext:
            result=result+1
        print("no of characters in djtext is ", result)

        params = {'purpose': 'char count', 'analyzed_text': analyzed}
        # analyze the text
    if(removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps !="on" and charcount!="on")
            return HttpResponse("error")

    return render(request, 'analyze.html', params)


def capfirst(request):
    return HttpResponse('capitalizefirst')
def newlineremove(request):
    return HttpResponse('newlineremove')
def spaceremove(request):
    return HttpResponse("spaceremover <a href='/'>back<a/>")
def charcount(request):
    return HttpResponse('charcount')
def navigation(request):
    s ='''<h2>Navigation Bar<br></h2>
    <a href= "http://www.facebook.com">GO TO FACEBOOK</a><br>
    <a href= "http://www.google.com">GO TO GOOGLE</a><br>'''
    return HttpResponse(s)
