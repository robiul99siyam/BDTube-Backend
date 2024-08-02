from .models import categoryModel,contentModel,ReviewModel ,Like
from rest_framework import serializers
from django.contrib.auth.models import User

# this category in serializer 
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']




class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryModel
        fields = '__all__'
    


# this content serializers 
class contentSerializer(serializers.ModelSerializer):
    category = categorySerializer()
    author = userSerializer()
    total_views = serializers.SerializerMethodField()
    total_likes = serializers.IntegerField(source="like.count", read_only=True)
   
    class Meta:
        model = contentModel
        fields = ['id', 'category', 'author', 'title', 'relase_date', 'language', 'videofile', 'thumbell', 'description', 'total_views', 'total_likes']

    def get_total_views(self, obj):
        return obj.total_view_count()

  

class LikeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'





# this is review serializers 
class reviewSeriailzer(serializers.ModelSerializer):
    user = userSerializer()
    content = contentSerializer()
    class Meta:
        model = ReviewModel
        fields = '__all__'

