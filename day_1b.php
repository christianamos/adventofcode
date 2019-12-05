<?
include('helper/functions.php');
include('helper/modules.php');

$total_fuel = 0;
foreach ($modules as $mass) {
	$total_fuel += calc_fuel_recursive($mass);
}
puts($total_fuel);
?>