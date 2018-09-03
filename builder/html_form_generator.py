"Generating stright HTML forms."

def generate_webform(text_fields, checkbox_fields):
    if text_fields:
        generated_fields = "\n".join(
            map(
                lambda x: f'{x}:<br><input type="txt" name={x}><br>', text_fields
            )
        )
    else:
        generated_fields = ""

    if checkbox_fields:
        generated_fields += "\n".join(
            map(
                lambda x: f'<label><input type="checkbox" id="{x}" value="{x}">{x}<br>', checkbox_fields
            )
        )

    return f"<form>{generated_fields}</form>"

def build_html_form(text_fields, checkbox_fields):
    with open("generated_form_with_checkbox_file.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(
                generate_webform(text_fields, checkbox_fields)
            )
        )

if __name__ == "__main__":
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    build_html_form(text_fields, checkbox_fields)