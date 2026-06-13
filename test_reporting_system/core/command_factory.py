from commands.add_test import AddTest
from commands.add_test_group import AddTestGroup
from commands.add_test_run import AddTestRun
from commands.remove_group import RemoveGroup
from commands.test_report import TestReport
from commands.view_group import ViewGroup
from commands.view_system import ViewSystem
from core.application_data import ApplicationData


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "addtestgroup":
            return AddTestGroup(params, self._app_data)
        if cmd.lower() == "addtest":
            return AddTest(params, self._app_data)
        if cmd.lower() == "addtestrun":
            return AddTestRun(params, self._app_data)
        if cmd.lower() == "testreport":
            return TestReport(params, self._app_data)
        if cmd.lower() == "removegroup":
            return RemoveGroup(params, self._app_data)
        if cmd.lower() == "viewgroup":
            return ViewGroup(params, self._app_data)
        if cmd.lower() == "viewsystem":
            return ViewSystem(params, self._app_data)


        raise ValueError(f'Invalid command name: {cmd}!')
