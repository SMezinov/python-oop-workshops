from models.constants.test_result import TestResult
from models.test import Test
from models.test_group import TestGroup
from models.test_run import TestRun


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []

        self._group_id = 1
        self._test_id = 1

    @property
    def groups(self):
        return tuple(self._test_groups)

    def add_test_group(self, name):
        group = TestGroup(self._group_id, name)

        self._test_groups.append(group)
        self._group_id += 1

        return group


    def find_test_group_by_id(self, group_id):
        for group in self._test_groups:
            if group.id == group_id:
                return group

        raise ValueError(f'Group with id {group_id} does not exist.')

    def remove_test_group_by_id(self, group_id):
        for group in self._test_groups:
            if group.id == group_id:
                self._test_groups.remove(group)
                return group_id

        raise ValueError(f'Group with this {group_id} not exist.')

    def find_test_by_id(self, test_id):
        for group in self._test_groups:
            for test in group.tests:
                if test.id == test_id:
                    return test

        raise ValueError(f'Test with {test_id} is not found')

    def add_test(self, test_gr_id, description):
        group = self.find_test_group_by_id(test_gr_id)
        new_test = Test(self._test_id, description)
        group.add_test(new_test)
        self._test_id += 1

        return new_test

    def add_run_to_test(self, test_id, result, runtime):
        test = self.find_test_by_id(test_id)
        new_run = TestRun(result, runtime)
        test.add_test_run(new_run)

    def test_report(self, test_id):
        test = self.find_test_by_id(test_id)

        test_runs_count = len(test.test_runs)
        passing_runs_count = 0
        failing_runs_count = 0
        total_runtime = 0

        for test_run in test.test_runs:
            if test_run.test_result == TestResult.PASS:
                passing_runs_count += 1
            elif test_run.test_result == TestResult.FAIL:
                failing_runs_count += 1

            total_runtime += test_run.runtime_ms

        average_runtime = total_runtime / test_runs_count

        return (test.id, test.description,
                test_runs_count, passing_runs_count,
                total_runtime, failing_runs_count, average_runtime)