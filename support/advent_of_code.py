from environs import Env
import requests

requests = requests.Session()

env = Env()
env.read_env()


class Puzzle:
    INPUT_URL = 'https://adventofcode.com/{year}/day/{day}/input'
    ANSWER_URL = 'https://adventofcode.com/{year}/day/{day}/answer'

    def __init__(self, year, day, session_id=None):
        self.year = year
        self.day = day
        self.session_id = session_id or env.str('SESSION_ID')

    def fetch(self):
        return self.call(
            'GET',
            self.INPUT_URL.format(year=self.year, day=self.day)
        )

    def answer(self, answer, level):
        data = {
            'answer': answer,
            'level': level,
        }

        response = self.call(
            'POST',
            self.ANSWER_URL.format(year=self.year, day=self.day),
            data=data
        )

        if 'That\'s not the right answer' in response:
            return 'Wrong.'
        elif 'Did you already complete it?' in response:
            return 'Already completed.'
        elif 'That\'s the right answer' in response:
            return 'Completed!'
        else:
            return 'Error.'

    def call(self, method, url, data=None):
        cookies = {
            'session': self.session_id,
        }

        response = requests.request(method, url, cookies=cookies, data=data)
        response.raise_for_status()

        return response.text
