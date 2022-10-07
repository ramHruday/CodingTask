import json


class CoffeeDeserializer:
    @classmethod
    def read(cls, filepath):
        f = open(filepath)
        data = json.load(f)
        return data

    @classmethod
    def json_to_list(cls, coffee_object):
        coffee_object = json.load(coffee_object)
        return [
            coffee_object.title,
            coffee_object.description,
            coffee_object.ingredients,
            coffee_object.image,
            coffee_object.id
        ]
