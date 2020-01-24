from dummyapp.tivol_migrations.animals_migration import AnimalMigrations
from tivol.base_classes.entry_point import EntryPoint


class CustomEntryPoint(EntryPoint):

    def register_migrations(self):
        self.add_migration_handler(AnimalMigrations)
