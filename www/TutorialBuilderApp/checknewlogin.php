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
$n=$_POST['myname']; 
$e=$_POST['email']; 
$s=$_POST['mystream'];

// To protect MySQL injection (more detail about MySQL injection)
$id = stripslashes($id);
$p = stripslashes($p);
$id = mysql_real_escape_string($id);
$p = mysql_real_escape_string($p);
$sql="SELECT name FROM $tbl_name WHERE uname='$id'";
$result=mysql_query($sql);

echo "<h1>LOADING...</h1>";
if($row=mysql_fetch_array($result)){
	header("Location:indexerror.php");
}
else {
$sql1="INSERT into $tbl_name VALUES('$n','$e','$id','$p','$s')";

			mysql_query($sql1);
			echo("<form action='regEnd.php' method='post' name='frm'>
		</form>");
}
ob_end_flush();
?>
<script>
document.frm.submit();
</script>
</body>
</html>
<? ob_flush(); ?>