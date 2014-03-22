from rest_framework import serializers
from api.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_id', 'name', 'gender', 'age', 'description', 'orientation', 'photo_link1',
                  'photo_link2', 'photo_link3', 'photo_link4', 'photo_link5', 'photo_link6')