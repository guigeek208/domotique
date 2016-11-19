<?php
include("utils.php");
if (isset($_GET["val"])) {
	changeLight($_GET["val"]);
}
?>