from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from example.models import Artist
from example.serializers import ArtistSerializer


@csrf_exempt
def artist_list(request):

    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def artist_detail(request, pk):

    if request.method == 'GET':
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        artist = Artist.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(artist, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        artist = Artist.objects.get(pk=pk)
        artist.delete()
        return JsonResponse(data={'message': 'Deleted'}, status=204)
