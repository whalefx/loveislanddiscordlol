import discord
import os

contestants_names = []
bios_dict = {}
pic_dict = {}


class Contestant:
    instances = []

    def __init__(self, first_name, last_name, age, gender, town, status='in', pronoun=None):
        self.first_name = first_name.lower()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.town = town.title()
        self.status = status
        if pronoun is None:
            if gender == 'male':
                self.pronoun = 'he'
            else:
                self.pronoun = 'she'
        else:
            self.pronoun = pronoun
        self.partner = None
        self.bio = f"{self.first_name.title()} {self.last_name} is a {self.age} year old from {self.town}. {self.pronoun.title()} is currently {self.status} the game."
        self.init_bio = self.bio
        self.pic = f"{self.first_name.lower()}.jpg"
        contestants_names.append(f'{first_name}')
        bios_dict[f'{first_name}'] = self.bio
        pic_dict[f'{first_name}'] = self.pic
        self.__class__.instances.append(self)

    def __repr__(self):
        return f"<I am a contestant named {self.first_name.title()} {self.last_name}.>"

    def kick(self):
        self.status = "out"
        self.bio = f"{self.first_name.title()} {self.last_name} is  a {self.age} year old from {self.town}. {self.pronoun.title()} is currently {self.status} of the game."
        bios_dict[self.first_name] = self.bio

    def couple_up(self, partner):
        self.bio = self.init_bio
        partner = partner.lower()
        if partner in contestants_names:
            self.partner = partner
            for c in Contestant.instances:
                if partner == c.first_name:
                    setattr(c, 'partner', self.first_name)
                    break
            print(f'{self.first_name.title()} and {partner.title()} are now a couple.')
            self.bio += f" {self.first_name.title()} is coupled up with {self.partner.title()}."
        else:
            print('Error: name not found.')


def get_bio(first_word):
    found_pic = None
    found_bio = None
    for k in pic_dict.keys():
        if first_word == k:
            found_pic = pic_dict[k]
            break
    for k in bios_dict.keys():
        if first_word == k:
            found_bio = bios_dict[k]
            break
    return (found_pic, found_bio)


paige = Contestant('paige', 'thorne', '24', 'female', 'swansea')
dami = Contestant('dami', 'hope', '26', 'male', 'dublin')
indiyah = Contestant('indiyah', 'polack', '23', 'female', 'london')
liam = Contestant('liam', 'lewellyn', '22', 'male', 'newport')
tasha = Contestant('tasha', 'ghouri', '23', 'female', 'thirsk')
davide = Contestant('davide', 'sanclimenti', '27', 'male', 'manchester')
gemma = Contestant('gemma', 'owen', '19', 'female', 'chester')
ikenna = Contestant('ikenna', 'ekwonna', '23', 'male', 'nottingham')
andrew = Contestant('andrew', 'le page', '27', 'male', 'guernsey')
amber = Contestant('amber', 'beckford', '24', 'female', 'london')
luca = Contestant('luca', 'bish', '23', 'male', 'brighton')