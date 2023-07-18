<?php
session_start();


// connect to the database
$db = mysqli_connect('localhost', 'root', '', 'carehand');

$username=$_SESSION['username'];
$query = "UPDATE rc_register SET status='Not Active' WHERE user_name='$username' ";

$res=mysqli_query($db,$query);


header('location: rcuserhome.php');
?>