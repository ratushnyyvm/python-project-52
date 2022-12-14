from django.contrib.auth import get_user_model
from django.views import generic

User = get_user_model()


class UserListView(generic.ListView):

    model = User
    template_name = 'users/index.html'
