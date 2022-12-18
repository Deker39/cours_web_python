import datetime
import unittest
from unittest.mock import Mock,patch

# mock = Mock()
#
#
# def is_weekday():
#     today = datetime.date.today()
#     return 0 <= today.weekday()
#
# print(mock)

class  CharacterTest(unittest.TestCase):

    @patch('main_test.Character')
    def test_character(self,character_mock):
        ch = character_mock()
        ch.character.return_value = [{
            "id": '2', "name": "Morty Smith", "status": "Alive", "species": "Human", "type": "", "gender": "Male",
            "origin": {"name": "Earth", "url": "https://rickandmortyapi.com/api/location/1"},
            "location": {"name": "Earth", "url": "https://rickandmortyapi.com/api/location/20"},
            "image": "https://rickandmortyapi.com/api/character/avatar/2.jpeg",
            "episode": ["https://rickandmortyapi.com/api/episode/1",
                        "https://rickandmortyapi.com/api/episode/2", ], "url": "https://rickandmortyapi.com/api/character/2", "created": "2017-11-04T18:50:21.651Z"
        }]
        response = ch.character()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0],dict)





