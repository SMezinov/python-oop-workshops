from commands.base.base_command import BaseCommand

class AddTestGroup(BaseCommand):
    def execute(self):
        new_group_name  = self.params[0]
        new_group = self._app_data.add_test_group(new_group_name)

        return f'Group #{new_group.id} created'