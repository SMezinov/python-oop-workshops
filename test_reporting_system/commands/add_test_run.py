from commands.base.base_command import BaseCommand


class AddTestRun(BaseCommand):
    def execute(self):
        test_id = int(self.params[0])
        result = self.params[1]
        runtime = int(self.params[2])

        self._app_data.add_run_to_test(test_id, result, runtime)

        return f'TestRun registered'