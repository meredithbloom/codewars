// Who has the most money? - 6 kyu

/*
You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student {
  constructor(name, fives, tens, twenties) {
    this.name = name;
    this.fives = fives;
    this.tens = tens;
    this.twenties = twenties;
  }
}
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money

*/

class Student {
  constructor(name, fives, tens, twenties) {
    this.name = name;
    this.fives = fives;
    this.tens = tens;
    this.twenties = twenties;
  }
}


function mostMoney(students) {
    let most_money;
    let money = 0
    let sums = []
    // if there is only one student
    if (students.length === 1) {
        let { name, fives, tens, twenties } = students[0]
        console.log(name)
        return name
    }
    // if there is more than one student
    else {
        for (let s of students) {
            let { name, fives, tens, twenties } = s
            let money_count = (fives * 5) + (tens * 10) + (twenties * 20)
            sums.push(money_count)
            s['total_money'] = money_count
            if (money_count > money) {
                most_money = s
                money = money_count
            }
        }
        // if they all have the same amount of money
        if (new Set(sums).size === 1) {
            console.log('all')
            return 'all'
        }
        // if they don't all have the same amount of money
        else {
            console.log(most_money.name)
            return most_money.name
        }
    }
}

const andy = new Student("Andy", 0, 0, 2);
const stephen = new Student("Stephen", 0, 4, 0);
const eric = new Student("Eric", 8, 1, 0);
const david = new Student("David", 2, 0, 1);
const phil = new Student("Phil", 0, 2, 1);
const cam = new Student("Cameron", 2, 2, 0);
const geoff = new Student("Geoff", 0, 3, 0);


mostMoney([andy, stephen, eric, david, phil]) // Eric
mostMoney([cam, geoff, andy, stephen, eric, david, phil]) // Eric
mostMoney([cam, geoff]) // all
mostMoney([andy]) // andy