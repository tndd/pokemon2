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

same_team = {}

for tr in div_pokemon_trend_card.find_all('tr'):
    # 各行のセルを取得
    cells = tr.find_all('td')
    if cells and len(cells) >= 2:
        # 順位を取得
        rank = cells[0].get_text(strip=True)
        # ポケモン名を取得
        pokemon_name = cells[1].find('a', class_="pokemon-name").get_text(strip=True)
        # 順位とポケモン名を辞書に追加
        same_team[rank] = pokemon_name

print(same_team)

# div_pokemon_trend_cardが目的の要素です
# with open('mock/pokemon_same_team.html', 'w', encoding='utf-8') as f:
#     f.write(div_pokemon_trend_card.prettify())
