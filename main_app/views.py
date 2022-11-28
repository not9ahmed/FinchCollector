from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird
from .forms import FeedingForm
# Create your views here.

# class Bird():
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# birds_list = [
#     Bird('Tweety', 'Brambling', 'Similar in size and shape to the chaffinch, the male has a black head in summer, and an orange breast with white belly. In flight it shows a long white rump.', 3),
#     Bird('Bull', 'Bullfinch', 'The male is unmistakable with his bright pinkish-red breast and cheeks, grey back, black cap and tail, and bright white rump.', 5),
#     Bird('Chaf', 'Chaffinch', 'The chaffinch is the UK\'s second commonest breeding bird, and is arguably the most colourful of the UK\'s finches.', 1),
#     Bird('Goldy', 'Goldfinch', 'A highly coloured finch with a bright red face & yellow wing patch. Sociable, often breeding in loose colonies, they have a delightful liquid twittering song.', 2),
# ]
        

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):

    birds_list = Bird.objects.all()
    
    context = {
        'birds': birds_list
    }

    return render(request, 'birds/index.html', context)

def birds_details(request, bird_id):
    
    bird = Bird.objects.get(id=bird_id)

    feeding_form = FeedingForm()

    context ={
        'bird': bird,
        'feeding_form': feeding_form
    }

    return render(request, 'birds/details.html', context)


class CreateBird(CreateView):
    model = Bird
    fields = '__all__'
    success_url = '/birds/'

class UpdateBird(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']
    success_url = '/birds/'

class DeleteBird(DeleteView):
    model = Bird
    success_url = '/birds/'



def add_feeding(request, bird_id):

  
  form = FeedingForm(request.POST)

  if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.bird_id = bird_id
      new_feeding.save()


  return redirect('details', bird_id=bird_id)