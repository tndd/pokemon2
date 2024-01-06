import json

from bs4 import BeautifulSoup

# HTMLファイルを読み込む
with open('mock/pokemon.html', 'r', encoding='utf-8') as file:
    contents = file.read()

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(contents, 'html.parser')

# "同じチーム"というテキストを持つspanを見つける
span_same_team = soup.find('span', string="同じチーム")
# spanから最も近い親要素でクラスが'pokemon-trend-card'のdivを見つける
div_pokemon_trend_card = span_same_team.find_parent(class_="pokemon-trend-card")

# div_pokemon_trend_cardが目的の要素です
with open('mock/pokemon_same_team.html', 'w', encoding='utf-8') as f:
    f.write(div_pokemon_trend_card.prettify())

# JSON形式で保存
# with open('pokemon_data.json', 'w', encoding='utf-8') as f:
#     json.dump(sections, f, ensure_ascii=False, indent=2)
