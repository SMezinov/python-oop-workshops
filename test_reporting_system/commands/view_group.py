from commands.base.base_command import BaseCommand


class ViewGroup(BaseCommand):
    def execute(self):
        group_id = int(self.params[0])

        group = self._app_data.find_test_group_by_id(group_id)

        string_return = f'#{group_id}. {group.name} ({len(group.tests)} tests)'

        for test in group.tests:
            string_return += f'\n  #{test.id}. [{test.description}]: {len(test.test_runs)} runs'

        return string_return