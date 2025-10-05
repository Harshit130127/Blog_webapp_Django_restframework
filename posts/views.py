from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

posts=[
    {"id":1,"title":"First Post","content":"This is the content of the first post."},
    {"id":2,"title":"Second Post","content":"This is the content of the second post."},
    {"id":3,"title":"Third Post","content":"This is the content of the third post."}
]






@api_view(http_method_names=["GET","POST"])
def homepage(request: Request):
    

    if request.method=="POST":
        data=request.data
        response={"message":"this is homepage","data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)
        
    response={"message":"this is homepage"}
    return Response(data=response,status=status.HTTP_200_OK)



# ...............this is without using generic and class views.................
# @api_view(http_method_names=["GET","POST"])
# def list_posts(request: Request):
#     posts=Post.objects.all()
    
    
#     if request.method=="POST":
#         data=request.data
        
#         serializer=PostSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()  # saves the data to the database
#             response={"message":"post created successfully","data":serializer.data}
#             return Response(data=response,status=status.HTTP_201_CREATED)
    
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     serializer=PostSerializer(instance=posts,many=True)  # here many=True is used to serialize multiple objects
    
    
#     response={"message":"list of posts","data":serializer.data}   # format the response in this way
    
    
#     return Response(data=response,status=status.HTTP_200_OK)

# .......................this is using class based views...................
'''class PostListCreateView(APIView):
    
    def get(self,request: Request):  # to list all posts
        posts=Post.objects.all()
        serializer=PostSerializer(instance=posts,many=True)  # here many=True is used to serialize multiple objects
        response={"message":"list of posts","data":serializer.data}   # format the response in this way
        return Response(data=response,status=status.HTTP_200_OK)
    
    def post(self,request: Request):   # to create a new post
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # saves the data to the database
            response={"message":"post created successfully","data":serializer.data}
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

'''
# ...................this is without using generic and class views.................

# @api_view(http_method_names=["GET"])
# def post_detail(request: Request,post_index:int):
    
#     post=get_object_or_404(Post,pk=post_index)  # fetch the post with the given post_index or return 404 if not found
    
#     serializer=PostSerializer(instance=post)  # serialize the post object
    
    
#     response={"message":"post details","data":serializer.data}   # format the response in this way
#     return Response(data=response,status=status.HTTP_404_NOT_FOUND)   # return 404 if post not found
    



# @api_view(http_method_names=["PUT"])
# def update_post(request: Request,post_index:int):
#     post=get_object_or_404(Post,pk=post_index)  # fetch the post with the given post_index or return 404 if not found
    
#     data=request.data
    
#     serializer=PostSerializer(instance=post,data=data)  # serialize the post object with the new data
    
#     if serializer.is_valid():
#         serializer.save()  # saves the updated data to the database
#         response={"message":"post updated successfully","data":serializer.data}
#         return Response(data=response,status=status.HTTP_200_OK)
    
#     return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=["DELETE"])
# def delete_post(request: Request,post_index:int):
#     post=get_object_or_404(Post,pk=post_index)  # fetch the post with the given post_index or return 404 if not found
    
#     post.delete()  # delete the post from the database
    
#     response={"message":"post deleted successfully"}
#     return Response(data=response,status=status.HTTP_200_OK)



# ...................this is using class based views.................

'''class PostRetrieveUpdateDeleteView(APIView):
    
    serializer_class=PostSerializer
    def get(self,request: Request,pk:int):  # to retrieve a post by id
        post=get_object_or_404(Post,pk=pk)  # fetch the post with the given post_index or return 404 if not found
        serializer=PostSerializer(instance=post)  # serialize the post object
        response={"message":"post details","data":serializer.data}   # format the response in this way
        return Response(data=response,status=status.HTTP_200_OK)   # return 200 if post found
    
    def put(self,request: Request,pk:int):  # to update a post by id
        post=get_object_or_404(Post,pk=pk)  # fetch the post with the given post_index or return 404 if not found
        data=request.data
        serializer=PostSerializer(instance=post,data=data)  # serialize the post object with the new data
        if serializer.is_valid():
            serializer.save()  # saves the updated data to the database
            response={"message":"post updated successfully","data":serializer.data}
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request: Request,pk:int):  # to delete a post by id
        post=get_object_or_404(Post,pk=pk)  # fetch the post with the given post_index or return 404 if not found
        post.delete()  # delete the post from the database
        response={"message":"post deleted successfully"}
        return Response(data=response,status=status.HTTP_200_OK) '''
        
        
        
        
# ...................this is using generic class based views.................

class PostListCreateView(generics.GenericAPIView,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    
    def get(self,request: Request, *args, **kwargs):
        return self.list(request)  # to list all posts
    
    
    def post(self,request: Request, *args, **kwargs):
        return self.create(request)  # to create a new post
    
    
class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin):
    
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    
    def get(self,request: Request, *args, **kwargs):
        return self.retrieve(request)  # to retrieve a post by id
    
    
    def put(self,request: Request, *args, **kwargs):
        return self.update(request)  # to update a post by id
    
    
    def delete(self,request: Request, *args, **kwargs):
        return self.destroy(request)  # to delete a post by id