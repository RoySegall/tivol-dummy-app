from tivol.base_classes.mappers import SqlMapper
from dummyapp.models import Tag
from tivol.base_classes.migration_handler_base import MigrationHandlerBase


class TagMigration(MigrationHandlerBase):

    def init_metadata(self):
        mysql_mapper = SqlMapper()
        mysql_mapper.set_connection('other_site')
        mysql_mapper.set_table('tags')

        self.id = 'tag'
        self.name = 'Tags migration'
        self.description = 'Migrating tags into the system'
        self.add_source_mapper(mysql_mapper)
        self.set_model_target(Tag)
