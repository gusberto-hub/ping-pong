# from django.contrib.auth import get_user_model
from rest_framework import serializers
# from category.models import Category, SubCategory
from member_request.models import MemberRequest, HelperReview


class HelperReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelperReview
        fields = ["rating"]


class ListMemberRequestSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    member_username = serializers.CharField(source='member.username', read_only=True)
    helper_username = serializers.CharField(source='helper.username', read_only=True)

    member_city = serializers.CharField(source='member.city', read_only=True)
    member_zip = serializers.CharField(source='member.city', read_only=True)
    member_lon = serializers.FloatField(source='member.lon', read_only=True)
    member_lat = serializers.FloatField(source='member.lat', read_only=True)
    # helper_rating = serializers.InergerField(source='')

    # helper_rating = HelperReviewSerializer(read_only=True)

    class Meta:
        model = MemberRequest
        fields = ['id', 'title', 'created', 'img_one', 'description', 'budget', 'category_name', 'urgency',
                  'member_username', 'helper_username', 'member_zip', 'member_city', 'member_lon', 'member_lat']


class MemberRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRequest
        fields = '__all__'


