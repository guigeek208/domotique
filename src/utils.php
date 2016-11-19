<?php

function checkLight($pin="15") {
	$cmd = "gpio read ".$pin;
	$return = shell_exec($cmd);
	if ($return == 0) {
		return True;
	}
	else {
		return False;
	}
}

function changeLight($val) {
	$pin="15";
	$cmd = "gpio write ".$pin." ".$val;
	shell_exec($cmd);
	if ($val=="0") {
		echo '<button class="btn btn-defaul btn-primary" type="submit" onclick="changeLight(0);">Eteindre</button>';
	}
	if ($val=="1") {
		echo '<button class="btn btn-defaul btn-primary" type="submit" onclick="changeLight(0);">Allumer</button>';
	}
}

?>