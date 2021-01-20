<head>
    <html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>TutorialBuilderApp</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" href="layout/styles/layout.css" type="text/css" />
<script type="text/javascript" src="layout/scripts/jquery.min.js"></script>
<script type="text/javascript" src="layout/scripts/jquery.jcarousel.pack.js"></script>
<script type="text/javascript" src="layout/scripts/jquery.jcarousel.setup.js"></script>
    <script>
    function showhide()
    {
    	var div = document.getElementById("newpost1");
		if (div.style.display !== "none")
		{
			div.style.display = "none";
		}
		else {
			div.style.display = "block";
		}
		var div = document.getElementById("newpost2");
		if (div.style.display !== "none")
		{
			div.style.display = "none";
		}
		else {
			div.style.display = "block";
		}
    }
  	</script>
<SCRIPT type="text/javascript">
    window.history.forward();
    function noBack() { window.history.forward(); }
</SCRIPT>
  </head>
  <body>
  	
	
	<div style="margin: 13%; margin-top:0;">
	<h1>These Are Your 11 Players For The day </h1> <br />
	<div>
	<p> This is your team 1 Goalkeepers(GK), 4 defenders(D), 4 midfielders(MF), 2 forwards(F) for the day who will earn points for you 
<br> Before a match day you will have to set 11 players for your core team 
<br>the time to do so is from 9pm at night the previous day - 1pm on match day 
<br> The 11 players set will earn points not the ones on the bench
</p>
</div>
<?php
$host="localhost"; // Host name 
$username="root"; // Mysql username 
$password=""; // Mysql password 
$db_name="tutorial_clients"; // Database name 
$tbl_name="clients"; // Table name 
$a=$_POST['name']; 

mysql_connect("$host", "$username", "$password")or die("cannot connect"); 
mysql_select_db("$db_name")or die("cannot select DB");
$sql="SELECT * FROM $tbl_name WHERE name='$a'";
$result=mysql_query($sql);

	/*$i=0;
if($row1=mysql_fetch_array($result)){
	$t=$row1['m_points'];
echo "<div id='newtable'>
	<h1>Playing 11</h1>
	<h1>Total Points ".$t."</h1>
	<form name='f' action='index.php' >
	<table border='1'>
	<tr>
	<td>Player Position&nbsp</td>
	Googly7628
	<td>Player Class&nbsp</td>
	<td>Player Name&nbsp</td>
	<td>Player Points Today&nbsp</td>
	<td>Player Cost&nbsp</td>
	</tr>";
	for($i=1;$i<=11;$i++)
	{
		$z="p_id".$i;
		$sql1="SELECT * FROM p_list WHERE p_id='$row1[$z]'";
		$result1=mysql_query($sql1);
		if($row=mysql_fetch_array($result1))
		{
		echo "<tr>
			<td>".$row['p_pos']."</td> 
			<td>".$row['p_class']."</td> 
			<td>".$row['p_name']."</td> 
			<td>".$row['p_points']."</td> 
			<td>".$row['p_cost']." M</td> 
		</tr>";
		}
	}
echo"</table>
<h1>Back Up Players</h1>
<table border='1'>
<tr>
	<td>Player Position&nbsp</td>
	<td>Player Class&nbsp</td>
	<td>Player Name&nbsp</td>
	<td>Player Points Today&nbsp</td>
	<td>Player Cost&nbsp</td>
</tr>
";
	for($i=12;$i<=16;$i++)
	{
		$z='p_id'.$i;
		$sql1="SELECT * FROM p_list WHERE p_id='$row1[$z]'";
		$result1=mysql_query($sql1);
		if($row=mysql_fetch_array($result1))
		{
		echo "<tr>
			<td>".$row['p_pos']."</td> 
			<td>".$row['p_class']."</td> 
			<td>".$row['p_name']."</td> 
			<td>".$row['p_points']."</td> 
			<td>".$row['p_cost']." M</td> 
		</tr>";
		}
	}
echo"</table>
<input type='submit' name='submit' value='LOGOUT'>
</form>
</div>";
}
else{
	echo "
		<form name='new' method='post' action='newmanager.php' >
		<input type='hidden' value='".$a."' name='mid' id='mid'>
		</form>
		";
}
ob_end_flush(); */
?> 
</div>
<!-- <script>
	document.new.submit();
</script> -->
	
	
	<!-- footer start -->
   <div class="wrapper col5">
  <div id="copyright">
    <p class="fl_left">Copyright &copy; 2014 - All Rights Reserved - <a href="#">Domain Name</a></p>
    <p class="fl_right">Template by <a target="_blank" href="http://www.os-templates.com/" title="Free Website Templates">OS Templates</a></p>
    <br class="clear" />
  </div>
</div>

    <!-- footer end -->    
	<script>
	/*$('.gallery_more').click(function(){
		var $this = $(this);
		$this.toggleClass('gallery_more');
		if($this.hasClass('gallery_more')){
			$this.text('Load More');			
		} else {
			$this.text('Login');
		}
	});
	*/
	//function validateForm()
{
var x=document.forms["form1"]["myusername"].value;
var atpos=x.indexOf("@");
var dotpos=x.lastIndexOf(".");
if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
  {
  alert("Not a valid e-mail address");
  return false;
  }
}
function validateForm1()
{

  alert("Registrations have been Closed till 8 pm");
  return false;
}
    </script>
  </body>
</html>