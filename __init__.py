from airflow.operators.docker_operator import DockerOperator
from airflow.plugins_manager import AirflowPlugin


class DockerExOperator(DockerOperator):
    template_fields = DockerOperator.template_fields + ('volumes',)


class DockerExPlugin(AirflowPlugin):
    name = "dockerex_plugin"
    hooks = []
    operators = [DockerExOperator]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
