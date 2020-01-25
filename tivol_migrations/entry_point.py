from dummyapp.tivol_migrations.animals_migration import AnimalMigration
from dummyapp.tivol_migrations.companies_migration import CompanyMigration
from tivol.base_classes.entry_point import EntryPoint


class CustomEntryPoint(EntryPoint):

    def register_migrations(self):
        self.add_migration_handler(AnimalMigration)
        self.add_migration_handler(CompanyMigration)
