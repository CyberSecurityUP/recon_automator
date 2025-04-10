from jinja2 import Template
import os

def generate_html_report(results):
    with open("templates/report_template.html") as f:
        template = Template(f.read())

    html_output = template.render(results=results)

    os.makedirs("output", exist_ok=True)
    with open("output/target_report.html", "w") as f:
        f.write(html_output)
