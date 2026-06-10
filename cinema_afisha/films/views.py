from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  .models import Film
from .serializers import FilmListSerializer, FilmDetailSerializer


@api_view(http_method_names=['GET'])
def film_list_api_view(request):
    films = Film.objects.select_related('director').prefetch_related('genres', 'reviews').all()

    data = FilmListSerializer(films, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK,
    )

@api_view(http_method_names=['GET'])
def film_detail_api_view(request,id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'error: Film not found!'},
        )

    data = FilmDetailSerializer(film).data
    return Response(
        data=data,
        status=status.HTTP_200_OK,
    )