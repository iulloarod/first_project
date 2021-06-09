from django.shortcuts import HttpResponse, redirect

def root(request):
	return redirect("/blogs")

def create(request):
	return redirect("/")

def destroy(request,number):
	return redirect("/blogs")


from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")


def new(request):
	return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")


def show(request,number):
	return HttpResponse(f"placeholder para mostrar el blog numero {number}")


def edit(request,number):
	return HttpResponse(f"placeholder para editar el blog {number}")

from django.http import JsonResponse

def json(request):
	return JsonResponse({"Nombre" : "Don Ignacio"})