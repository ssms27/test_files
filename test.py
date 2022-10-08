#!/Users/ssms27/venv/bin/python3
import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ENV = Environment(loader=FileSystemLoader('.'))
t = ENV.get_template("test.j2")

location = ['DR', 'PROD']
r = yaml.safe_load(Path("test.yml").read_text())

for i in location:
	print(t.render(ntp=r['Juniper'][i]['ntp']))
