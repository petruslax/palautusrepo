from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content + "\n")

        data = tomllib.loads(content)
        project_data = data["project"]
        dependency_groups = data.get("dependency-groups", {})
        
            
        #print(data)
        #print("\n")
        
        authors = [author["name"] for author in project_data.get("authors", [])]

        dependencies = [dep.split(">")[0] for dep in project_data.get("dependencies", [])]
        dependcy_dev = [dep.split(">")[0] for dep in dependency_groups.get("dev", [])]

        project = Project(
            project_data["name"],
            project_data.get("description"),
            project_data.get("license"),
            authors,
            dependencies,
            dependcy_dev
        )
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return project
