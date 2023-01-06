from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from app_utspbo.forms import formJurnal
from django.shortcuts import redirect

def halamanjurnal(request):
    Jurnals = Jurnal.objects.all()
    data = {
        'Title' : "Data Bencana",
        'Heading' : "DATA JURNAL IKAN TAWAR",
        'Jurnals' : Jurnals,
    }
    return render(request, 'halamanjurnal.html' , data)

def detail(request, id):
    Jurnalikantawar = Jurnal.objects.get(pk=id)
    data = {
        'Title' : "DATA JURNAL IKAN TAWAR",
        'Jurnal' : Jurnalikantawar,
    }
    return render(request, 'detail.html', data)

def halamandetail(request):
    Jurnals = Jurnal.objects.all()
    data = {
        'Title' : "Tentang",
        'Heading' : "DATA JURNAL IKAN TAWAR",
        'Jurnals' : Jurnals,
    }
    return render(request, 'halamandetail.html' , data)


def tambahjurnal(request):
    if request.POST:
        form = formJurnal(request.POST)
        if form.is_valid():
            form.save()
            form = formJurnal()
            judul = 'Tambah Data Jurnal'
            pesan = 'Data Berhasil Ditambahkan!'
            data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'pesan' : pesan
    }
        return render(request, 'tambahjurnal.html', data)
    else:
        form = formJurnal()
        Jurnals = Jurnal.objects.all()
        data ={
        'title' : 'Tambah Data Jurnal',
        'heading' : 'Tambah Data Jurnal',
        'form' : form,
        'Jurnals' : Jurnals,
    }
    return render(request, 'tambahjurnal.html', data)


def updatejurnal(request, id_Jurnal):
    Jurnals = Jurnal.objects.get(id = id_Jurnal)
    judul = "Update Data Jurnal"
    template = "updatejurnal.html"
    if request.POST:
        form = formJurnal(request.POST, instance=Jurnals)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate!"
            data ={
            'title' : judul,
            'heading' : judul,
            'pesan' : pesan,
            'Jurnals' : Jurnals,

    }
        return render(request, template, data)
    else:
        form = formJurnal( instance=Jurnals)
        data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'Jurnals' : Jurnals,
    }
    return render(request, template, data)

def deletejurnal(request, id_Jurnal):
    Jurnals = Jurnal.objects.get(id = id_Jurnal)
    Jurnals.delete()

    return redirect('/halamanjurnal/')

# Create your views here.
