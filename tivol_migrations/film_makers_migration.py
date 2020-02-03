from tivol.base_classes.plugins import DatePlugin
from tivol.base_classes.mappers import RestMapper
from dummyapp.models import Filmmaker
from tivol.base_classes.migration_handler_base import MigrationHandlerBase


class FilmMakerMigration(MigrationHandlerBase):

    def init_metadata(self):
        rest_mapper = RestMapper()
        rest_mapper.set_address('http://localhost:8000/dummy/rest')

        self.id = 'film_maker'
        self.name = 'Film makers migration'
        self.description = 'Migrating film makers into the system'
        self.add_source_mapper(rest_mapper)
        self.set_model_target(Filmmaker)

        self.fields_plugins = {
            'active_since': [{'plugin': DatePlugin, 'extra_info': {'format': '%Y'}}]
        }
