<?
include('functions.php');
include('modules.php');
echo array_sum( array_map('calc_fuel', $modules) );   #3412207
?>