<?php
include 'db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Prepare SQL query
    $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    $result = mysqli_query($conn, $query);

    if ($result && mysqli_num_rows($result) > 0) {
        // Successful login - redirect to the main website page (index.html)
        header("Location: index.html");
        exit();
    } else {
        // Failed login - show error message
        echo "Invalid username or password.";
    }
}
?>
