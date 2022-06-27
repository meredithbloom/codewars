<!--  square every digit -->

function square_digits($num){
    $array = str_split($num);
    $squared = '';
    foreach ($array as $num) {
    $squared = $squared.($num**2);
    }
    return $squared;
}


square_digits(9119)
square_digits(24680)
square_digits(13579)
square_digits(0)




<!--  -->
function solution($number){
$sum = 0;
for ($count = 3; $count <= $number; $count++) { if ($count % 3===0 && $count % 5===0) { $sum+=0; } elseif ($count % 3===0) { $sum+=$count; } elseif ($count % 5===0) { $sum+=$count; } else { $sum+=0; } } return $sum; }