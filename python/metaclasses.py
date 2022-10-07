# Metaclasses - Simple Django Models - 3 kyu

# Django is a famous back-end framework written in Python. It has a vast list of features including the creation of database tables through "models". You can see an example of such model below:

# class Person(models.Model):
#     first_name = models.CharField()
#     last_name = models.CharField()


# Apart from creating a table it can perform validation, generate HTML forms, and so on. This is possible thanks to metaclasses. Normally there are better solutions than using metaclasses, but they can be of great help in creating powerful framework interfaces. This goal of this kata is to learn and understand how such frameworks works.

# Your task is to implement a class Model and classes for its fields to support functionality like in the following example:

# class User(Model):
#     first_name = CharField(max_length=30)
#     last_name = CharField(max_length=50)
#     email = EmailField()
#     is_verified = BooleanField(default=False)
#     date_joined = DateTimeField(auto_now=True)
#     age = IntegerField(min_value=5, max_value=120, blank=True)


# user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
# user1.validate()

# print(user1.date_joined)  # prints date and time when the instance was created
# print(user1.is_verified)  # prints False (default value)

# user1.age = 256
# user1.validate()  # raises ValidationError - age is out of range

# user2 = User()
# user2.validate()  # raises ValidationError - first three fields are missing and mandatory


# The classes which inherit from Model should:

# support creation of fields using class-attribute syntax
# have a validate method which checks whether all fields are valid
# The field types which you should implement are:

# CharField - a string with min_length (default 0) and max_length (default None) parameters
# IntegerField - an integer with min_value (default None) and max_value (default None) parameters
# BooleanField - a boolean
# DateTimeField - a datetime with auto_now (default False) parameters which determines whether the current time should be set automatically on creation
# EmailField - a string in the format of address@subdomain.domain where address, subdomain, and domain are sequences of alphabetical characters with min_length (default 0) and max_length (default None) parameters
# Also, each field type has parameters blank (default False) which determines whether None is allowed as a value, and default (default None) which determines the value to be used if nothing was provided.

# Each field type should have its own validate method which checks whether the provided value has the correct type and satisfies the length/value constraints.

# Notes
# min_value/max_value and min_length/max_length bounds are inclusive
# if DateTimeField's auto_now flag is set to True, and no default value is specified, accessing its default attribute should always yield current time.

import datetime
import re
from typing import Any

class ValidationError(Exception):
    pass

# ** kwargs is when you pass a name to the variable as you pass it into the function

class ValidationField:
    def __init__(self, default = None, blank=False, **kwargs):
        self.default = default
        self.blank = blank
        # will hash keyword -> values to instance dict
        self.__dict__.update(**kwargs)

    # if there has to be a value set and there is no val, return validation error
    def validate(self, val):
        if val is None and self.blank is False:
            raise ValidationError


class CharField(ValidationField):
    def __init__(self, min_length = 0, max_length = None, **kwargs):
        # initializes parent class validation field
        super().__init__(**kwargs)
        # additional parameters specific to char field
        self.min_length = min_length
        self.max_length = max_length
            
    def validate(self, val):
        # checks if blank is true or false
        super().validate(val)
        if val is None:
            return
        # checks if string
        if not isinstance(val, str):
            raise ValidationError
        # if less than min length
        if self.min_length is not None and len(val) < self.min_length:
            raise ValidationError
        # if greater than max length
        if self.max_length is not None and self.max_length < len(val):
            raise ValidationError
        

class IntegerField(ValidationField):
    def __init__(self, min_value = None, max_value = None, **kwargs):
        # initializes parent class validation field
        super().__init__(**kwargs)
        # additional params specific to integer field
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, val):
        # checks if blank true or false
        super().validate(val)
        if val is None:
            return
        # checks if integer
        if not isinstance(val, int):
            raise ValidationError
        # checks if less than min val
        if self.min_value is not None and val < self.min_value:
            raise ValidationError
        # checks if greater than max val
        if self.max_value is not None and self.max_value < val:
            raise ValidationError


class BooleanField(ValidationField):
    # either true or false
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # test if true or false value, if not return validation error message
    def validate(self, val):
        # checks if blank is true or false
        super().validate(val)
        if val is None:
            return
        # check if boolean data type
        if not isinstance(val, bool):
            raise ValidationError
        

class DateTimeField(ValidationField):
    # needs date (day, month, year) and time
    def __init__(self, default = None, auto_now = False, **kwargs):
        # initialize parent class validation field
        super().__init__(**kwargs)
        # datetime specific params
        self.auto_now = auto_now
        # adds extra _ before default to separate from parent class default attribute
        self._default = default
    
    def __getattribute__(self, name: str) -> Any:
        if name == 'default':
            if self._default is None and self.auto_now is True:
                return datetime.datetime.now()
            else:
                return self._default
        return super().__getattribute__(name)
    
    def validate(self, val):
        # check if blank is true or false
        super().validate(val)
        if val is None:
            return
        # checks if datetime object
        if not isinstance(val, datetime.datetime):
            raise ValidationError


class EmailField(ValidationField):
    # needs address, subdomain, domain - all strings of alphabetic chars with min and max length
    def __init__(self, min_length = 0, max_length = None, **kwargs):
        # initialize parent class validation field
        super().__init__(**kwargs)
        # email address specific params
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, val):
        super().validate(val)
        
        if val is None:
            return
        # check if string data type
        if not isinstance(val, str):
            raise ValidationError
        # need to check if min/max length compliant, and match email regex
        if self.min_length is not None and len(val) < self.min_length:
            raise ValidationError
        
        if self.max_length is not None and self.max_length < len(val):
            raise ValidationError

        if not re.match(r"[^@]+@[^@]+\.[^@]+", val):
            raise ValidationError

class Model:
    def __init__(self, **kwargs):
        # iterating through directory of class methods searching for public methods
        for i in [i for i in dir(self.__class__) if i.startswith('_f_')]:
            # pulling attribute from public method
            attribute = getattr(self.__class__,i)
            # assigning attribute
            setattr(self, i[3:], attribute.default)
        
        # sets keyword -> value pairs as attributes of class instance/object
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    # altering behavior of future sub classes of Model to ensure relevant attributes are deemed public methods   
    def __init_subclass__(cls) -> None:
        for i in [i for i in dir(cls) if not i.startswith('_')]:
            attribute = getattr(cls, i)
            # if attribute is any of the above defined classes
            if isinstance(attribute, (CharField, IntegerField, BooleanField, DateTimeField, EmailField)):
                delattr(cls, i)
                # resetting attribute as public method
                setattr(cls, '_f_'+i, attribute)
        super().__init_subclass__()
        
    def validate(self):
        # if both a public method and one of the special validation ones
        for i in [i for i in dir(self.__class__) if i.startswith('_f_') and hasattr(self, i[3:])]:
            class_attribute = getattr(self.__class__, i)
            instance_attribute = getattr(self, i[3:])
            class_attribute.validate(instance_attribute)