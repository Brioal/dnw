from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.parsers import JSONParser

from items.models import Item, Step, Item_Product, Item_Instrument
from items.serializers import ItemSerializer, StepSerializer, ItemProductSerializer, ItemInstrumentSerializer
from product.models import Product, Instrument


def testone(request):
    return render(request, "items/addItems.html")

@csrf_exempt
def item_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        # create item
        item = Item()
        item_data = {}
        item_data['item_name'] = data['item_name']
        item_data['item_price'] = data['item_price']
        item_data['frequency'] = data['frequency']
        item_data['classify'] = data['classify']
        serializer = ItemSerializer(item, data=item_data)
        if serializer.is_valid():
            serializer.save()
            item_id = item.id
            # create step
            step_list = data['steps']
            for step_val in step_list:
                step = Step()
                step_data = step_val
                step_data['belong_item'] = item_id
                serializer = StepSerializer(step, step_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return JsonResponse(serializer.errors, status=400)
            product_list = data['product']
            for product_val in product_list:
                item_product = Item_Product()
                product_data = product_val
                product_data['item'] = item_id
                product_data['product'] = Product.objects.get(name=product_data['name']).id
                serializer = ItemProductSerializer(item_product, product_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return JsonResponse(serializer.errors, status=400)
            instrument_list = data['instrument']
            for instrument_val in instrument_list:
                item_instrument = Item_Instrument()
                instrument_data = instrument_val
                instrument_data['item'] = item_id
                instrument_data['instrument'] = Instrument.objects.get(name=instrument_data['name']).id
                serializer = ItemInstrumentSerializer(item_instrument, instrument_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return JsonResponse(serializer.errors, status=400)
            return JsonResponse({"text": "success"})
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def step_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        step = Step()
        serializer = StepSerializer(step, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)