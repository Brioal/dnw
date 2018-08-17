from rest_framework import serializers

from .models import Item, Step, Item_Product, Item_Instrument


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class ItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Product
        fields = '__all__'


class ItemInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Instrument
        fields = '__all__'