import sys
import os
import re
from settings import *

def render_template(template_file):
    if not template_file.endswith('.template'):
        print("Error: The file must have a .template extension.")
        return

    if not os.path.isfile(template_file):
        print(f"Error: File '{template_file}' does not exist.")
        return

    try:
        with open(template_file, 'r') as f:
            content = f.read()


        placeholders = re.findall(r"\{(.*?)\}", content)
        for placeholder in placeholders:
            if placeholder in globals():
                value = globals()[placeholder]
                content = content.replace(f"{{{placeholder}}}", value)
            else:
                print(f"Error: No value defined for placeholder '{placeholder}'.")
                return


        output_file = template_file.replace('.template', '.html')
        with open(output_file, 'w') as f:
            f.write(content)

        print(f"HTML file '{output_file}' successfully generated.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <file.template>")
    else:
        render_template(sys.argv[1])
