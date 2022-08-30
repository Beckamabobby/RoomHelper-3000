import re


def ms(text: str, code: str):  # Make status
    s = re.sub(r'\W', '', text)
    key = s[0].lower() + s[1:]
    return key, code, text


settingsTemplate = {
    'teacherName': 'Dave Briccetti',  # Change this
    'missingSeatIndexes': [],
    'chatEnabled': False,
    'sharesEnabled': True,
    'checksEnabled': False,
    'shares': [],
    'statuses': [
        ms('Need Help',   '?'),
        ms('Have Answer', 'A'),
        ms('Done',        'D')
    ],
    'chatDelayMs': 5000,
    'statusChangeEnableDelayMs': 3000,
    'chatMessageMaxLen': 150,
    'allowedSharesDomains': ['repl.it', 'editor.p5js.org', 'scalafiddle.io']
}

school1_config = {
    'periods': [
        (5, '11:50', '12:32'),
        (6, '13:10', '13:57'),
        (7, '14:00', '14:50'),
    ]
}

room1 = {
    'columns': 9,
    'rows': 4,
    'missingSeatIndexes': [8, 35],
    'aisleAfterColumn': 3,
}

settings = settingsTemplate
settings.update(room1)
settings.update(school1_config)