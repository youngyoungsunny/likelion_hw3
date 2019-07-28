from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import PortfolioPost

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios' : portfolios})





