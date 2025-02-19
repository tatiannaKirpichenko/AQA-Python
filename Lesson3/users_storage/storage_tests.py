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

    def test_CreateUser_Positives_ValidPositive(self):

        #arrange
        command = self.external_app + " create PetrPetrov"

        #act
        res = self.execute_shell(command)

        #assert
        self.assertEqual(1, int(res))

        content = self.read_storage()
        self.assertEqual("1  {}PetrPetrov\n", content)

    def test_GetUser_Positives_ValidPositive(self):
        # arrange
        create_command = self.external_app + " create PetrPetrov"
        self.execute_shell(create_command)

        get_command = self.external_app + " get 1"

        # act
        res = self.execute_shell(get_command)

        # assert
        self.assertEqual('PetrPetrov', res.strip())


    def test_EqualsResultCreateAndGetUser_Positives_ValidPositive(self):

        command = self.external_app + " create PetrPetrov"

        res = self.execute_shell(command)

        self.assertEqual(1, int(res))

        content = self.read_storage()
        resultCreate = self.assertEqual("1  {}PetrPetrov\n", content)

        get_command = self.external_app + " get 1"

        res = self.execute_shell(get_command)

        resultGet = self.assertEqual('PetrPetrov', res.strip())

        self.assertEqual(resultCreate, resultGet)

    def test_CreateNewUser_Positives_ValidPositive(self):
        command = self.external_app + " create IvanIvanov"

        # act
        res = self.execute_shell(command)

        # assert
        self.assertEqual(1, int(res))

        content = self.read_storage()
        self.assertEqual("1  {}IvanIvanov\n", content)

    def test_GetNewUser_Positives_ValidPositive(self):
        # arrange
        create_command = self.external_app + " create IvanIvanov"
        self.execute_shell(create_command)

        get_command = self.external_app + " get 1"

        # act
        res = self.execute_shell(get_command)

        # assert
        self.assertEqual('IvanIvanov', res.strip(), )
        content = self.read_storage()
        self.assertEqual("1  {}IvanIvanov\n", content)


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


