from django.shortcuts import render, redirect, get_object_or_404


def site(request):
	return render(request, 'mysite.html')
