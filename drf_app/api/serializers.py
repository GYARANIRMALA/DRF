from rest_framework import serializers

from drf_app.models import Review, StreamPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ("id",)
        

# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name="stream-detail")

    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"







    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate(self, data):   # Object level validators
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should be Different!")
    #     else:
    #         return data
    

    # def validate_name(self, value):  # Field level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value










# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])   # Validators
#     description = serializers.CharField()
#     active = serializers.BooleanField()


#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):   # Object level validators
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be Different!")
#         else:
#             return data
        

#     # def validate_name(self, value):  # Field level validation
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return value