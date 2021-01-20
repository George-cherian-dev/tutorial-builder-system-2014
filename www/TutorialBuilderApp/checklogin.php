<? ob_start(); ?>
<!DOCTYPE html>
<html>
<head>
<title>The Tutorial Builder App</title>
</head>
<body>
<?php
$host="localhost"; // Host name 
$username="root"; // Mysql username 
$password=""; // Mysql password 
$db_name="tutorial_clients"; // Database name 
$tbl_name="clients"; // Table name 

// Connect to server and select databse.
mysql_connect("$host", "$username", "$password")or die("cannot connect"); 
mysql_select_db("$db_name")or die("cannot select DB");

// Define $myusername and $mypassword 
$id=$_POST['myusername']; 
$p=$_POST['mypassword']; 

// To protect MySQL injection (more detail about MySQL injection)
$id = stripslashes($id);
$p = stripslashes($p);
$id = mysql_real_escape_string($id);
$p = mysql_real_escape_string($p);
$sql="SELECT name FROM $tbl_name WHERE uname='$id' and password='$p'";
$result=mysql_query($sql);
if($row=mysql_fetch_array($result)){
	echo "<form action='search.php' method='post' name='frm'>
		<input type='hidden' name='myusername' id='myusername' value='".$id."'>
		</form>";
}
else {
header("Location: index2.php");
}
?>
<script>
document.frm.submit();
</script>
</body>
</html>
<? ob_flush(); ?>