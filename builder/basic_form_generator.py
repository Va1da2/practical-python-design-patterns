"Basic form generator. First part of the builder pattern presentation."


def generate_webform(field_list):
    generate_fields = "\n".join(
        map(
            lambda x: f'{x}:<br><input type="txt" name={x}><br>', field_list
        )
    )

    return f"<form>{generate_fields}</form>"

if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    print(generate_webform(fields))