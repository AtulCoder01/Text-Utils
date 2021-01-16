from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # if text var nown found the print defalt value
    # Get the text
    djtext = request.POST.get('text', 'defalt')
    # check checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('caps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(djtext)
    print(removepunc)
    # analyzed = "djtext"
    if removepunc == "on":
        # punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                # analyzed += char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlinerem == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Total Character', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    if(removepunc != "on" and fullcaps != "on" and extraspaceremove != "on" and charcount != "on" and newlinerem != "on"):
        return HttpResponse("Please Slect any operations. try again")

    return render(request, 'analyze.html', params)
