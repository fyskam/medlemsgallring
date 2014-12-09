<?php header("Content-Type: text/html; charset=utf8");?>

<html>
    <head></head>
    <body>
<?php

//Hämta hashtaggen
$hashtag=$_GET[v];

//Anslut till mysqlservern
$con = mysql_connect("localhost", "fyskam", "abc123") OR die(mysql_error());
mysql_select_db("register_copy", $con) OR die(mysql_error());
$TABLE = 'members';

//städa hashtaggen
$hashtag = mysql_real_escape_string($hashtag);

//kolla att hashtaggen finns och att det finns exakt en av den
$result = mysql_query("select hash from $TABLE where hash='$hashtag'", $con);
$numrows = mysql_num_rows($result);
if ($numrows == 0) die("Kunde inte hitta dig...");
if ($numrows != 1) die("Hashkollision, detta borde inte hända...");

//uppdatera active = 1
mysql_query("update $TABLE set active='1' where hash='$hashtag'");

//kontroll
if (mysql_affected_rows() == -1) die("Oväntat fel (".mysql_error()."). Kontakta Info (nvf-info@utn.se)");
if (mysql_affected_rows() != 1) die("Oväntat fel (".mysql_error()."). Kontakta Info (nvf-info@utn.se)");

mysql_close($con);
echo "Ditt medlemskap är förnyat, tack för ditt engagemang";

?>

    </body>
</html>
