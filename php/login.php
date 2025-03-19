<?php
include 'db.php';
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    $result = mysqli_query($conn, $query);

    $ip = $_SERVER['REMOTE_ADDR'];
    $ua = $_SERVER['HTTP_USER_AGENT'];
    $params = "username=$username&password=$password";

    shell_exec("python3 ../app/log_handler.py $ip '$ua' '/php/login.php' '$params'");

    if (mysqli_num_rows($result) > 0) {
        echo "Login Successful!";
    } else {
        echo "Invalid Credentials!";
    }
}
?>

<form method="POST" action="">
    <h2>Login</h2>
    <input type="text" name="username" placeholder="Username" required><br>
    <input type="password" name="password" placeholder="Password" required><br>
    <button type="submit">Login</button>
</form>
