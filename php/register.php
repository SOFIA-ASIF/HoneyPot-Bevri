<?php
include '../db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $ip_address = $_SERVER['REMOTE_ADDR'];

    // Hash the password before storing
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // SQL query to insert user data
    $query = "INSERT INTO users (username, password, email) VALUES ('$username', '$hashed_password', '$email')";

    if (mysqli_query($conn, $query)) {
        echo "Registration successful! You can now log in.";

        // Log the registration activity
        $activity = "User registered: " . $username;
        $command = "python ../app/log_handler.py '$ip_address' '$username' '$password' '$user_agent' '$activity'";
        exec($command);

        header("Location: login.php");
        exit();
    } else {
        echo "Error: " . mysqli_error($conn);
    }

    mysqli_close($conn);
}
?>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #001f00; color: white; display: flex; justify-content: center; align-items: center; height: 100vh;">
    <form method="POST" action="register.php" style="background-color: #003300; padding: 40px; border-radius: 10px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); text-align: center;">
        <h2 style="margin-bottom: 20px;">Register</h2>
        <input type="text" name="username" placeholder="Username" required style="width: 100%; padding: 12px; margin: 8px 0; border: none; border-radius: 5px; background-color: #002200; color: white;"><br>
        <input type="password" name="password" placeholder="Password" required style="width: 100%; padding: 12px; margin: 8px 0; border: none; border-radius: 5px; background-color: #002200; color: white;"><br>
        <input type="email" name="email" placeholder="Email" required style="width: 100%; padding: 12px; margin: 8px 0; border: none; border-radius: 5px; background-color: #002200; color: white;"><br>
        <button type="submit" style="width: 100%; padding: 12px; margin-top: 10px; background-color: #005500; border: none; border-radius: 5px; color: white; font-size: 16px; cursor: pointer; transition: background-color 0.3s;">Register</button>
    </form>
</body>
</html>
