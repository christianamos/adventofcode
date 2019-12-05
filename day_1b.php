<?
include('functions.php');
include('modules.php');
$total_fuel = 0;
foreach ($modules as $mass) {
	$total_fuel += calc_fuel_recursive($mass);
}
echo $total_fuel;   #5115436
?>