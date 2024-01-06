from bs4 import BeautifulSoup

# HTMLファイルを読み込む
with open('main.html', 'r', encoding='utf-8') as file:
    contents = file.read()

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(contents, 'html.parser')

# data-pokemon-name属性を持つすべての要素を検索し、"圏外"でないもののみ抽出
for div in soup.find_all('div', attrs={"data-pokemon-name": True}):
    # "圏外"を含むspan要素を検索
    rank_span = div.find('span', class_="pokemon-ranking-rank")
    # "圏外"テキストを持つかどうかをチェック
    if rank_span and "圏外" not in rank_span.text:
        # aタグからURLを抽出
        a_tag = div.find('a')
        if a_tag and a_tag.has_attr('href'):
            url = 'https://sv.pokedb.tokyo' + a_tag['href']
            print(url)