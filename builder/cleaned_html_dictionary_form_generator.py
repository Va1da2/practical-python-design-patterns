"Cleaned htnl form generator from dictionary."


def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            field_html = generate_text_field(field_dict)
        elif field_dict["type"] == "checkbox":
            field_html = generate_checkbox(field_dict)

        generated_field_list.append(field_html)

    generated_fields = "\n".join(generated_field_list)

    return f"<form>{generated_fields}</form>"

def generate_text_field(text_field_dict):
    return f'{text_field_dict["label"]}:<br><input type="text" name="{text_field_dict["name"]}"><br>'

def generate_checkbox(checkbox_dict):
    return f"""<label><input type="checkbox" id="{checkbox_dict["id"]}" 
            value="{checkbox_dict["value"]}"> {checkbox_dict["label"]}<br>"""

def build_html_form(field_dict_list):
    with open("form_from_cleaned_dict_file.html", "w") as f:
        f.write(
            f"<html><body>{generate_webform(field_dict_list)}</body></html>"
        )

if __name__ == "__main__":
    field_dict_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text"
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "value": 1,
            "label": "Check for one"
        },
        {
            "type": "text_field",
            "label": "Another text field",
            "name": "text_field_2"
        }
    ]

    build_html_form(field_dict_list)