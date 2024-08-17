# pseudo charfield
# Why is it that calling `ShortCode.code` returns the `CharField` class
# but in Django, it returns a deferred attribute?


class ModelBase(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)


class Model(metaclass=ModelBase):
    # Some Django magic code
    ...


class CharField:
    def __init__(self, max_length, null=False, blank=False, default=None):
        self.max_length = max_length
        self.null = null
        self.blank = blank
        self.default = default


class ShortCode(Model):
    code = CharField(max_length=8, default=lambda: "some random string")
    ...


print(f"{ShortCode.code=}")

sc = ShortCode()
print(f"{sc.code=}")  # why do I receive something different here compared to Django?
