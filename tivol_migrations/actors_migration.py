from tivol.base_classes.mappers import JsonMapper
from dummyapp.models import Actor
from tivol.base_classes.migration_handler_base import MigrationHandlerBase
import os
from tivol.base_classes.plugins import DatePlugin


class ActorMigration(MigrationHandlerBase):

    def init_metadata(self):
        json_mapper = JsonMapper()
        json_mapper.set_destination_file(path=os.path.join(os.getcwd(), 'dummyapp', 'tivol_migrations', 'source_files', 'actors.json'))

        self.id = 'actor'
        self.name = 'Actor migration'
        self.description = 'Migrating actors to the DB'
        self.add_source_mapper(json_mapper)
        self.set_model_target(Actor)
        self.fields_plugins = {
            'birth_date': [{'plugin': DatePlugin, 'extra_info': {'format': '%B %d, %Y'}}]
        }
