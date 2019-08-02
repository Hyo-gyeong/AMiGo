from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from .models import Korean, Lforeigner, Sforeigner, K_Comment, Lf_Comment, Sf_Comment
from .forms import KNew, LfNew, SfNew, K_CommentForm, Lf_CommentForm, Sf_CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    return render(request, 'index.html')

def korean(request):
    koreans = Korean.objects.all()

    korean_list = Korean.objects.all()
    paginator = Paginator(korean_list, 6)
    page = request.GET.get('page')
    try:
        kposts = paginator.get_page(page)   
    except PageNotAnInteger:
        kposts = paginator.get_page(1)

    return render(request, 'korean.html', {'koreans':koreans,'kposts':kposts})

def korean_delete(request, korean_id):
    korean = get_object_or_404 (Korean, pk = korean_id)
    korean.delete()

    return redirect('/korean')

def create_korean(request):

     # 1. 입력된 내용 처리 : POST
    if request.method == 'POST':

        kform = KNew(request.POST, request.FILES)
        if kform.is_valid(): 
            kpost = kform.save(commit=False)
            kpost.pub_date = timezone.now()
            kpost.save()
        return redirect('korean')
            
    # 2. 빈 페이지 띄워주는 기능 : GET
    else:

        kform = KNew()
        return render(request, 'create_korean.html', {'kform': kform}) 

def korean_search(request):
    korean_list = Korean.objects.all()
    return render(request, 'korean_search.html', {'korean_list', korean_list})

def korean_detail(request, korean_id):
    korean_detail = get_object_or_404(Korean, pk = korean_id)
    return render(request, 'korean_detail.html', {'korean_detail': korean_detail})

def korean_updateForm(request, korean_id):
    korean = get_object_or_404(Korean, pk=korean_id)
    if(request.user != korean.user):
        error = '글을 작성한 유저만 수정할 수 있습니다.'
        return redirect('/korean/'+korean_id)
    return render(request, 'korean_updateForm.html', {'korean': korean})

def kcomment_create(request, korean_id):
   
    if request.method == 'POST':
        korean = get_object_or_404(Korean, pk=korean_id)
        kcform = K_CommentForm(request.POST)
        
        if kcform.is_valid():
            kcomment = kcform.save(commit = False)
            kcomment.korean = korean
            kcomment.save()
        return redirect('/korean/' + str(korean.id))
    else:
        kcform = K_CommentForm()
        return render(request, 'korean_detail.html', {'kcform' : kcform})

def kcomment_delete(request, korean_id, kcomment_id):
    
    korean = get_object_or_404(Korean, pk=korean_id)
    kcomment = get_object_or_404(K_Comment, pk=kcomment_id)
    kcomment.delete()
    
    return redirect('/korean/' + str(korean.id))























def lforeigner(request):
    lforeigners = Lforeigner.objects.all()

    lforeigner_list = Lforeigner.objects.all()
    paginator = Paginator(lforeigner_list, 6)
    page = request.GET.get('page')
    try:
        lfposts = paginator.get_page(page)   
    except PageNotAnInteger:
        lfposts = paginator.get_page(1)

    return render(request, 'lforeigner.html',{'lforeigners':lforeigners,'lfposts':lfposts})

def lforeigner_delete(request, lforeigner_id):
    lforeigner = get_object_or_404 (Lforeigner, pk = lforeigner_id)
    lforeigner.delete()

    return redirect('/lforeigner')

def create_lforeigner(request):

    if request.method == 'POST':

        lfform = LfNew(request.POST, request.FILES)
        if lfform.is_valid(): 
            lfpost = lfform.save(commit=False)
            lfpost.pub_date = timezone.now()
            lfpost.save()
        return redirect('lforeigner')
            
    else:

        lfform = LfNew()
        return render(request, 'create_lforeigner.html', {'lfform': lfform})

def lforeigner_detail(request, lforeigner_id):
    lforeigner_detail = get_object_or_404(Lforeigner, pk = lforeigner_id)
    return render(request, 'lforeigner_detail.html', {'lforeigner_detail': lforeigner_detail})


def lforeigner_updateForm(request, lforeigner_id):
    lforeigner = get_object_or_404(Lforeigner, pk=lforeigner_id)
    if(request.user != lforeigner.user):
        error = '글을 작성한 유저만 수정할 수 있습니다.'
        return render(request, 'lforeigner_detail.html', {'error':error})
    return render(request, 'lforeigner_updateForm.html', {'lforeigner': lforeigner})

def lfcomment_create(request, lforeigner_id):
       
    if request.method == 'POST':
        lforeigner = get_object_or_404(Lforeigner, pk=lforeigner_id)
        lfcform = Lf_CommentForm(request.POST)
        
        if lfcform.is_valid():
            lfcomment = lfcform.save(commit = False)
            lfcomment.lforeigner = lforeigner
            lfcomment.save()
        return redirect('/lforeigner/' + str(lforeigner.id))
    else:
        lfcform = Lf_CommentForm()
        return render(request, 'lforeigner_detail.html', {'lfcform' : lfcform})

def lfcomment_delete(request, lforeigner_id, lfcomment_id):
    
    lforeigner = get_object_or_404(Lforeigner, pk=lforeigner_id)
    lfcomment = get_object_or_404(Lf_Comment, pk=lfcomment_id)
    lfcomment.delete()
    
    return redirect('/lforeigner/' + str(lforeigner.id))
















def sforeigner(request):
    sforeigners = Sforeigner.objects.all()

    sforeigner_list = Sforeigner.objects.all()
    paginator = Paginator(sforeigner_list, 6)
    page = request.GET.get('page')
    try:
        sfposts = paginator.get_page(page)   
    except PageNotAnInteger:
        sfposts = paginator.get_page(1)

    return render(request, 'sforeigner.html', {'sforeigners':sforeigners,'sfposts':sfposts})

def sforeigner_delete(request, sforeigner_id):
    sforeigner = get_object_or_404 (Sforeigner, pk = sforeigner_id)
    sforeigner.delete()

    return redirect('/sforeigner')

def create_sforeigner(request):
    
    if request.method == 'POST':
        sfform = SfNew(request.POST, request.FILES)

        if sfform.is_valid(): 
            sfpost = sfform.save(commit=False)
            sfpost.pub_date = timezone.now()
            sfpost.save()
            return redirect('sforeigner')
            
    else:

        sfform = SfNew()
        return render(request, 'create_sforeigner.html', {'sfform': sfform})

def sforeigner_detail(request, sforeigner_id):
    sforeigner_detail = get_object_or_404(Sforeigner, pk = sforeigner_id)
    return render(request, 'sforeigner_detail.html', {'sforeigner_detail': sforeigner_detail})


def sforeigner_updateForm(request, sforeigner_id):
    sforeigner = get_object_or_404(Sforeigner, pk=sforeigner_id)
    if(request.user != sforeigner.user):
        error = '글을 작성한 유저만 수정할 수 있습니다.'
        return render(request, 'sforeigner_detail.html', {'error':error})
    return render(request, 'sforeigner_updateForm.html', {'sforeigner': sforeigner})


def sfcomment_create(request, sforeigner_id):
       
    if request.method == 'POST':
        sforeigner = get_object_or_404(Sforeigner, pk=sforeigner_id)
        sfcform = Sf_CommentForm(request.POST)
        
        if sfcform.is_valid():
            sfcomment = sfcform.save(commit = False)
            sfcomment.sforeigner = sforeigner
            sfcomment.save()
        return redirect('/sforeigner/' + str(sforeigner.id))
    else:
        sfcform = Sf_CommentForm()
        return render(request, 'sforeigner_detail.html', {'sfcform' : sfcform})

def sfcomment_delete(request, sforeigner_id, sfcomment_id):
    
    sforeigner = get_object_or_404(Sforeigner, pk=sforeigner_id)
    sfcomment = get_object_or_404(Sf_Comment, pk=sfcomment_id)
    sfcomment.delete()
    
    return redirect('/sforeigner/' + str(sforeigner.id))















def about(request):
    return render(request, 'about.html')