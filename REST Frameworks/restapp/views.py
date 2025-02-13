from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProductView(APIView):
    
    def get(self,request):
        data=Product.objects.all()
        
        selected_serializer=Application_serializer(data,many=True).data
       
        
        # list_data=[]
        
        # for product in data:
            
        #     selected_product={
        #         'id':product.id,
        #         'product_name':product.product_name,
        #         'product_code':product.product_code,
        #         'price':product.price,
        #         'gst':product.gst
        #     }
        #     list_data.append(selected_product)
        return Response(selected_serializer)
    
    def post(self,request):
        
        #print(request.data)
        new_data=Product(product_name=request.data['product_name'],product_code=request.data['product_code'],price=request.data['price'],gst=request.data["gst"])
        
        new_data.save()
        
        return Response('Data is added successfully!')
        
class GetDataById(APIView):
    
    def get(self,request,id):
        
        product=Product.objects.get(id=id)
        
        list1=[]
        
        selected_product={
                'id':product.id,
                'product_name':product.product_name,
                'product_code':product.product_code,
                'price':product.price,
                'gst':product.gst
            }
        
        list1.append(selected_product)
        return Response(list1)
    
    def patch(self,request,id):
        
        data2=Product.objects.filter(id=id)
        
        data2.update(product_name=request.data['product_name'],product_code=request.data['product_code'],price=request.data['price'],gst=request.data["gst"])
        
        return Response('Updated Successfully')
    
    def delete(self,request,id):
        
        data3=Product.objects.get(id=id)
        
        data3.delete()
        
        return Response("Deleted Successfully")
    

        
       
         
         
    