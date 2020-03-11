from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import PREDICTION_CHART
from .models import Registry
from . import forms
from first_app.forms import NewUserForm,FormName

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            password = form.cleaned_data['password']

            predictions = PREDICTION_CHART.objects.filter(userId = user, prediction__isnull = False).order_by('prediction')

            if len (predictions) == 0 :
                predictions = PREDICTION_CHART.objects.filter(userId = 'user_000052', prediction__isnull = False)

            con = 1
            dataRes_1 = []
            dataRes_2 = []
            dataRes_3 = []
            print(predictions)

            for prediction in reversed(predictions):

                if(con <= 3):
                    artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
                    dataRes_1.append(artistName.artistName)
                    con = con+1
                else:
                    if(con <=6):
                        artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
                        dataRes_2.append(artistName.artistName)
                        con = con+1
                    else:
                        if(con <= 9 ):
                            artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
                            dataRes_3.append(artistName.artistName)
                            con = con+1
                        else:
                            break

            dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,}

            if userValid(user,password):
                return  render(request,'basicapp/workPage.html',context=dataRes)

            else:
                data = {'user': 'null', 'password': 'null'}
                form = NewUserForm(data)
                form.is_valid()

                return render(request,'basicapp/pageError.html')

    return render(request,'basicapp/login.html',{'form':form})


def logup(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'basicapp/successPage.html')
        else:
            print('ERROR FORM INVALID')

    return render(request,'basicapp/logup.html',{'form':form})


def userValid (user, password):
    try:
        User.objects.get(user = user, password =  password)
    except:
        return False

    return True


def singout(request):
    return render(request,'index.html')


def search(request,**kwargs):

    user = kwargs['user']
    password = kwargs['user']
    dataRes = {'user': user, 'password': password}

    return  render(request,'basicapp/search.html',context=dataRes)


def search(request,**kwargs):
    form = forms.FormSearch()

    user = kwargs['user']
    user = kwargs['user']
    password = kwargs['user']
    dataRes = {'user': user, 'password': password,'form':form}

    return  render(request,'basicapp/search.html',context=dataRes)


def home(request,**kwargs):
    user = kwargs['user']
    password = kwargs['user']

    predictions = PREDICTION_CHART.objects.filter(userId = user, prediction__isnull = False).order_by('prediction')

    if len (predictions) == 0 :
        predictions = PREDICTION_CHART.objects.filter(userId = 'user_000052', prediction__isnull = False)

    con = 1
    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []
    print(predictions)

    for prediction in reversed(predictions):

        if(con <= 3):
            artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
            dataRes_1.append(artistName.artistName)
            con = con+1
        else:
            if(con <=6):
                artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
                dataRes_2.append(artistName.artistName)
                con = con+1
            else:
                if(con <= 9):
                    artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
                    dataRes_3.append(artistName.artistName)
                    con = con+1
                else:
                    break

    dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,}

    return  render(request,'basicapp/workPage.html',context=dataRes)


def analysis(request,**kwargs):

    user=kwargs['user']

    predictions = PREDICTION_CHART.objects.filter(userId = user, prediction__isnull = False).order_by('prediction')

    dataRes_artistName = []
    dataRes_artistId = []
    dataRes_prediction = []

    for prediction in reversed(predictions):
        dataRes_artistId.append(prediction.artistId)
        dataRes_prediction.append(prediction.prediction)
        artistName = Registry.objects.filter(musicbrainzArtistId = prediction.artistId).first()
        dataRes_artistName.append(artistName.artistName)

    dataRes = {'user': user, 'password': user,'dataRes_artistName':dataRes_artistName,'dataRes_artistId':dataRes_artistId,'dataRes_prediction':dataRes_prediction}
    return  render(request,'basicapp/analysis.html',context=dataRes)


def songSerch(request,**kwargs):
    form = forms.FormSearch()
    dataRes_  = []

    if request.method == 'POST':
        form = forms.FormSearch(request.POST)

        if form.is_valid():
            print("NAME: "+form.cleaned_data['search'])
            artistName = Registry.objects.filter(artistName = form.cleaned_data['search']).first()
            print(artistName)
            user=kwargs['user']
            try:
                dataRes_.append(artistName.artistName)
            except:
                dataRes = {'user': user, 'password': user}
                return render(request,'basicapp/NoResults.html',context=dataRes)
            dataRes = {'user': user, 'password': user,'form':form, 'dataRes_':dataRes_}

        print(user)
        return  render(request,'basicapp/search.html',context=dataRes)

    return  render(request,'basicapp/search.html',context=dataRes)


def scoreone(request,**kwargs):
    user=kwargs['user']
    artist=kwargs['dataRes']
    print('************************************ UNO'+artist)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scoretwo(request,**kwargs):
    user=kwargs['user']
    print('************************************ DOS'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scorethree(request,**kwargs):
    user=kwargs['user']
    print('************************************ TRES'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scorefour(request,**kwargs):
    user=kwargs['user']
    print('************************************ CUATRO'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scorefive(request,**kwargs):
    user=kwargs['user']
    print('************************************ CINCO'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)
