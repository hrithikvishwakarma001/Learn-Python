from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mongo_connection import db
from .models import MenuItem
@api_view(['GET'])
def get_menu_items_api(request):
    menu_collection = db["menu"]  
    menu_items = menu_collection.find()
    serialized_menu_items = [
        {
            "id": str(item["_id"]), # Convert ObjectId to string
            "name": item["name"],
            "price": item["price"],
            "availability": item["availability"],
        }
        for item in menu_items
    ]
    return Response(serialized_menu_items)


@api_view(['POST'])
def create_menu_item(request):
    data = request.data
    menu_item = {
        'name': data['name'],
        'price': data['price'],
        'availability': data['availability']
    }
    db.menu.insert_one(menu_item)
    return Response({'message': 'Menu item created successfully'})