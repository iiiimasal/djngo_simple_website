from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Room , Topic
from django.db.models import Q
from .form import RoomForm
# rooms =[
#     {'id':1,'name':'lets learn python'},
#     {'id':2,'name':'lets learn Java'},
# ]

def projects(request):
    return render(request,'tempelates.html')

def project(request,pk):
    return HttpResponse('Single project'+" "+str(pk))
 
# def room(request,age):
#     if str(age)=="12":
#         return render(request,'room.html',{'rooms':rooms})
#     else :
# 
# 
#         return HttpResponse('age under limmited')


def home(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''

    rooms=Room.objects.filter(Q(topic__name__icontains=q)|
                              Q(name__icontains=q)|
                              Q(description__icontains=q)
                              )
    topic=Topic.objects.all()

    context={'rooms':rooms,'topics':topic}
    return render(request,'home.html',context) 

def room(request,pk):
    room=Room.objects.get(id=pk)
   
    context={'room':room}        
    return render(request,'room.html',context)
   
 
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
       form = RoomForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('room')

    context = {'form': form}
    return render(request, 'room-form.html', context)


def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.method == 'POST':
       form = RoomForm(request.POST,instance=room)
       if form.is_valid():
            form.save()
            return redirect('room')


    context = {'form': form}
    return render(request, 'room-form.html', context)

def deleteRoom(request , pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room')
    
    return render(request,'delete.html',{'obj':room})