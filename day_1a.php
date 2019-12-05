<?
include('helper/functions.php');
include('helper/modules.php');

puts( array_sum( array_map('calc_fuel', $modules) ) );
?>