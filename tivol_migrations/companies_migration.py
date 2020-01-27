from dummyapp.models import Company
from tivol.base_classes.mappers import YamlMapper
from tivol.base_classes.migration_handler_base import MigrationHandlerBase
import os
from tivol.base_classes.plugins import DatePlugin, UppercasePlugin


class CompanyMigration(MigrationHandlerBase):

    def init_metadata(self):
        yaml_mapper = YamlMapper()
        yaml_mapper.set_destination_file(path=os.path.join(os.getcwd(), 'dummyapp', 'tivol_migrations', 'source_files', 'companies.yml'))

        self.id = 'company'
        self.name = 'Company migration'
        self.description = 'Migrating companies into the system'
        self.add_source_mapper(yaml_mapper)
        self.set_model_target(Company)
        self.fields_plugins = {
            'name': [UppercasePlugin],
            'founded_at': [{'plugin': DatePlugin, 'extra_info': {'format': '%B %d, %Y'}}]
        }
