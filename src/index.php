<?php
include("header.php");
include("navbar.php");
include("utils.php");
?>
<div class="container">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Lumière</h3>
    </div>
    <div class="panel-body">
      <div id="light">
        <?php
          if (checkLight()) {
            echo '<button class="btn btn-defaul btn-primary" type="submit" onclick="changeLight(1);">';
            echo "Eteindre";
          }
          else {
            echo '<button class="btn btn-defaul btn-primary" type="submit" onclick="changeLight(0);">';
            echo "Allumer";
          }
        ?>
        </button>
      </div>
  </div>
</div> <!-- /container -->
<?php
include("footer.php");
?>