from commands.base.base_command import BaseCommand


class RemoveGroup(BaseCommand):
    def execute(self):
        group_id = int(self.params[0])

        self._app_data.remove_test_group_by_id(group_id)

        return f'Group #{group_id} removed'