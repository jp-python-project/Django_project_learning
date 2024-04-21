from django.shortcuts import render, get_object_or_404, redirect

from Test_Meeting.models import Meeting, Room
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/details.html', {'meeting': meeting})

@login_required
def room_list(request):
    return render(request, 'meetings/room_obj.html',
                  context={'rooms': Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])


@login_required
def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})

@login_required
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("details", id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html",
                  {"form": form})
@login_required
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        # Form is only shown to ask for confirmation
        # When we get a POST, we know we can go ahead and delete
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request, "meetings/confirm_delete.html",
                      {"meeting": meeting})