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

    def test_createAndGetUser_creatingAndReadingUserFromDatabase_ValidPositive(self):

        username = "PetrPetrov"
        create_command = f"{self.external_app} create {username}"
        res_create = self.execute_shell(create_command)

        get_command = f"{self.external_app} get {res_create}"
        res_get = self.execute_shell(get_command)

        self.assertEqual(username, res_get.strip())

    def test_createAndGetThreeUsers_creatingAndReadingThreeUsersFromDatabase_ValidPositive(self):

        users = ["PetrPetrov", "IvanIvanov", "AlexSmirnov"]
        user_ids = []

        for username in users:
            create_command = f"{self.external_app} create {username}"
            res_create = self.execute_shell(create_command)

            user_ids.append(res_create)

        for i, username in enumerate(users):
            get_command = f"{self.external_app} get {user_ids[i]}"
            res_get = self.execute_shell(get_command)

            self.assertEqual(username, res_get.strip())

    def test_deleteFirsUser_deleteFirstUserCreatingAndReadingUserFromDatabase_ValidPositive(self):

        users = ["PetrPetrov", "IvanIvanov", "AlexSmirnov"]
        user_ids = []

        first_user = users.pop(0)

        for username in users:
            create_command = f"{self.external_app} create {username}"
            res_create = self.execute_shell(create_command)

            user_ids.append(res_create)

        for i, username in enumerate(users):
            get_command = f"{self.external_app} get {user_ids[i]}"
            res_get = self.execute_shell(get_command)

            self.assertEqual(username, res_get.strip())

    def test_sortUsersAlphabetically_sortUsersAlphabeticallyFromDatabase_ValidPositive(self):

        users = ["PetrPetrov", "IvanIvanov", "AlexSmirnov"]
        user_ids = []

        users.sort()

        for username in users:
            create_command = f"{self.external_app} create {username}"
            res_create = self.execute_shell(create_command)

            user_ids.append(res_create)

        for i, username in enumerate(users):
            get_command = f"{self.external_app} get {user_ids[i]}"
            res_get = self.execute_shell(get_command)

            self.assertEqual(username, res_get.strip())

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
