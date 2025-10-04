from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView



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




@api_view(http_method_names=["GET","POST"])
def list_posts(request: Request):
    posts=Post.objects.all()
    
    
    if request.method=="POST":
        data=request.data
        
        serializer=PostSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()  # saves the data to the database
            response={"message":"post created successfully","data":serializer.data}
            return Response(data=response,status=status.HTTP_201_CREATED)
    
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    serializer=PostSerializer(instance=posts,many=True)  # here many=True is used to serialize multiple objects
    
    
    response={"message":"list of posts","data":serializer.data}   # format the response in this way
    
    
    return Response(data=response,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request: Request,post_index:int):
    
    post=posts[post_index]
    
    if post:
        return Response(data=post,status=status.HTTP_200_OK)
    
    return Response(data={"message":"post not found"},status=status.HTTP_404_NOT_FOUND)
    