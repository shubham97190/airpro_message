from django.views.generic.edit import FormView
from django.contrib import messages

from message.forms import EmailForm
# Create your views here.

class PageView(FormView):
    template_name = 'index.html'
    form_class = EmailForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        enquiry = form.save(commit=False)
        messages.success(self.request,'Your message has been sent successfully')
        enquiry.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("dsadfmskfnsfkns")
        return super().form_invalid(form)