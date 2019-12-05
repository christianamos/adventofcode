<?
#day 1a
function calc_fuel($mass) {
	return floor($mass / 3) - 2;
}

#day 1b
function calc_fuel_recursive($mass) {
	$fuel = calc_fuel($mass);
	
	if ($fuel > 0) {
		return $fuel + calc_fuel_recursive($fuel);
	}
	return 0;
}
?>