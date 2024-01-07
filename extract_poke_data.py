import json

from bs4 import BeautifulSoup


def extract_same_team(soup):
    # "同じチーム"というテキストを持つspanを見つける
    span_same_team = soup.find('span', string="同じチーム")
    # spanから最も近い親要素でクラスが'pokemon-trend-card'のdivを見つける
    div_pokemon_trend_card = span_same_team.find_parent(class_="pokemon-trend-card")
    # 同じチーム数の順位と名前のペア
    same_team = {}
    # ペア情報の取得
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
    return same_team


def extract_dominant_pokemon(soup):
    # "同じチーム"というテキストを持つspanを見つける
    dominant_pokemon = soup.find('p', string="倒したポケモン")
    # spanから最も近い親要素でクラスが'pokemon-trend-card'のdivを見つける
    div_pokemon_trend_card = dominant_pokemon.find_parent(class_="pokemon-trend-card")
    # 同じチーム数の順位と名前のペア
    d_dominant_pokemon = {}
    # ペア情報の取得
    for tr in div_pokemon_trend_card.find_all('tr'):
        # 各行のセルを取得
        cells = tr.find_all('td')
        if cells and len(cells) >= 2:
            # 順位を取得
            rank = cells[0].get_text(strip=True)
            # ポケモン名を取得
            pokemon_name = cells[1].find('a', class_="pokemon-name").get_text(strip=True)
            # 順位とポケモン名を辞書に追加
            d_dominant_pokemon[rank] = pokemon_name
    return d_dominant_pokemon


def extract_disadvantage_pokemon(soup):
        # "同じチーム"というテキストを持つspanを見つける
    disad_pokeon = soup.find('p', string="倒したポケモン")
    # spanから最も近い親要素でクラスが'pokemon-trend-card'のdivを見つける
    div_pokemon_trend_card = disad_pokeon.find_parent(class_="pokemon-trend-card")
    # 同じチーム数の順位と名前のペア
    disad_pokeon = {}
    # ペア情報の取得
    for tr in div_pokemon_trend_card.find_all('tr'):
        # 各行のセルを取得
        cells = tr.find_all('td')
        if cells and len(cells) >= 2:
            # 順位を取得
            rank = cells[0].get_text(strip=True)
            # ポケモン名を取得
            pokemon_name = cells[1].find('a', class_="pokemon-name").get_text(strip=True)
            # 順位とポケモン名を辞書に追加
            disad_pokeon[rank] = pokemon_name
    return disad_pokeon


if __name__ == '__main__':
    # HTMLファイルを読み込む
    with open('mock/pokemon.html', 'r', encoding='utf-8') as file:
        contents = file.read()
    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(contents, 'html.parser')
    d = extract_dominant_pokemon(soup)
    print(d)
