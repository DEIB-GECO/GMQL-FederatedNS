from rest_framework.relations import PrimaryKeyRelatedField

from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

class InstanceSerializer( serializers.ModelSerializer):

    password = serializers.CharField(max_length=255, write_only=True,style={'input_type': 'password'})
    creation_date = serializers.CharField(read_only=True)
    instancename=serializers.CharField(source='username')

    location  = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Instance
        fields = ( 'instancename', 'description', 'email', 'password', 'creation_date', 'location')

    def create(self, validated_data):

        user = get_user_model().objects.create_user(validated_data['description'],
                                  validated_data['username'],
                                  validated_data['email'],
                                  validated_data['password'])

        return user

    def get_location(self, obj):
        try:
         return '{}'.format(obj.username)
        except:
         return None

class CurrentInstanceSerializer( InstanceSerializer):

    token = serializers.SerializerMethodField()
    instancename = serializers.CharField(source='username')

    class Meta:
        model = Instance
        fields = ( 'instancename', 'description', 'email', 'password', 'creation_date', 'location', 'token')


    def get_token(self, obj):

        token = Token.objects.get(user=obj)
        return  token.key


class GroupSerializer(serializers.ModelSerializer):

    identifier = serializers.SerializerMethodField()

    instances = serializers.SlugRelatedField(
        many=True,
        queryset=Instance.objects.all(),
        #read_only=True,
        slug_field='username'
    )

    def get_identifier(self, obj):
        return obj.name

    class Meta:
        model = Group
        fields = ('identifier', 'name', 'owner', 'instances')


class LocationSerializer(serializers.ModelSerializer):

    #identifier = serializers.SerializerMethodField()

    #def get_identifier(self, obj):
        #return '{}.{}'.format(obj.instance.username, obj.name)
        #return '{}'.format(obj.instance.username)

    def create(self, validated_data):

        r = super(LocationSerializer, self).create(validated_data)
        res = Location.objects.filter(name=validated_data['name']).first()
        res.checkAlive()
        return r

    def update(self, instance, validated_data):
        r = super(LocationSerializer, self).update(instance, validated_data)
        instance.checkAlive()
        return r


    class Meta:
        model = Location
        fields = ('instance', 'name', 'details', 'URI', 'alive')
        read_only_fields = ('instance', 'alive')


class DatasetSerializer(serializers.ModelSerializer):

    identifier = serializers.SerializerMethodField()

    copies = serializers.SlugRelatedField(
        many=True,
        queryset=Instance.objects.all(),
        #read_only=True,
        slug_field='username'
    )
    allowed_to = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        #read_only=True,
        slug_field='name'
    )
    pub_date = serializers.CharField(read_only=True)

    def get_identifier(self, obj):
        return '{}.{}'.format(obj.owner_id, obj.name)

    def create(self, validated_data):

        allowed_to = validated_data["allowed_to"]

        # Check if the dataset is visible to the copies
        if not "GMQL-ALL" in map(lambda group: group.name, allowed_to):
            copies = validated_data["copies"]
            allowed_instances = []
            for gp in allowed_to:
                allowed_instances += Group.objects.get(name=gp.name).instances.all()
            if not set(copies).issubset(set(allowed_instances)):
                error = {'message': 'The dataset must be visible to all hosting repositories.'}
                raise serializers.ValidationError(error)

        return super(DatasetSerializer, self).create(validated_data)

    def update(self, instance, validated_data):

        allowed_to = validated_data["allowed_to"]

        # Check if the dataset is visible to the copies
        if not "GMQL-ALL" in map(lambda group: group.name, allowed_to):
            copies = validated_data["copies"]
            allowed_instances = []
            for gp in allowed_to:
                allowed_instances += Group.objects.get(name=gp.name).instances.all()
            if not set(copies).issubset(set(allowed_instances)):
                error = {'message': 'The dataset must be visible to all hosting repositories.'}
                raise serializers.ValidationError(error)

        return super(DatasetSerializer, self).update(instance, validated_data)

    class Meta:
        model = Dataset
        fields = ('identifier', 'name', 'owner', 'author', 'description', 'pub_date', 'copies', 'allowed_to')

class AuthenticationSerializer(serializers.ModelSerializer):

    identifier = serializers.SerializerMethodField()

    def get_identifier(self, obj):
        return '{}_{}'.format(obj.client.username, obj.target.username)

    class Meta:
        model = Authentication
        fields = ('identifier', 'client', 'target', 'token', 'expiration')