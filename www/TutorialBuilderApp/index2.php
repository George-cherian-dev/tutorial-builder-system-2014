<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

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
		var d = document.getElementById("buttonL");
		if (div.style.display !== "none")
		{
			div.style.display = "none";
		}
		else {
			div.style.display = "block";
			//d.style.margin-top = "10px";
			
		}
	}
    function showhide2()
    {
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
</head>
<body id="top">
<!-- ####################################################################################################### -->
<div class="wrapper col1">
  <div id="header">
    <div id="logo">
      <h1><span style=" width:100%;"><a href="index.html">The Tutorial Builder Application</a></span></h1>
      <p><span style="margin-left: auto;margin-right: auto;">Making life easier, one subject at a time.</span></p>
    </div>
    <!--<div id="topnav">
      <ul>
        <li class="active"><a href="index.html">Home</a></li>
        <li><a href="pages/style-demo.html">Style Demo</a></li>
        <li><a href="pages/full-width.html">Full Width</a></li>
        <li><a href="#">DropDown</a>
          <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
          </ul>
        </li>
        <li class="last"><a href="#">A Long Link Text</a></li>
      </ul>
    </div> -->
    <br class="clear" />
  </div>
</div>
<!-- ####################################################################################################### -->
<div class="wrapper col2">
  <div id="featured_slide">
    <div id="featured_content">
      <ul>
        <li><img src="images/demo/1.gif" alt="" />
          <div class="floater">
            <h2>Step 1</h2>
            <p>This is a W3C standards compliant free website template from <a href="http://www.os-templates.com/">OS Templates</a>. This template is distributed using a <a href="http://www.os-templates.com/template-terms">Website Template Licence</a>, which allows you to use and modify the template for both personal and commercial use when you keep the provided credit links in the footer. For more CSS templates visit <a href="http://www.os-templates.com/">Free Website Templates</a>.</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
          </div>
        </li>
        <li><img src="images/demo/2.gif" alt="" />
          <div class="floater">
            <h2>Step 2</h2>
            <p>Temperinte interdum sempus odio urna eget curabitur semper convallis nunc laoreet. Nullain convallis ris elis vest liberos nis diculis feugiat in rutrum. Suspendreristibulumfaucibulum lobortor quis tortortor ris sapien sce enim et volutpat sus. Urnaretiumorci orci fauctor leo justo nulla cras ridiculum&hellip;</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
          </div>
        </li>
        <li><img src="images/demo/3.gif" alt="" />
          <div class="floater">
            <h2>Step 3</h2>
            <p>Temperinte interdum sempus odio urna eget curabitur semper convallis nunc laoreet. Nullain convallis ris elis vest liberos nis diculis feugiat in rutrum. Suspendreristibulumfaucibulum lobortor quis tortortor ris sapien sce enim et volutpat sus. Urnaretiumorci orci fauctor leo justo nulla cras ridiculum&hellip;</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
          </div>
        </li>
      </ul>
    </div>
    <a href="javascript:void(0);" id="featured-item-prev"><img src="layout/images/prev.png" alt="" /></a> <a href="javascript:void(0);" id="featured-item-next"><img src="layout/images/next.png" alt="" /></a> </div>
</div>
<!-- ####################################################################################################### -->
<div class="Login">
	<div id="login_form">
		<div  id="newpost1" style="display:block;"> 
			
			<table width="50%" border="0px" border-style="none" cellpadding="0" cellspacing="1" bgcolor="white" align="center">
		<tr>
		<form name="form2" method="post" action="checklogin.php" >
		<td>
		<table width="50%" border="0" cellpadding="3" cellspacing="1" bgcolor="#B2C629" align="center">

		<tr>
		<td width="65">Username</td>
		<td width="3">:</td>
		<td width="208"><input name="myusername" type="text" id="myusername"></td>
		</tr>
		<tr>
		<td>Password</td>
		<td>:</td>
		<td><input name="mypassword" type="password" id="mypassword"></td>
		</tr>
		<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td><input type="submit" name="Submit" value="Login" align="center"></td>
		</tr>
		<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td><p>Invalid Username Or Password</p></td>
		</tr>
		</table>
		</td>
		</form>
		</tr>
		</table>
			</div>
	</div>	

	<div id="login_button">
    	
			 <button id="buttonL" style="margin-top:100px" onClick="showhide()">Login</button>
            
    </div>
</div>	
	
		
<div class="Register">
	<div id="register_form">
		<div  id="newpost2" style="display:none;> 
		<table width="50%" border="0" cellpadding="0" cellspacing="1" bgcolor="white" align="center">
		 <tr>
		<form name="form1" method="post" action="checknewlogin.php" onsubmit="return validateForm2();">
		<td>
		<table width="50%" border="0" cellpadding="3" cellspacing="1" bgcolor="#B2C629" align="center">
		<tr>
		<td width="65">Name</td>
		<td width="3">:</td>
		<td width="208"><input name="myname" type="text" id="myname"></td>
		</tr>
		<tr>
		<td width="65">Email Id</td>
		<td width="3">:</td>
		<td width="208"><input name="myusername" type="text" id="myusername"></td>
		</tr>
		<tr>
		<td width="65">Username</td>
		<td width="3">:</td>
		<td width="208"><input name="myusername" type="text" id="myusername"></td>
		</tr>
		<tr>
		<td>Password</td>
		<td>:</td>
		<td><input name="mypassword" type="password" id="mypassword"></td>
		</tr>
		<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td><input type="submit" name="Submit" value="Confirm"></td>
		</tr>
		</table>
		</td>
		</form>
		</tr>
		</table>
		</div>
	</div>
	
  	     
	<div id="register_button">
    	
			 <button id="buttonR" onClick="showhide2()">Register</button>
            
    </div>
</div>		
<!-- ####################################################################################################### -->
<div class="wrapper col3">
  <div id="container">
    <div class="homepage">
      <ul>
        <li>
          <h2><img src="images/demo/60x60.gif" alt="" />Nullamlacus dui ipsum conseque loborttis</h2>
          <p>Nullamlacus dui ipsum conseque loborttis non euisque morbi penas dapibulum orna. Urnaultrices quis curabitur phasellentesque congue magnis vestibulum quismodo nulla et feugiat. Adipisciniapellentum leo ut consequam ris felit elit id nibh sociis malesuada.</p>
          <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </li>
        <li>
          <h2><img src="images/demo/60x60.gif" alt="" />Nullamlacus dui ipsum conseque loborttis</h2>
          <p>Nullamlacus dui ipsum conseque loborttis non euisque morbi penas dapibulum orna. Urnaultrices quis curabitur phasellentesque congue magnis vestibulum quismodo nulla et feugiat. Adipisciniapellentum leo ut consequam ris felit elit id nibh sociis malesuada.</p>
          <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </li>
        <li class="last">
          <h2><img src="images/demo/60x60.gif" alt="" />Nullamlacus dui ipsum conseque loborttis</h2>
          <p>Nullamlacus dui ipsum conseque loborttis non euisque morbi penas dapibulum orna. Urnaultrices quis curabitur phasellentesque congue magnis vestibulum quismodo nulla et feugiat. Adipisciniapellentum leo ut consequam ris felit elit id nibh sociis malesuada.</p>
          <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </li>
      </ul>
      <br class="clear" />
    </div>
  </div>
</div>
<!-- ####################################################################################################### -->
<!--<div class="wrapper col4">
  <div id="footer">
    <div class="box1">
      <h2>A Little Company Information !</h2>
      <img class="imgl" src="images/demo/imgl.gif" alt="" />
      <p>Morbitincidunt maurisque eros molest nunc anteget sed vel lacus mus semper. Anterdumnullam interdum eros dui urna consequam ac nisl nullam ligula vestassa. Condimentumfelis et amet tellent quisquet a leo lacus nec augue</p>
      <p>Portortornec condimenterdum eget consectetuer condis.</p>
    </div>
    <div class="box contactdetails">
      <h2>Our Contact Details !</h2>
      <ul>
        <li>Company Name</li>
        <li>Street Name &amp; Number</li>
        <li>Town</li>
        <li>Postcode/Zip</li>
        <li>Tel: xxxxx xxxxxxxxxx</li>
        <li>Fax: xxxxx xxxxxxxxxx</li>
        <li>Email: info@domain.com</li>
        <li class="last">LinkedIn: <a href="#">Company Profile</a></li>
      </ul>
    </div>
    <div class="box flickrbox">
      <h2>Latest Flickr Images !</h2>
      <div class="wrap">
        <div class="fix"></div>
        <div class="flickr_badge_image" id="flickr_badge_image1"><a href="#"><img src="images/demo/80x80.gif" alt="" /></a></div>
        <div class="flickr_badge_image" id="flickr_badge_image2"><a href="#"><img src="images/demo/80x80.gif" alt="" /></a></div>
        <div class="flickr_badge_image" id="flickr_badge_image3"><a href="#"><img src="images/demo/80x80.gif" alt="" /></a></div>
        <div class="flickr_badge_image" id="flickr_badge_image4"><a href="#"><img src="images/demo/80x80.gif" alt="" /></a></div>
        <div class="flickr_badge_image" id="flickr_badge_image5"><a href="#"><img src="images/demo/80x80.gif" alt="" /></a></div>
        <div class="flickr_badge_image" id="flickr_badge_image6"><a href="#"><img src="images/demo/80x80.gif" alt="" /></a></div>
        <div class="fix"></div>
      </div>
    </div>
    <br class="clear" />
  </div>
</div>-->
<!-- ####################################################################################################### -->
<div class="wrapper col5">
  <div id="copyright">
    <p class="fl_left">Copyright &copy; 2014 - All Rights Reserved - <a href="#">Domain Name</a></p>
    <p class="fl_right">Template by <a target="_blank" href="http://www.os-templates.com/" title="Free Website Templates">OS Templates</a></p>
    <br class="clear" />
  </div>
</div>
</body>
</html>