from django.shortcuts import render

def homepage(request):
    return render(request, 'pratoservido/homepage.html')
