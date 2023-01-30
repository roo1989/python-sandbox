from pydantic.dataclasses import dataclass
from typing import Tuple
from pprint import pprint

@dataclass
class Scientist:
    name: str
    field: str
    born: int
    nobel: bool
    
    class Config:
        allow_mutations = False


scientists: Tuple = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

if __name__ == '__main__':
    fs = filter(lambda x: x.nobel is True, scientists)
    pprint(next(fs))
