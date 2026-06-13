from commands.base.base_command import BaseCommand


class TestReport(BaseCommand):

    def execute(self):
        test_id = int(self.params[0])

        (test_id, test_description,
         test_runs_count, passing_runs_count,
         total_runtime, failing_runs_count, avg_runtime) = self._app_data.test_report(test_id)

        return f'''#{test_id}. [{test_description}]: {test_runs_count} runs
- Passing: {passing_runs_count}
- Failing: {failing_runs_count}
- Total runtime: {total_runtime}ms
- Average runtime: {avg_runtime:.1f}ms'''