from rest_framework import serializers

from api.models import Account, Match, Location


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_id', 'name', 'gender', 'age', 'description', 'orientation', 'photo_link1',
                  'photo_link2', 'photo_link3', 'photo_link4', 'photo_link5', 'photo_link6')
        
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('user_id','match_user_id','islike')
        
class LocationSerializer(serializers.ModelSerializer):
    #user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Location
        fields = ('user_id','latitude','longitude')