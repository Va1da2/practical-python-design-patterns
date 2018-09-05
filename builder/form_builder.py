"Html form builder with a Builder pattern."
from abc import ABCMeta, abstractmethod


class Director(object, metaclass=ABCMeta):

    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object

class AbstractFormBuilder(object, metaclass=ABCMeta):

    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass

class HtmlForm(object):

    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return f'<form>{"".join(self.field_list)}</form>'



class HtmlFormBuilder(AbstractFormBuilder):
    
    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict):
        label = field_dict["label"]
        field_name = field_dict["field_name"]

        self.constructed_object.field_list.append(
            f'{label}:<br><input type="text" name="{field_name}"><br>'
        )

    def add_checkbox(self, checkbox_dict):
        field_id = checkbox_dict["field_id"]
        value = checkbox_dict["value"]
        label = checkbox_dict["label"]

        self.constructed_object.field_list.append(
            f'<label><input type="checkbox" id="{field_id}" value="{value}">{label}<br>'
        )

    def add_button(self, button_dict):
        text = button_dict["text"]

        self.constructed_object.field_list.append(
            f'<button type="button">{text}</button>'
        )

class FormDirector(Director):

    def __init__(self):
        super().__init__()

    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)


if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)

    field_dict_list = [
        {
            "field_type": "text_field",
            "label": "Best text you have ever written",
            "field_name": "Field One"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": 1,
            "label": "Check for one"
        },
        {
            "field_type": "text_field",
            "label": "Another text field",
            "field_name": "Field Two"
        },
        {
            "field_type": "button",
            "text": "DONE"
        }
    ]

    director.construct(field_dict_list)

    with open("form_builder_dp_approach.html", "w") as f:
        f.write(
            "<html><body>{0!r}</body></html>".format(
                director.get_constructed_object()
            )
        )

