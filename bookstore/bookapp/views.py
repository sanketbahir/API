from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import BookModels
from .serializer import BookModelsSerializers
from rest_framework.response import Response
from rest_framework.excptions import APIException
from rest_framework import status

class BookModelsViewSet(ModelViewSet):
    queryset = ModelViewSet.objects,all()
    serializer_class = BookModelsSerializers

    def get_serializer_class(self):
        return self.serializer_class

    def list(self,request):
        try:
            sample_objs = BookModels.objects.all()
            serializer = self.get_serializer(sample_objs, many = True)

            return Response({
              'status':status.HTTP_200_OK,
              'data':serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
              'message':APIException.default_detail,
              'status':APIException.status_code
            })

    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)

            if not serializer.is_valid():
                print(serializer.error)
                return Response({
                  'status':status.HTTP_400_BAD_REQUEST,
                  'data':serializer.error,
                  'message':'Invalid data'
                })
            serializer.save()

            return({
              'status':status.HTTP_201_BAD_CREATED,
              'data':serializer.data,
              'message':'Detail added successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
              'message':APIExecption.default_detail,
              'status':APIExecption.status_code
            })

    def retrieve(self,request, pk=None):
        try:
            id = pk
            if id is not None:
                sample_obj = self.get_object()
                serializer = self.gat_serializer(sample_obj)

            return Response({
              'status':status.HTTP_200_OK,
              'data':serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
              'message':APIException.default_detail,
              'status':APIException.stauts_code
            })

    def update(self,request, pk = None):
        try:
            sample_objs = self.get_object(),
            serializer = get_serializer(sample_objs,data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.error)
                return Response({
                  'status':status.HTTP_400_BAD_REQUEST,
                  'data':serializer.error,
                  'message':'Invalide data'
                })

            serializer.save()
            return Response({
              'status':status.HTTP_200_OK,
              'data':serializer.data,
              'messege':'Detail update successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
              'message':APIException.default_detail,
              'status':APIException.status_code
            })

    def partial_update(self, request, pk= None):
        try:
            sample_obj = self.get_object(),
            serializer = self.get_serializer(sample_obj, data=request.data, partial =True)
            if not Serializer.is_valid():
                print(serializer.error)
                return Responce({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data':sarializer.error,
                    'message':'Invalid Data'
                })
                serializer.save()
            return Responce({
                'status': status.HTTP_300_ok,
                'data':sarializer.data,
                'message':'Book added successfully'  
                })
         except Exception as e:
            print(e)
            raise APIException({
              'message':APIException.default_detail,
              'status':APIException.status_code
            })
    def destroy(self,request, pk):
        try:
            id = pk 
            sample_obj = self.get_object()
            sample_obj =.delete()
            return Response({
              'status':status.HTTP_200_OK.
              'message':'Detail deleted successfully'
            })
            
        except Exception as e:
            print(e)
            raise APIException({
              'message':APIException.default_detail,
              'status':APIException.status_code
            })
