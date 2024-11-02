def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(
        getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(
        getattr(obj, method)) and not method.startswith("__")]
    module = getattr(obj, '__module__', None)
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }
    return info


class Example:
    def __init__(self):
        self.attribute1 = 10
        self.attribute2 = "Hello"

    def method1(self):
        return self.attribute1


obj = Example()
info = introspection_info(obj)
print(info)
