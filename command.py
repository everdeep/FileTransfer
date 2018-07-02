import server
import filetransfer
from collections import deque

class CommandHistory(object):
    """The INVOKER class"""
    def __init__(self):
        self._history = deque()


    @property
    def history(self):
        return self._history


    def execute(self, command, args):
        self._history.appendleft((command, args))
        command.execute(args)


class Command(object):
    """ The COMMAND interface """
    def __init__(self, obj):
        self._obj = obj


    def execute(self, args):
        raise NotImplementedError


class StartServerCommand(Command):
    """ The COMMAND for starting the server """
    def execute(self, args):
        self._obj.start_server(args)


class StopServerCommand(Command):
    """ The COMMAND for stopping the server """
    def execute(self, args):
        self._obj.stop_server(args)

class SendDataCommand(Command):
    """ The COMMAND for sending data to server """
    def execute(self, args):
        self._obj.send_data(args)

class BrowseFilesCommand(Command):
    """ The COMMAND for browsing files """
    def execute(self, args):
        self._obj.browse(args)


class TransferFilesCommand(Command):
    """ The COMMAND for transfering files """
    def execute(self, args):
        self._obj.transfer(args)


class RemoveFilesCommand(Command):
    """ The COMMAND for removing files """
    def execute(self, args):
        self._obj.remove(args)


class CommandCenter(object):
    """The CLIENT class"""
    def __init__(self):
        self._server = server.Server()
        self._files = filetransfer.FileTransfer()
        self._history = CommandHistory()


    @property
    def history(self):
        return self._history.history


    def execute(self, cmd, *args):
        cmd = cmd.strip()
        if cmd == '00':
            return self._history.execute(StartServerCommand(self._server), args)
        elif cmd == '01':
            self._history.execute(StopServerCommand(self._server), args)
        elif cmd == '02':
            self._history.execute(SendDataCommand(self._server), args)
        elif cmd == '10':
            self._history.execute(BrowseFilesCommand(self._files), args)
        elif cmd == '11':
            self._history.execute(TransferFilesCommand(self._files), args)
        elif cmd == '12':
            self._history.execute(RemoveFilesCommand(self._files), args)
        else:
            print("Invalid command.")
