from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Companies, Side, Seekers



class CompanyNode(DjangoObjectType):
    class Meta:
        model = Companies
        filter_fields = [
            "name",
            #"seekers"
        ]
        interfaces = (relay.Node, )


class SideNode(DjangoObjectType):
    class Meta:
        model = Side
        filter_fields = [
            'name'
        ]
        interfaces = (relay.Node, )


class SeekerType(DjangoObjectType):
    class Meta:
        model = Seekers
        filter_fields = {
            "seeker": ['exact'],
            "seeker__name": ['exact']
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    companies = relay.Node.Field(CompanyNode)
    #all_companies = DjangoFilterConnectionField(CompanyNode,)

    seekers = relay.Node.Field(SeekerType)
    #all_seekers = DjangoFilterConnectionField(SeekerType)
