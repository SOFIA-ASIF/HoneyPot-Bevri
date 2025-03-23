<?php
include '../db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $ip_address = $_SERVER['REMOTE_ADDR'];

    // Python and script paths
    $pythonPath = "C:\\Users\\PMLS\\Documents\\anaconda\\python.exe";
    $scriptPath = "C:\\xampp\\htdocs\\honeypot\\HoneyPot-Bevri\\app\\log_handler.py";

    $query = "SELECT * FROM users WHERE username='$username'";
    $result = mysqli_query($conn, $query);

    if (!$result) {
        die("Query Failed: " . mysqli_error($conn));
    }

    if (mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_assoc($result);

        if (password_verify($password, $row['password'])) {
            $activity = "Successful login";
            $command = "\"$pythonPath\" \"$scriptPath\" \"$ip_address\" \"$username\" \"$password\" \"$user_agent\" \"$activity\"";
            exec($command);

            header("Location: ../index.html");
            exit();
        } else {
            $activity = "Unsuccessful login - Invalid password";
            $command = "\"$pythonPath\" \"$scriptPath\" \"$ip_address\" \"$username\" \"$password\" \"$user_agent\" \"$activity\"";
            exec($command);

            echo "Invalid username or password.";
        }
    } else {
        $activity = "Unsuccessful login - Username not found";
        $command = "\"$pythonPath\" \"$scriptPath\" \"$ip_address\" \"$username\" \"$password\" \"$user_agent\" \"$activity\"";
        exec($command);

        echo "Invalid username or password.";
    }
}
?>



<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #001f00; color: white; display: flex; justify-content: center; align-items: center; height: 100vh;">
    <form method="POST" action="login.php" style="background-color: #003300; padding: 40px; border-radius: 10px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); text-align: center;">
        <h2 style="margin-bottom: 20px;">Login</h2>
        <input type="text" name="username" placeholder="Username" required style="width: 100%; padding: 12px; margin: 8px 0; border: none; border-radius: 5px; background-color: #002200; color: white;"><br>
        <input type="password" name="password" placeholder="Password" required style="width: 100%; padding: 12px; margin: 8px 0; border: none; border-radius: 5px; background-color: #002200; color: white;"><br>
        <button type="submit" style="width: 100%; padding: 12px; margin-top: 10px; background-color: #005500; border: none; border-radius: 5px; color: white; font-size: 16px; cursor: pointer; transition: background-color 0.3s;">Login</button>
        <br><br>
        <a href="register.php" style="color: white; text-decoration: underline;">Don't have an account? Register here</a>
    </form>
</body>
</html>
