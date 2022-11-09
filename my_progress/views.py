from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView,FormView
from my_progress.models import Exercise
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from my_progress.forms import AddExerciseForm
# Create your views here.

class ExerciseListView(ListView):
    
    model = Exercise
    paginate_by: 10
    context_object_name = "exercises"
    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)
    
class ExercisePage(CreateView):
    form_class = AddExerciseForm
    template_name = 'my_progress/add_exercise.html'
    success_url= '/progress/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user:
            print(self.request.user)
            self.object.user = self.request.user
        
        self.object.save()
        return super(ExercisePage, self).form_valid(form)
    

# @csrf_exempt
def exercise_page(request):
    if(request.method == "POST"):
        
        form_info = AddExerciseForm(data = request.POST)
        # print(form_info)
        exercise = form_info.save()
        print(type(exercise))
        if request.user:
            print(request.user)
            # request.object.user = request.user
        
            exercise.user = request.user
        exercise.save()
        
    else:
        form_info = AddExerciseForm()
    return render(request,'my_progress/add_exercise.html',{'form':form_info})
    
    
def delete(request,id):
    exercise = Exercise.objects.get(id = id) 
    exercise.delete()
    return HttpResponseRedirect(reverse('my_progress:Info'))
    

class UpdateExercise(UpdateView):
    model = Exercise
    # form_class = AddExerciseForm
    fields = ["current_weight","goal_weight","rep_count"]
    template_name = "my_progress/update_exercise_form.html"
    success_url = '/progress/'
    
        
    