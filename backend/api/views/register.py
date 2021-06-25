# -*- coding: utf-8 -*-

from api.views._base import *

from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token



################################################################################
class RegisterSerializer(serializers.ModelSerializer):

	#---------------------------------------------------------------------------
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    #---------------------------------------------------------------------------
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    #---------------------------------------------------------------------------
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        
        
################################################################################
class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )
    
	#---------------------------------------------------------------------------
    def post(self, request):
        #-----------------------------------------------------------------------
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #-----------------------------------------------------------------------
        token, created = Token.objects.get_or_create(user=user)
        #-----------------------------------------------------------------------
        data = {
            'token': token.key
        }
        #-----------------------------------------------------------------------
        return Response(data, status=status.HTTP_201_CREATED)
        #-----------------------------------------------------------------------
