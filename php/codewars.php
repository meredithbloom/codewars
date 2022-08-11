
<?php
// Bit Counting - 6 kyu
// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

function countBits($n) {
    $converted = strval(decbin($n));
    return substr_count($converted, "1");
}

// echo countBits(0);
// countBits(4);
// countBits(7);
// countBits(9);
// countBits(10);


// Highest and Lowest - 7 kyu
// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

function highAndLow($numbers) {
    $strs = explode(" ", $numbers);
    $nums = array_map('intval', $strs);
    return strval(max($nums)).' '.strval(min($nums));
}


// echo highAndLow("1 2 3 4 5");
// echo "\n";
// echo highAndLow("1 2 -3 4 5");
// echo "\n";
// echo highAndLow("1 9 3 4 -5");
// echo "\n";



// Array.diff - 6 kyu
// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

//It should remove all values from list a, which are present in list b keeping their order.
// arrayDiff([1,2],[1]) == [2]

// If a value is present in b, all of its occurrences must be removed from the other:
// arrayDiff([1,2,2,2,3],[2]) == [1,3]

function arrayDiff($a, $b) {
    return array_values(array_diff($a,$b));
}

arrayDiff([1,2], [1]);
arrayDiff([1,2,2,2,3], [2]);



// WeIrD StRiNg CaSe - 6kyu
// write a function that takes a string, and return the same string with all even indexed characters in each word cased, and all odd indexed character in each word lower cased. so the zero-ith index is even

function toWeirdCase($string) {
    $split = explode(' ', $string);
    $new_string = [];
    foreach ($split as $word) {
        $word = strtolower($word);
        for ($index = 0; $index < strlen($word); $index+=2) {
            $word[$index] = strtoupper($word[$index]);
        }
        // echo $word."\n";
        array_push($new_string, $word);
    }
    $newString = implode(" ", $new_string);
    return $newString;
}

//toWeirdCase('Hello world foo bar baz');
//toWeirdCase('wEll i GuesS you passed');


//L1: set alarm
function setAlarm(bool $employed, bool $vacation)
{
    if ($employed && !$vacation) {
        return true;
    } else {
        return false;
    }
}




// get the middle character. return middle character of given word. if odd length, return single middle character. if even length, return middle two characters
function getMiddle($text) {
    $length = strlen($text);
    if ($length == 1) {
        return $text[0];
    } elseif ($length % 2 == 0) {
        return $text[($length/2)-1].$text[$length/2];
    } elseif ($length % 2 != 0) {
        return $text[($length-1)/2];
    }
}

// echo getMiddle("test");
// echo "\n";
// echo getMiddle("testing");
// echo "\n";
// echo getMiddle("middle");
// echo "\n";
// echo getMiddle("A");
// echo "\n";





// find the odd int - given an array of numbers, find the one that appears an odd number of times
function findIt(array $seq) {
    $counts = array_count_values($seq);
    foreach ($counts as $key => $value) {
        if ($value % 2 != 0) {
            return $key;
        }
    }
}



// count number of duplicates - number of distinct case insensitive alphabetic characters and numeric digits that occur more than once in input string
function duplicateCount($text) {
    $counts = array_count_values(str_split(strtolower($text)));
    $dupes = 0;
    foreach ($counts as $key => $value) {
        if ($value > 1) {
            $dupes++;
        }
    }
    echo $dupes;
}


// duplicateCount("");
// duplicateCount("abcde");
// duplicateCount("aabbcde");
// duplicateCount("aabBcde");
// duplicateCount("Indivisibility");


// square digits
function square_digits($num){
    $array = str_split($num);
    $squared = '';
    foreach ($array as $num) {
    $squared = $squared.($num**2);
    }
    echo $squared;
    return $squared;
}


// square_digits(9119);
// square_digits(24680);
// square_digits(13579);
// square_digits(0);




//count multiples of 3 or 5
function solution($number){
    $sum = 0;
    for ($count = 3; $count <= $number; $count++) { 
        if ($count % 3===0 && $count % 5===0) { 
            $sum+=0; 
        } elseif ($count % 3===0) { 
            $sum+=$count; 
        } elseif ($count % 5===0) { 
            $sum+=$count; 
        } else { $sum+=0; } 
    } return $sum; 
}


?>