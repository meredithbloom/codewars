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
import typing

class ValidationError(Exception):
    pass

# ** kwargs is when you pass a name to the variable as you pass it into the function

class ValidationField:
    def __init__(self, default = None, blank=False, **kwargs):
        self.default = default
        self.blank = blank
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
            
    # test if input is string of min and max length. if not, return validation error
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
    def __init__(self, min_value = None, max_value = None, default = None, blank=False):
        # initializes parent class validation field
        super().__init__(**kwargs)
        
        # additional params specific to integer field
        self.min_value = min_value
        self.max_value = max_value

    # test if integer data type within min and max val constraints. if not, return validation error
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
    def __init__(self, default = None, blank = False):
        pass

    # test if true or false value, if not return validation error message
    def validate(self):
        pass

class DateTimeField(ValidationField):
    # needs date (day, month, year) and time
    def __init__(self, auto_new = False, default = None):
        self.auto_new = auto_new
    
    def validate(self):
        pass


class EmailField(ValidationField):
    # needs address, subdomain, domain - all strings of alphabetic chars with min and max length
    def __init__(self, blank = False, default = None):
        pass

    def validate(self):
        pass


class Model:
    pass