import csv
import json
from concurrent.futures import ProcessPoolExecutor

import requests
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
    disad_pokeon = soup.find('p', string="倒されたポケモン")
    # spanから最も近い親要素でクラスが'pokemon-trend-card'のdivを見つける
    div_pokemon_trend_card = disad_pokeon.find_parent(class_="pokemon-trend-card")
    # 同じチーム数の順位と名前のペア
    d_disad_pokeon = {}
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
            d_disad_pokeon[rank] = pokemon_name
    return d_disad_pokeon


def extract_pokemon_data(rank, pokemon_name, url):
    # urlからポケモン情報の取得
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # 取得した情報をパース
    same_team = extract_same_team(soup)
    dominant_pokemon = extract_dominant_pokemon(soup)
    disadvantage_pokemon = extract_disadvantage_pokemon(soup)
    return {
        'rank': rank,
        'pokemon': pokemon_name,
        'same_team': same_team,
        'dominant': dominant_pokemon,
        'disadvantage': disadvantage_pokemon
    }


def fetch_pokemon_data(rank, pokemon_name, url):
    d = extract_pokemon_data(rank, pokemon_name, url)
    # dをjson形式でファイルに保存
    with open(f'data/pokemon/{pokemon_name}.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)
    print(f'{pokemon_name}のデータを取得しました')


def all_fetch_pokemon_data():
    with open('data/ranking.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # ヘッダーをスキップ
        next(reader)
        # ThreadPoolExecutorを使用して並列処理
        with ProcessPoolExecutor(max_workers=16) as executor:
            # 各行に対してfetch_pokemon_data関数を実行
            futures = [executor.submit(fetch_pokemon_data, *row) for row in reader]
            # 結果を待つ
            for future in futures:
                future.result()



if __name__ == '__main__':
    all_fetch_pokemon_data()