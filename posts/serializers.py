from rest_framework import serializers
from .models import Post


# class PostSerializer(serializers.Serializer):   #manual serializer
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField(max_length=50)
#     content=serializers.CharField()
#     created=serializers.DateTimeField(read_only=True)


class PostSerializer(serializers.ModelSerializer):  #model based serializer
    
    title=serializers.CharField(max_length=50)  # adding extra validation 
    
    class Meta:
        model=Post
        fields=["id","title","content","created"]
        read_only_fields=["id","created"]
        
        
