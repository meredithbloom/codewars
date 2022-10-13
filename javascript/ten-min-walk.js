// Take a Ten Minutes Walk - 6 kyu
/*
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
*/

function isValidWalk(walk) {
	let x = 0;
	let y = 0;
	if (walk.length !== 10) {
		return false
	}
	for (let step of walk) {
		if (step === 'n') {
			y++
		} else if (step === 's') {
			y--
		} else if (step === 'e') {
			x++
		} else if (step === 'w') {
			x--
		}
	}
	if (x !== 0 || y !== 0) {
		return false
	} else {
		return true
	}
}

let dir1 = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'];
let dir2 = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'];

// console.log(isValidWalk(dir1))
// console.log(isValidWalk(dir2))




