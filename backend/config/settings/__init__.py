import copy
import importlib
import operator
import os

empty = object()


def unpickle_lazyobject(wrapped):
    return wrapped


def new_method_proxy(func):
    def inner(self, *args):
        if self._wrapped is empty:
            self._setup()
        return func(self._wrapped, *args)
    return inner


class LazyObject:
    _wrapped = None

    def __init__(self):
        self._wrapped = empty

    __getattr__ = new_method_proxy(getattr)

    def __setattr__(self, name, value):
        if name == '_wrapped':
            self.__dict__['_wrapped'] = value
        else:
            if self._wrapped is empty:
                self._setup()
            setattr(self._wrapped, name, value)

    def __delattr__(self, name):
        if name == '_wrapped':
            raise TypeError('can\'t delete _wrapped.')
        if self._wrapped is empty:
            self._setup()
        delattr(self._wrapped, name)

    def _setup(self):
        raise NotImplementedError('subclasses of LazyObject must provide a _setup() method')

    def __reduce__(self):
        if self._wrapped is empty:
            self._setup()
        return unpickle_lazyobject, (self._wrapped,)

    def __copy__(self):
        if self._wrapped is empty:
            return type(self)()
        else:
            return copy.copy(self._wrapped)

    def __deepcopy__(self, memo):
        if self._wrapped is empty:
            result = type(self)()
            memo[id(self)] = result
            return result
        return copy.deepcopy(self._wrapped, memo)

    __bytes__ = new_method_proxy(bytes)
    __str__ = new_method_proxy(str)
    __bool__ = new_method_proxy(bool)

    __dir__ = new_method_proxy(dir)

    __class__ = property(new_method_proxy(operator.attrgetter('__class__')))
    __eq__ = new_method_proxy(operator.eq)
    __lt__ = new_method_proxy(operator.lt)
    __gt__ = new_method_proxy(operator.gt)
    __ne__ = new_method_proxy(operator.ne)
    __hash__ = new_method_proxy(hash)

    __getitem__ = new_method_proxy(operator.getitem)
    __setitem__ = new_method_proxy(operator.setitem)
    __delitem__ = new_method_proxy(operator.delitem)
    __iter__ = new_method_proxy(iter)
    __len__ = new_method_proxy(len)
    __contains__ = new_method_proxy(operator.contains)


class LazySettings(LazyObject):
    def _setup(self):
        self._wrapped = Settings()


class Settings:
    def __init__(self):
        settings_module = os.getenv('SETTINGS_MODULE')
        mod = importlib.import_module(settings_module)
        for config_key in dir(mod):
            if config_key.isupper():
                config_value = getattr(mod, config_key)
                setattr(self, config_key, config_value)


settings = LazySettings()
