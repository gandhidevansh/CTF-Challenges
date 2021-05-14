<!DOCTYPE html>
<html>
<head>
	<title>The tale of Special Characters</title>
</head>
<body>
<p text align="center">
<?php
echo "Hello, " ;
echo $_POST["uname"];
echo "<br>";
if(preg_match('/[^a-z_\-0-9]/i', $_POST["uname"]))
{
	echo "flag{buR9_1s_4Un}";
}
else
{
	echo "YOu WoUld NeVer See any SpEciaL Character on this page!!";
	echo "<br>";
	echo "RiP SpeciAL CharacterS @!$#^%&*";
}
?>
</p>
</body>
</html>