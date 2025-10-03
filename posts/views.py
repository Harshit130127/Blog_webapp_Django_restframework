from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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




@api_view(http_method_names=["GET"])
def list_posts(request: Request):

    return Response(data=posts,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request: Request,post_index:int):
    post=posts[post_index]
    
    if post:
        return Response(data=post,status=status.HTTP_200_OK)
    
    return Response(data={"message":"post not found"},status=status.HTTP_404_NOT_FOUND)
    