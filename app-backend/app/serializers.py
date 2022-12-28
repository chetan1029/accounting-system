from rest_framework import serializers
from .models import Account, Transaction, Category, Choice, Guest, Result
from django.db.models import F


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name", "category_image", "created_at"]

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ["id", "guest_name", "created_at"]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "category_id", "choice_name", "choice_image","created_at"]
        read_only_fields = ['category_id']

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ["id", "choice_id", "guest_id", "elo_rating", "created_at"]