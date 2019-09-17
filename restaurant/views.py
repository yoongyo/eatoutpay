from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect, redirect
from .models import MenuCategory, Menu, Restaurant, Review
from .forms import RestaurantForm, MenuForm, MenuCategoryForm
from django.contrib.auth.decorators import login_required
import sys
sys.path.append('..')
from admins.models import AdminComment

@login_required
def restaurant_list(request):
    restaurants = Restaurant.objects.filter(admin=request.user)
    return render(request, 'restaurant/restaurant_list.html', {
        'restaurants': restaurants,
    })


@login_required
def restaurant_detail(request, rpk):
    restaurant = get_object_or_404(Restaurant, pk=rpk)
    menus = Menu.objects.filter(restaurant__pk=rpk, admin=request.user)
    menu_category = MenuCategory.objects.filter(restaurant__pk=rpk, admin=request.user)
    menu_count = len(menus)
    reviews = Review.objects.filter(restaurant__pk=rpk)
    reviews_count = len(reviews)
    admin_comments = AdminComment.objects.filter(restaurant__pk=rpk, admin=request.user)
    admin_comments_count = len(admin_comments)
    reviews_sum = 0
    reviews_average = 0
    for i in reviews:
        reviews_sum += i.rating
        reviews_average = reviews_sum / reviews_count
        round(reviews_average, 1)
    count = reviews.count()
    like_count = get_object_or_404(Restaurant, pk=rpk).likes.count()

    return render(request, 'restaurant/restaurant_detail.html', {
        'restaurant': restaurant,
        'menus': menus,
        'menu_category': menu_category,
        'reviewsCount': count,
        'reviews_average': reviews_average,
        'admin_comments': admin_comments,
        'admin_comments_count': admin_comments_count,
        'menu_count': menu_count,
        'like_count': like_count
    })


@login_required
def restaurant_new(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.admin = request.user
            form.save()
            return redirect(form)
    else:
        form = RestaurantForm()

    return render(request, 'restaurant/restaurant_new.html', {
        'form': form
    })


@login_required
def restaurant_edit(request, rpk):
    restaurant = get_object_or_404(Restaurant, pk=rpk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form = form.save(commit=False)
            form.admin = request.user
            form.save()
            return redirect(form)
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'restaurant/restaurant_edit.html', {
        'form': form
    })


@login_required
def menu_list(request, rpk):
    menus = Menu.objects.filter(restaurant__pk=rpk)
    return render(request, 'restaurant/menu_list.html', {
        'menus': menus
    })


@login_required
def menu_detail(request, rpk, mpk):
    menu = get_object_or_404(Menu, pk=mpk)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return
    else:
        form = MenuForm(instance=menu)

    return render(request, 'restaurant/menu_detail.html', {
        'menu': menu,
        'form': form
    })


@login_required
def menu_new(request, rpk):
    restaurant = get_object_or_404(Restaurant, pk=rpk)
    if request.method == 'POST':
        menu_form = MenuForm(request.POST, request.FILES)
        if menu_form.is_valid():
            menu_form = menu_form.save(commit=False)
            menu_form.restaurant = restaurant
            menu_form.save()
            return
    else:
        menu_form = MenuForm(request.user, restaurant)

    return render(request, 'restaurant/menu_new.html', {
        'menu_form': menu_form,
    })


@login_required
def menu_category_new(request, rpk):
    restaurant = get_object_or_404(Restaurant, pk=rpk)
    if request.method == 'POST':
        form = MenuCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.admin = request.user
            form.restaurant = restaurant
            form.save()
            return
    else:
        form = MenuCategoryForm(request.user, restaurant)

    return render(request, 'restaurant/menu_category_new.html', {
        'form': form
    })

