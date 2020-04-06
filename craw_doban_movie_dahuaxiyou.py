def get_movie_info():
	headers = {'User-Agent': 'Mozilla/5.0 xxxxxx'}
	basel = 'https://movie.douban.com/subject/1292213/'
	html = requests.get(basel, headers=headers).content.decode('utf-8', 'ignore')
	url_content = re.search(r'"@context": "http://schema.org",(.*?)"ratingValue": "9.2"', html, re.S)
	texts = url_content.group()  # 获取匹配正则表达式的整体结果
	texts = str("{" + texts + "}}")
	# important
	data = json.loads(texts, strict=False)
	movie_info = {'name': data['name'], 'author': data['author'], 'actor': data['actor'], 'director': data['director']}
	print(movie_info)
	ju.write_json(data, r'data/data.json')

if __name__ == '__main__':
    get_movie_info()