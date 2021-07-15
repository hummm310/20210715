from django.shortcuts import render, redirect
# 登陸過後才能執行:
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
import random
from mysite.models import Post,Country,City
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np


def index(request): #index是為了呼應urls.py的index
	names = '林芷因'
	lotto = [random.randint(1,42) for i in range(6)]
	special = lotto[0]
	lotto = lotto[1:6]
	#0~2拍 產生360點
	x = np.linspace(-2*np.pi, 2*np.pi, 360)
	y1 = np.sin(x)
	y2 = np.cos(x)
	plot_div = plot([
		#散步圖
		go.Scatter(x=x, y=y1,
		mode='lines', name='SIN',
		#透明度=0.8
		opacity=0.8, marker_color='green'),
		
		go.Scatter(x=x, y=y2,
		mode='lines', name='COS', 
		opacity=0.8, marker_color='blue')
		],
		output_type='div') #輸出形式
	return render(request, 'index.html', locals())
	#next step:index.html


def news(request):
	posts = Post.objects.all() 
	return render(request, 'news.html' , locals())

@login_required(login_url='/admin/login/')
def show(request, id):
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect('/news/')
	return render(request, 'show.html' , locals())

@login_required(login_url='/admin/login/')
def rank(request):
	# 使用POST這個方法
	if request.method == 'POST':
		id = request.POST["id"]
		if id.strip() == '999':
			return redirect() ==('/rank/')
		try:
			# 在Country這張表取得藍色id country裡
			country = Country.objects.get(id=id)
		except:
			redirect("/rank/")
		cities = City.objects.filter(country=country)
		# 小到大排序.order_by('population')
	else:
		cities = City.objects.all()
	countries = Country.objects.all()
	return render(request, 'rank.html', locals())

#next step:產生rank.html

# @表示未登錄點chart會跳到登錄畫面
@login_required(login_url='/admin/login/')
def chart(request):
	if request.method == 'POST':
		id = request.POST["id"]
		if id.strip() == '999':
			return redirect() ==('/chart/')
		try:
			# 在Country這張表取得藍色id country裡
			country = Country.objects.get(id=id)
		except:
			redirect("/chart/")
		cities = City.objects.filter(country=country)
		# 小到大排序.order_by('population')
	else:
		cities = City.objects.all()
	countries = Country.objects.all() #出現國家的選單
	names = [city.name for city in cities]
	population = [city.population for city in cities]
	return render(request, 'chart.html', locals())
#next step:產生chart.html

def mylogout(request):
	logout(request)
	return redirect('/')

def delete(request,id):
	try:
		post = Post.objects.get(id=id)
		post.delete()
	except:
		return redirect('/news/')
	return redirect('/news/')