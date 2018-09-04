"OOP approach to generating forms."


class HtmlField(object):
    def __init__(self, **kwargs):
        self.html = ""

        if kwargs["field_type"] == "text_field":
            self._construct_text_field(kwargs["label"], kwargs["field_name"])
        elif kwargs["field_type"] == "checkbox":
            self._construct_checkbox(kwargs["field_id"], kwargs["value"], kwargs["label"])

    def _construct_text_field(self, label, field_name):
        self.html = f'{label}:<br><input type="text" name="{field_name}"><br>'

    def _construct_checkbox(self, field_id, value, label):
        self.html = f'<label><input type="checkbox" id="{field_id}" value="{value}"> {label}<br>'

    def __str__(self):
        return self.html

def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        try:
            generated_field_list.append(str(HtmlField(**field_dict)))
        except Exception as e:
            print(f"error: {e}")

    generated_fields = "\n".join(generated_field_list)

    return f'<form>{generated_fields}</form>'

def build_html_form(field_dict_list):
    with open("form_oop_approach.html", "w") as f:
        f.write(
            f"<html><body>{generate_webform(field_dict_list)}</body></html>"
        )

if __name__ == "__main__":
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
        }
    ]

    build_html_form(field_dict_list)