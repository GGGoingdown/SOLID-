from enum import Enum
from dataclasses import dataclass
from typing import Iterator, List
from abc import ABC, abstractclassmethod


class Continent(Enum):
    EUROPE = 1
    AFRICA = 2
    ASIA = 3
    AMERICA = 4


class Language(Enum):
    ENGLISH = 1
    GERMAN = 2
    MANDARIN = 3


@dataclass
class Country:
    name: str
    language: Language
    contient: Continent


class BadFilter:
    """
    Bad filter
    如果增加不同的條件 ex. 人口
    或是增加and的條件
    則需要一直修改filter的class (Breaking Open/closed principle)
    """

    def filter_language(
        self, countries: List[Country], language: Language
    ) -> Iterator[Country]:
        for country in countries:
            if country.language == language:
                yield country

    def filter_contient(
        self, countries: List[Country], contient: Continent
    ) -> Iterator[Country]:
        for country in countries:
            if country.contient == contient:
                yield country


class Spcification(ABC):
    @abstractclassmethod
    def is_satisfied(self, country: Country) -> bool:
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class ContientSpcification(Spcification):
    def __init__(self, contient: Continent):
        self.contient = contient

    def is_satisfied(self, country: Country) -> bool:
        return country.contient == self.contient


class LanguageSpecification(Spcification):
    def __init__(self, language: Language):
        self.language = language

    def is_satisfied(self, country: Country) -> bool:
        return country.language == self.language


class AndSpecification(Spcification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, country: Country) -> bool:
        return all(map(lambda spec: spec.is_satisfied(country), self.args))


class GoodFilter:
    def filter(
        self, countries: List[Country], specification: Spcification
    ) -> Iterator[Country]:
        for country in countries:
            if specification.is_satisfied(country):
                yield country


if __name__ == "__main__":
    taiwan = Country(name="Taiwan", language=Language.MANDARIN, contient=Continent.ASIA)
    germany = Country(
        name="Germany", language=Language.GERMAN, contient=Continent.EUROPE
    )
    china = Country(name="China", language=Language.MANDARIN, contient=Continent.ASIA)
    usa = Country(name="USA", language=Language.ENGLISH, contient=Continent.AMERICA)
    singapore = Country(
        name="Singapore", language=Language.ENGLISH, contient=Continent.ASIA
    )

    countries = [taiwan, germany, china, usa, singapore]

    lang_spec = LanguageSpecification(language=Language.ENGLISH)
    continent_spec = ContientSpcification(contient=Continent.ASIA)

    asis_eng_spec = lang_spec & continent_spec

    gf = GoodFilter()
    for country in gf.filter(countries=countries, specification=asis_eng_spec):
        print(country.name)
