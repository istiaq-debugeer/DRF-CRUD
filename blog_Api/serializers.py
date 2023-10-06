from rest_framework import serializers
from blog.models import Post
from blog_Api.models import Student

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','title','excerpt','content','status','author')



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    # name = serializers.CharField(max_length=50)
    # Department = serializers.CharField(max_length=50)
    # City = serializers.CharField(max_length=30)
    # phone_number = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name),
        instance.Department=validated_data.get('Department',instance.Department),
        instance.City=validated_data.get('City',instance.City),
        # instance.phone_number=validated_data.get('phone_number',instance.phone_number),
        # instance.Division=validated_data.get('Division',instance.Division),

        instance.save()

        return instance
