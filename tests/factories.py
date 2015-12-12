# -*- coding: utf-8 -*-

# Third Party Stuff
import factory
from django.conf import settings
from kyr.parliament.models import MemberOfParliament


class Factory(factory.DjangoModelFactory):

    class Meta:
        strategy = factory.CREATE_STRATEGY
        model = None
        abstract = True


class UserFactory(Factory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    email = factory.Sequence(lambda n: 'user%04d@email.com' % n)
    password = factory.PostGeneration(
        lambda obj, *args, **kwargs: obj.set_password('123123'))


class MPFactory(Factory):

    class Meta:
        model = MemberOfParliament

    name_of_the_mp = factory.Sequence(lambda n: 'test%04d' % n)


def create_user(**kwargs):
    "Create an user along with their dependencies"
    return UserFactory.create(**kwargs)


def create_mp(**kwargs):
    "create an MP with respective data"
    return MPFactory.create(**kwargs)
