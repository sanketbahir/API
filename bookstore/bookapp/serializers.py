from rest_framework import serializers
from .models import BookModels

class BookModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModels
        fields = ['id','firstname','lastname','city','age']
        read_only_fields = ['id']

        # add custom validator
        def validate(self,data):
            if(len(data['firstname']))== 0:
                raise serializers.validationError({'error':'name should be blank'})
            return data