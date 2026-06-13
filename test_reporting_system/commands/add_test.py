from commands.base.base_command import BaseCommand


class AddTest(BaseCommand):
    def execute(self):
        group_id = int(self.params[0])
        test_description = self.params[1]

        new_test = self._app_data.add_test(group_id, test_description)

        return f'Test #{new_test.id} added to group #{group_id}'