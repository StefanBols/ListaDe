import json

def addMovie(jsonMovie):
	with open('../DB/movies.db', 'a') as movies:
		movies.write(json.dumps(jsonMovie))
		movies.write('\n')

def findMovieById1(id):
	with open ('../DB/movies.db', 'r') as movies:
		idStructure = '"id":"' + id + '"'
		found = list(filter(lambda x: idStructure in x, movies))

		count = len(found)
		if count > 1:
			raise KeyError('The key produced multiple results')
		if count == 0:
			return None

		return json.loads(found[0])


def findMovieById(id):
	searchString = '"id":"' + id + '"'
	result = searchSingleMovie(searchString)
	return result
	
def findMovieByIMDbId(imdbId):
	searchString = '"imdbId":"' + imdbId + '"'
	result = searchSingleMovie(searchString)
	return result
	

def searchSingleMovie(searchString):
	movies = searchMovies(searchString)
	count = len(movies)
	if count > 1:
		raise KeyError('The search produced multiple results')
	if count == 0:
		return None

	return json.loads(movies[0])

def searchMovies(searchString):
	with open ('../DB/movies.db', 'r') as movies:
		results = list(filter(lambda x: searchString in x, movies))

		jsonObj = []
		for result in results:
			jsonObj.append(json.loads(result))

		return jsonObj


print(searchMovies('fgdf-324234-fgdgfg-GUID1'))
#print(findMovieById('fgdf-324234-fgdgfg-GUID1'))
