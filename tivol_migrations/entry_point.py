from dummyapp.tivol_migrations.actors_migration import ActorMigration
from dummyapp.tivol_migrations.animals_migration import AnimalMigration
from dummyapp.tivol_migrations.companies_migration import CompanyMigration
from dummyapp.tivol_migrations.film_makers_migration import FilmMakerMigration
from dummyapp.tivol_migrations.tags_migration import TagMigration
from tivol.base_classes.entry_point import EntryPoint


class CustomEntryPoint(EntryPoint):

    def register_migrations(self):
        self.add_migration_handler(AnimalMigration)
        self.add_migration_handler(CompanyMigration)
        self.add_migration_handler(ActorMigration)
        # self.add_migration_handler(TagMigration)
        self.add_migration_handler(FilmMakerMigration)
