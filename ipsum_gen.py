from random import randint

music_words = [
'The Clash', 'The Cure', 'The Sex Pistols', 'Boomtown Rats', 'The Airborne Toxic Event', 'Thees Uhlmann', 'Die Toten Hosen', 'Dave Hause', 'Brian Fallon', 'Billy Bragg'
]

def musicarize(word):
    random_pos = randint(0, len(music_words) - 1)
    return f'{word} {music_words[random_pos]}'

paragraphs = int(input('How many paragraphs of music ipsum:'))

with open('ipsum_txt') as ipsum_original:
    items = ipsum_original.read().split()

    for n in range(paragraphs):
        music_text = list(map(musicarize, items))
        with open('music_ipsum.txt', 'a') as ipsum_music:
            ipsum_music.write(' '.join(music_text) + '\n\n')
