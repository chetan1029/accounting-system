from .models import Account, Transaction, Category, Choice, Result, Guest
from .serializers import CategorySerializer, ChoiceSerializer, GuestSerializer, ResultSerializer
from django.db.models import F
from rest_framework import generics, filters, status
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .utility import elo_rating_cal

def ping(request):
    return JsonResponse({"result": "pong"})


class ResultListView(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    filter_backends = [filters.OrderingFilter]
    ordering = ['-elo_rating']

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            choice_win = self.request.data.get("choice_win", None)
            choice_loss = self.request.data.get("choice_loss", None)
            guest_id = self.request.data.get("guest_id", None)

            choice_win_data = Choice.objects.get(id=choice_win)
            choice_loss_data = Choice.objects.get(id=choice_loss)
            guest, created = Guest.objects.get_or_create(guest_name=guest_id)

            ## Call Elo rating function to get elo ratings for the items
            result_win_data, created = Result.objects.get_or_create(choice_id=choice_win_data, guest_id=guest)
            elo_rating_win = result_win_data.elo_rating

            result_loss_data, created = Result.objects.get_or_create(choice_id=choice_loss_data, guest_id=guest)
            elo_rating_loss = result_loss_data.elo_rating

            elo_rating = elo_rating_cal(choice_win_data.pk, choice_loss_data.pk, elo_rating_win, elo_rating_loss, choice_win_data.pk)
            
            choice_win_row = {}
            choice_win_row["choice_id"] = choice_win_data.pk
            choice_win_row["guest_id"] = guest.pk
            choice_win_row["elo_rating"] = elo_rating["new_choice_win_rating"]
            serializer = self.get_serializer(data=choice_win_row)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            choice_loss_row = {}
            choice_loss_row["choice_id"] = choice_loss_data.pk
            choice_loss_row["guest_id"] = guest.pk
            choice_loss_row["elo_rating"] = elo_rating["new_choice_loss_rating"]
            serializer = self.get_serializer(data=choice_loss_row)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        with transaction.atomic():
            choice_win = self.request.data.get("choice_win", None)
            choice_loss = self.request.data.get("choice_loss", None)
            guest_id = self.request.data.get("guest_id", None)
            try:
                choice_win_data = Choice.objects.get(id=choice_win)
                choice_loss_data = Choice.objects.get(id=choice_loss)
                guest, created = Guest.objects.get_or_create(guest_name=guest_id)
                serializer.save(choice_id=choice, guest_id=guest)
            except:
                pass
            return super().perform_create(serializer)

    # def perform_create(self, serializer):
    #     with transaction.atomic():
    #         choice_win = self.request.data.get("choice_win", None)
    #         choice_loss = self.request.data.get("choice_loss", None)
    #         guest_id = self.request.data.get("guest_id", None)
    #         try:
    #             choice_win_data = Choice.objects.get(id=choice_win)
    #             choice_loss_data = Choice.objects.get(id=choice_loss)
    #             guest, created = Guest.objects.get_or_create(guest_name=guest_id)
    #             serializer.save(choice_id=choice, guest_id=guest)
    #         except:
    #             pass
    #         return super().perform_create(serializer)

