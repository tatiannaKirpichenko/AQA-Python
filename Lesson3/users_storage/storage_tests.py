import os
import subprocess
import unittest


class StorageTestCase(unittest.TestCase):
    external_app = 'storage.cmd'
    storage_path = './storage/users.dat'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        if not os.path.isdir('users_storage'):
            os.mkdir('users_storage')

    def setUp(self) -> None:
        super().setUp()
        if os.path.isfile(self.storage_path):
            os.remove(self.storage_path)

    def test_storageTestCase_creatingUserAndReadingUserFromDatabase_ValidPositive(self):

        command = self.external_app + " create PetrPetrov"

        res = self.execute_shell(command)

        self.assertEqual(1, int(res))

        content = self.read_storage()
        resultCreate = self.assertEqual("1  {}PetrPetrov\n", content)

        get_command = self.external_app + " get 1"

        res = self.execute_shell(get_command)

        resultGet = self.assertEqual('PetrPetrov', res.strip())

        self.assertEqual(resultCreate, resultGet)

    def test_storageTestCase_creatingTwoUsersAndReadingTwoUsersFromDatabase_ValidPositive(self):

        command = self.external_app + " create PetrPetrov"

        res = self.execute_shell(command)

        self.assertEqual(1, int(res))

        content = self.read_storage()
        resultCreate = self.assertEqual("1  {}PetrPetrov\n", content)

        get_command = self.external_app + " get 1"

        res = self.execute_shell(get_command)

        resultGet = self.assertEqual('PetrPetrov', res.strip())

        self.assertEqual(resultCreate, resultGet)

        command = self.external_app + " create IvanIvanov"

        res = self.execute_shell(command)

        self.assertEqual(2, int(res))

        content = self.read_storage()

        resultCreate = self.assertEqual("1  {}PetrPetrov\n2  {}IvanIvanov\n", content)

        get_command = self.external_app + " get 2"

        res = self.execute_shell(get_command)

        resultGet = self.assertEqual('IvanIvanov', res.strip())

        self.assertEqual(resultCreate, resultGet)

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
