from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    '''comment = CommentSerializer()'''
    class Meta:
        model = Post
        fields = ('id','author', 'title', 'text')

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = ('author', 'text', 'post')
