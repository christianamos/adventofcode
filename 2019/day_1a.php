<?
include('2019/helper/functions.php');
include('2019/helper/modules.php');

puts( array_sum( array_map('calc_fuel', $modules) ) );
?>