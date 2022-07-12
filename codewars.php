
<?php
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
    $dupes = 0;
    $array = str_split($text);
    print_r($array);
    foreach ($array as $item) {
        if (substr_count($text, $item) > 0) {
            $dupes++;
        }
    }
}


duplicateCount("");
duplicateCount("abcde");
duplicateCount("aabbcde");



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