from rest_framework import serializers
from .models import Pet, Category, Tags

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name')

class PetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagsSerializer(many=True)

    class Meta:
        model = Pet
        fields = ('id', 'name', 'category', 'photoUrls', 'tags', 'status')

    def create(self, validated_data): 
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        tags_data = validated_data.pop('tags')
        tags = [Tags.objects.create(**tag) for tag in tags_data]
        pet = Pet.objects.create(category=category, **validated_data)
        pet.tags.set(tags)
        return pet
