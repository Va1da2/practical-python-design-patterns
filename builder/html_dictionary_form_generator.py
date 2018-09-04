"Generating stright HTML forms from input dictionary."


def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            generated_field_list.append(
                f'{field_dict["label"]}:<br><input type="text" name="{field_dict["name"]}"><br>'
            )

        if field_dict["type"] == "checkbox":
            generated_field_list.append(
                f'<label><input type="checkbox" id="{field_dict["id"]}" value="{field_dict["value"]}">{field_dict["label"]}<br>'
            )

    generated_fields = "\n".join(generated_field_list)

    return f"<form>{generated_fields}</forms>"

def build_html_form(field_dict_list):
    with open("form_from_dict_file.html", "w") as f:
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