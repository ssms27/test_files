
import yaml
from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
t = ENV.get_template("test.j2")

location = ['DR', 'PROD']

with open('test.yml') as f:
	r = yaml.load(f)

for i in location:
	print(t.render(ntp=r['Juniper'][i]['ntp']))
