<? ob_start(); ?>
<!DOCTYPE html>
<html>
<head>
<title>RCFPL</title>
</head>
<body>
<?php
$host="localhost"; // Host name 
$username="rotaract_check"; // Mysql username 
$password="foot80ball85"; // Mysql password 
$db_name="rotaract_rcfpl"; // Database name 
$tbl_name="m_list"; // Table name 

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
$sql="SELECT m_id FROM $tbl_name WHERE m_name='$id' and m_pass='$p'";
$result=mysql_query($sql);
if($row=mysql_fetch_array($result)){
	$a=$row['m_id'];
	echo "<form action='m.php' method='post' name='frm'>
		<input type='hidden' name='mid' id='mid' value='".$a."'>
		</form>";
}
if($id='ada'&&$p='ada'){
header("Location: checking.php");
}
		ob_end_flush();
?>
<script>
document.frm.submit();
</script>
</body>
</html>
<? ob_flush(); ?>