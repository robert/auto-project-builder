import string
import os
from jinja2 import Template

MIN_PROJECT_NAME_LENGTH = 2
MAX_PROJECT_NAME_LENGTH = 20
LEGAL_PROJECT_NAME_CHARS = (
    list(string.ascii_lowercase) +
    list(string.ascii_uppercase) +
    [str(x) for x in range(0, 10)] +
    ['-', '_']
)

def is_valid_project_name(project_name):
    illegal_chars  = []
    for ch in project_name:
        if ch not in LEGAL_PROJECT_NAME_CHARS:
            return False

    if len(project_name) < MIN_PROJECT_NAME_LENGTH:
        return False

    if len(project_name) > MAX_PROJECT_NAME_LENGTH:
        return False

    return True


def is_valid_author_name(author_name):
    if len(author_name) == 0:
        return False
    return True


def write_file_from_template(template_path, output_path, params):
    with open(template_path, mode='r') as f:
        template_string = f.read()
    
    template = Template(template_string)
    contents = template.render(params)

    with open(output_path, 'w') as f:
        f.write(contents)


if __name__ == "__main__":
    while True:
        project_name = input("What is the name of your project?\n")

        # Bonus points for returning a string/array of errors
        #
        # TODO: check if project already exists
        if is_valid_project_name(project_name):
            break
        else:
            print("Invalid project name!")

    while True:
        author_name = input("Who is the author of this project?\n")

        if is_valid_author_name(author_name):
            break
        else:
            print("Invalid author name!")

    output_dir_path = os.path.join("..", project_name)
    os.mkdir(output_dir_path)
    print("Created directory at %s" % output_dir_path)

    readme_output_path = os.path.join(output_dir_path, "README.md")
    write_file_from_template(
        template_path="templates/README.md.template",
        output_path=readme_output_path,
        params={
            'project_name': project_name,
            'author_name': author_name,
        }
    )
    print("Created README at %s" % readme_output_path)

    todo_output_path = os.path.join(output_dir_path, "TODO.md")
    write_file_from_template(
        template_path="templates/TODO.md.template",
        output_path=todo_output_path,
        params={
            'project_name': project_name,
            'author_name': author_name,
        }
    )
    print("Created TODO.md at %s" % todo_output_path)

    main_output_path = os.path.join(output_dir_path, "main.py")
    write_file_from_template(
        template_path="templates/main.py.template",
        output_path=main_output_path,
        params={'project_name': project_name},
    )
    print("Created main.py at %s" % main_output_path)

    print("Done!")
