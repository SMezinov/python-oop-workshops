from commands.base.base_command import BaseCommand


class ViewSystem(BaseCommand):
    def execute(self):

        string_return = f'Test Reporter System ({len(self._app_data.groups)} test groups)'

        for group in self._app_data.groups:
            string_return += f'\n  #{group.id}. {group.name} ({len(group.tests)}) tests'

        return string_return