from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import UserProfileSerializer
from .permissions import IsAdminOrReadOnly, IsSuperUserOrOwner, IsSuperUser
from .models import UserProfile

# Create your views here.

class UserProfileViewSet(ModelViewSet):
    def get_queryset(self): 
        # only the user's profile
        return UserProfile.objects.select_related("user").filter(user=self.request.user)
    
    def get_serializer_class(self):
        return UserProfileSerializer
    
    # to autofill the user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
