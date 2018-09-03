"Generating stright HTML forms."

def generate_webform(field_list):
    generate_fields = "\n".join(
        map(
            lambda x: f'{x}:<br><input type="txt" name={x}><br>', field_list
        )
    )

    return f"<form>{generate_fields}</form>"

def build_html_form(fields):
    with open("generated_form_file.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(generate_webform(fields))
        )

if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    build_html_form(fields)