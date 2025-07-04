"""Main entry point
"""
from pyramid.config import Configurator
from cornice_swagger import CorniceSwagger
from cornice.service import get_services


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.include('cornice_swagger')

    my_generator = CorniceSwagger(get_services())
    my_spec = my_generator('MyAPI', '1.0.0')

    config.cornice_enable_openapi_view(
        api_path='/openapi/openapi.json',
        title='MyAPI',
        description="OpenAPI documentation",
        version='1.0.0',
    )
    config.cornice_enable_openapi_explorer(
        api_explorer_path='/openapi'
    )   

    config.scan("dummy.views")
    return config.make_wsgi_app()

