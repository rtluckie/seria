from seria.utils import str_to_num, set_defaults
import pytest


class TestSeriaUtils(object):
#     def test_set_default_add(self):
#         kwargs = {"arg1": True}
#         defaults = {"arg2": True}
#         combined = dict(kwargs.items() + defaults.items())
#         set_defaults(kwargs, defaults)
#         assert kwargs == combined
#
    def test_set_default_dont_overide(self):
        kwargs = {"arg1": False}
        defaults = {"arg1": True}
        set_defaults(kwargs, defaults)
        assert kwargs == {"arg1": False}