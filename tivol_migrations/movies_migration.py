from dummyapp.models import Movie, Director
from tivol.base_classes.mappers import CsvMapper
from tivol.base_classes.migration_handler_base import MigrationHandlerBase
from tivol.base_classes.plugins import ReferencePlugin
import os


class MoviesMigration(MigrationHandlerBase):

    def init_metadata(self):
        csv_mapper = CsvMapper()
        csv_mapper.set_destination_file(path=os.path.join(os.getcwd(), 'dummyapp', 'tivol_migrations', 'source_files', 'movies.csv'))

        self.id = 'movie'
        self.name = 'Movie migration'
        self.description = 'Migrating movies into the system'
        self.add_source_mapper(csv_mapper)
        self.set_model_target(Movie)

        self.fields_plugins = {
            'director': [{'plugin': ReferencePlugin, 'extra_info': {'model': Director}}],
        }
