function solution($number){
$sum = 0;
for ($count = 3; $count <= $number; $count++) { if ($count % 3===0 && $count % 5===0) { $sum+=0; } elseif ($count % 3===0) { $sum+=$count; } elseif ($count % 5===0) { $sum+=$count; } else { $sum+=0; } } return $sum; }