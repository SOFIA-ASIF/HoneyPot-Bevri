<?php
include 'db.php';

$page = $_GET['page'] ?? 'home';

$ip = $_SERVER['REMOTE_ADDR'];
$ua = $_SERVER['HTTP_USER_AGENT'];
$params = "page=$page";

shell_exec("python3 ../app/log_handler.py $ip '$ua' '/php/page.php' '$params'");

echo "<h2>You are viewing page: $page</h2>";
?>
