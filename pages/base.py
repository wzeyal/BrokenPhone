import abc

import dash


class BasePage(metaclass=abc.ABCMeta):
    def __init__(self, path="/"):
        dash.register_page(self.get_module_name(), path=path)

    # def get_class_name(self):
    #     return type(self).__name__

    def get_module_name(self):
        return f"{type(self).__module__}"
