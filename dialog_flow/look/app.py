import falcon

from .images import ImageStore, Resource


def create_app(image_store):
    image_resource = Resource(image_store)
    api = falcon.API()
    api.add_route('/images', image_resource)
    return api

def get_app():
    image_store = ImageStore('.')
    return create_app(image_store)