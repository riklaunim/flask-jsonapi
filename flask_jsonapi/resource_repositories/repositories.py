from contextlib import contextmanager

from flask_jsonapi import exceptions


class ResourceRepository:
    def create(self, data, **kwargs):
        raise exceptions.NotImplementedMethod('Creating is not implemented.')

    def get_list(self, filters=None):
        raise exceptions.NotImplementedMethod('Getting list is not implemented.')

    def get_detail(self, id):
        raise exceptions.NotImplementedMethod('Getting object is not implemented.')

    def delete(self, id):
        raise exceptions.NotImplementedMethod('Deleting is not implemented')

    def update(self, id, **data):
        raise exceptions.NotImplementedMethod('Updating is not implemented')

    @contextmanager
    def begin_transaction(self):
        yield