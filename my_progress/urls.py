from django.contrib import admin
from django.urls import path,include
from my_progress import views

app_name = "my_progress"

urlpatterns = [
    path('',views.ExerciseListView.as_view(),name = "Info"),
    # path('add-exercise/',views.ExercisePage.as_view(),name="Add"),
    path('add-exercise/',views.exercise_page,name="Add"),
    path('delete/<int:id>',views.delete,name = "Delete"),
    path('update/<slug:pk>',views.UpdateExercise.as_view(),name = "Update"),
    
]