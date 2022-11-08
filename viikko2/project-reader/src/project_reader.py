from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        cont = toml.loads(content)
        
        name = cont['tool']['poetry']['name']
        description = cont['tool']['poetry']['description']
        dependencies = [key for key in cont['tool']['poetry']['dependencies']]
        devdependencies = [key for key in cont['tool']['poetry']['dev-dependencies']]
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, devdependencies)
