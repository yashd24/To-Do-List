from rest_framework.views import APIView
from .serializers import UserSerializer, ItemsSerializer
from rest_framework.response import Response
from .models import CustomUser, ToDoItems
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterUser(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serialzer = UserSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.get(username=username)

        if user:
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid Password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class ToDoItemsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):

        if pk:
            item = ToDoItems.objects.get(id=pk)
            if item:
                serializer = ItemsSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            items = ToDoItems.objects.all()

            if items:
                serializer = ItemsSerializer(items, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'No Items found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user = request.user
        if not user:
            return Response({'message': 'Login Required'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['user'] = user.id

        serializer = ItemsSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'To-Do Item created Successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        item = ToDoItems.objects.get(id=pk)
        serializer = ItemsSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        item = ToDoItems.objects.get(id=pk)
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
