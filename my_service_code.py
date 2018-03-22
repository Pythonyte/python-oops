class GenericSimpleView(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs.get('payload')
        self.instance = kwargs.get('instance')
        self.request = kwargs.get('request') # not request method

    @classmethod
    def call(cls, **kwargs):
        self = cls(**kwargs)
        self.display()

    def display(self):
        import pdb;pdb.set_trace()

class TestService(GenericSimpleView):
    pass

def call_service():
    payload = {'field':'value'}
    instance = 'model instance'
    request = 'api request'
    service_class = TestService

    service_class.call(payload=payload, request=request)
    # service_class.call(payload=payload, instance=instance, request=request)

call_service()