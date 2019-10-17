from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuCategory, Menu, Restaurant, Review, Area, Region
from .forms import RestaurantForm, MenuForm, MenuCategoryForm
from django.contrib.auth.decorators import login_required
from .serializers import ReviewSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import sys
sys.path.append('..')
from admins.models import AdminComment


@login_required
def restaurant_detail(request):
    restaurant = get_object_or_404(Restaurant, admin=request.user)
    menus = Menu.objects.filter(restaurant=restaurant, admin=request.user)
    menu_category = MenuCategory.objects.filter(restaurant=restaurant, admin=request.user)
    menu_count = len(menus)
    reviews = Review.objects.filter(restaurant=restaurant)
    reviews_count = len(reviews)
    admin_comments = AdminComment.objects.filter(restaurant=restaurant, admin=request.user)
    admin_comments_count = len(admin_comments)
    reviews_sum = 0
    reviews_average = 0
    for i in reviews:
        reviews_sum += i.rating
        reviews_average = reviews_sum / reviews_count
        round(reviews_average, 1)
    count = reviews.count()
    like_count = restaurant.likes.count()

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
def restaurant_edit(request):
    restaurant = get_object_or_404(Restaurant, admin=request.user)
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
def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    restaurant = get_object_or_404(Restaurant, admin=request.user)
    return render(request, 'restaurant/menu_detail.html', {
        'menu': menu,
        'restaurant': restaurant
    })


@login_required
def menu_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, admin=request.user)
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return
    else:
        form = MenuForm(request.user, restaurant, instance=menu)

    return render(request, 'restaurant/menu_edit.html', {
        'menu': menu,
        'menu_form': form
    })


@login_required
def menu_new(request):
    restaurant = get_object_or_404(Restaurant, admin=request.user)
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
def menu_category_new(request):
    restaurant = get_object_or_404(Restaurant, admin=request.user)
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


class ReviewViewSet(APIView):
    pass
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        reviews_serializer = ReviewSerializer(data=request.data)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return Response(reviews_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(reviews_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def getRegion(request):
    region = ['서울', '경기', '인천', '강원', '제주', '부산', '경남', '대구', '경북', '울산', '대전', '충남', '충북', '광주', '전남', '전북']
    for i in region:
        Region.objects.create(name=i)
    return


def getArea(request):
    region1 = get_object_or_404(Region, name='서울')
    area1 = ['강남·역삼·삼성·논현', '서초·방배', '잠실·신천', '영등포·여의도', '구로·금천·신도림', '강서·화곡·까치산역·목동',
             '천호·길동·둔촌', '서울대·신림·사당·동작', '종로·대학로', '용산·중구·명동·이태원' '성북·도봉·노원', '강북·수유·미아',
             '왕십리·성수', '건대·광진', '동대문·장안·청량리', '중랑·상봉·면목·태릉', '신촌·홍대·서대문·마포', '은평·연신내·불광']
    for i in area1:
        Area.objects.create(name=i, region=region1)

    region2 = get_object_or_404(Region, name='경기')
    area2 = ['수원·인계', '수원시청·권선·영통', '수원역·세류·팔달문·구운·장안', '대부도·제부도', '안성·평택·송탄', '오산·화성·동탄',
             '파주·김포', '고양·일산', '의정부', '부천', '안양·평촌·인덕원·과천', '군포·금정·산본·의왕', '안산', '광명·시흥', '용인',
             '이천·광중·여주', '성남·분당', '구리·남양주·하남', '가평·양평', '양주·동두천·연천·장흥', '포천']
    for i in area2:
        Area.objects.create(name=i, region=region2)

    region3 = get_object_or_404(Region, name='인천')
    area3 = ['부평', '주안', '구월·소래포구', '동암·간석', '중구·월미도·을왕리·인천공항', '작전·경인교대', '용현·숭의·도화·송림', '송도·연수',
             '서구·검단', '강화·옹진·백령도']
    for i in area3:
        Area.objects.create(name=i, region=region3)

    region4 = get_object_or_404(Region, name='강원')
    area4 = ['강릉역·교동택지·옥계', '경포대·사천·주문진', '양양·낙산·하조대·인제', '속초·설악·동명항·고성', '춘천·홍천·철원·화천',
             '원주·횡성', '정동진·동해·삼척', '평창·영월·정선·태백']
    for i in area4:
        Area.objects.create(name=i, region=region4)

    region5 = get_object_or_404(Region, name='제주')
    area5 = ['제주시', '서귀포·마라도']
    for i in area5:
        Area.objects.create(name=i, region=region5)

    region6 = get_object_or_404(Region, name='부산')
    area6 = ['해운대·재송', '송정·기장·정관', '서면·초읍·양정', '연산·토곡', '동래·온천장·부산대·구서·사직', '남포동·부산역·송도·영도·범일동',
             '광안리·수영·경성대·대연·용호', '사상', '덕천·만덕·구포·화명·북구', '강서·하단·사하·명지·신호']
    for i in area6:
        Area.objects.create(name=i, region=region6)

    region7 = get_object_or_404(Region, name='경남')
    area7 = ['김해·장유', '양산·밀양', '거제·통영·고성군', '진주', '사천·남해·하동', '창원 상남·용호·중앙', '창원 명서·팔용·봉곡·북면',
             '마산·진해', '거창·함안·창녕·합천·의령']
    for i in area7:
        Area.objects.create(name=i, region=region7)

    region8 = get_object_or_404(Region, name='대구')
    area8 = ['동성로·시청·서문시장·평리동·비산동', '수성구·남구·수성못', '동대구역·신천·대구공항·동촌', '경북대·북구·칠곡지구',
             '본리·죽전·이월드·두류공원·서부정류장']
    for i in area8:
        Area.objects.create(name=i, region=region8)

    region9 = get_object_or_404(Region, name='경북')
    area9 = ['경주', '구미', '포항 남구', '포항 북구', '울진·울릉도·청송·영덕', '영천·경산·청도', '문경·상주·영주·예천', '안동',
             '김천·성중·칠곡·의성·군위']
    for i in area9:
        Area.objects.create(name=i, region=region9)

    region10 = get_object_or_404(Region, name='울산')
    area10 = ['동구·울주군', '남구·중구·북구']
    for i in area10:
        Area.objects.create(name=i, region=region10)

    region11 = get_object_or_404(Region, name='대전')
    area11 = ['유성 봉명·도안·장대', '중구 은행·대흥·선화·유천', '동구 용전·복합터미널', '대덕구 신탄진·중리', '서구 둔산·용문·월평']
    for i in area11:
        Area.objects.create(name=i, region=region11)

    region12 = get_object_or_404(Region, name='충남')
    area12 = ['천안 서북구', '천안 동남구', '계룡·공주·금산·논산', '아산', '태안·당진·안면도·서산', '서천·부여', '대천·보령', '예산·청양·홍성',
              '세종']
    for i in area12:
        Area.objects.create(name=i, region=region12)

    region13 = get_object_or_404(Region, name='충북')
    area13 = ['청주 흥덕구·서원구', '청주 상당구·청원구', '제천·진천·음성·단양', '충주·수안보', '증평·괴산·영동·보은·옥천']
    for i in area13:
        Area.objects.create(name=i, region=region13)

    region14 = get_object_or_404(Region, name='광주')
    area14 = ['북구', '서구', '동구·남구', '광산구']
    for i in area14:
        Area.objects.create(name=i, region=region14)

    region15 = get_object_or_404(Region, name='전남')
    area15 = ['여수', '순천·광양', '목포·무안·영암', '나주·담양·곡성·구례·영광·장성·함평', '화순·보성·해남·완도·강진·고흥']
    for i in area15:
        Area.objects.create(name=i, region=region15)

    region16 = get_object_or_404(Region, name='전북')
    area16 = ['전주 덕진구', '전주 완산구·완주', '군산', '익산', '남원·임실·진안·무주·순창', '김제·부안·고창·정읍']
    for i in area16:
        Area.objects.create(name=i, region=region16)

    return