from django.shortcuts import render
from .forms import FeedbackForm
from django.views.generic import TemplateView, FormView
from rest_framework import viewsets
from .serializers import FeedbackSerializer
from .models import Feedback

class FeedbackFormView(TemplateView, FormView):
    template_name = "main.html"
    form_class = FeedbackForm


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-created_date')
    serializer_class = FeedbackSerializer
