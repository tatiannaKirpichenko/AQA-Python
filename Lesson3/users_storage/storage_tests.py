import os
import subprocess
import unittest


class StorageTestCase(unittest.TestCase):
    external_app = 'storage.cmd'
    storage_path = './storage/users.dat'

    def execute_shell(self, command):
        pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        res = pipe.stdout.read()
        pipe.stdout.close()
        pipe.wait(2)

        return res.decode('ASCII').lstrip().rstrip()

    def read_storage(self):
        f = open(self.storage_path, 'r')
        content = f.read()
        f.close()

        return content

