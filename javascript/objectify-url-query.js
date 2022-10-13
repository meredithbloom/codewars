// Objectify a URL Query String
// In this kata, we want to convert a URL query string into a nested object. The query string will contain parameters that may or may not have embedded dots ('.'), and these dots will be used to break up the properties into the nested object.

//You will receive a string input that looks something like this:
str1 = 'user.name.firstname=Bob&user.name.lastname=Smith&user.favoritecolor=Light%20Blue'

// Your method should return an object hash-map that looks like this:
/*
 {
  'user': {
    'name': {
      'firstname': 'Bob',
      'lastname': 'Smith'
    },
    'favoritecolor': 'Light Blue'
  }
}
*/
function convertQueryToMap(query) {
	//let params = new URLSearchParams(query)
	//console.log(params)
	const final = {}
	const keyValuePairs = query
		// splits into separate traits
		.split('&')
		// splits each trait so nested keys are separate from final val
		.map(kvp => kvp.split('='))
		//.filter(([key]) => Boolean(key))
	//console.log(keyValuePairs)
	// loops through all key value pairs
	for (const kvp of keyValuePairs) {
		// array destructuring, separates path from final val
		const [key, value] = kvp
		// splits path so we can convert to nested objects
		const path = key.split('.')
		let acc = final 
		// deconstructing further
		for (const [i, prop] of path.entries()) {
			//console.log([i, prop])
			if (i === path.length - 1) {
				acc[prop] = decodeURIComponent(value)
				continue
			}
			if (!acc[prop]) {
				acc[prop] = {}
			}
			acc = acc[prop]
		}
	}
	console.log(final)
	return final
}

//convertQueryToMap(str1)

