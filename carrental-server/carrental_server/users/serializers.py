from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    Fields that will get serialized.
    """
    email = serializers.EmailField(required=True)
    # username = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8, write_only=True)
    first_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=True)
    license_number = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(allow_null=False, required=False)
    phone_number = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    class Meta:
        """
        Uses NewUser model

        Validates data to ensure all required fields are provided.
        Sets password to write_only so that it may be used when updating or creating an instance,
        but is not included when serializing the representation.
        """
        model = NewUser
        fields = ('email', 'password', 'first_name', 'middle_name', 'last_name', 'license_number',
                  'date_of_birth', 'phone_number', 'address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Sets password if it is not None.
        Returns the serialized data given validated data.
        """
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
