import json

def addMovie(jsonMovie):
	with open('../DB/movies.db', 'a') as movies:
		movies.write(json.dumps(jsonMovie))
		movies.write('\n')

def findMovieById(id):
	with open ('../DB/movies.db', 'r') as movies:
		idStructure = '"id":"' + id + '"'
		found = list(filter(lambda x: idStructure in x, movies))

		count = len(found)
		if count > 1:
			raise KeyError('The key produced multiple results')
		if count == 0:
			return None

		return json.loads(found[0])