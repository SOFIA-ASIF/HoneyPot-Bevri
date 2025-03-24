<?php
session_start();
include '../db.php';

// Enable error reporting
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = isset($_SESSION['username']) ? $_SESSION['username'] : "Anonymous";

    // Vulnerable: Directly using $_POST['comment'] without sanitization
    $comment = $_POST['comment'];
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $ip_address = $_SERVER['REMOTE_ADDR'];

    // Save comment (still using prepared statements to prevent SQL injection)
    $stmt = $conn->prepare("INSERT INTO comments (username, comment) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $comment);

    if ($stmt->execute()) {
        // Directly echoing the unescaped comment (XSS vulnerability)
        echo "Comment submitted successfully! ".$comment ;

        // Log the comment submission
        $pythonPath = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe";
        $scriptPath = "C:\\xampp\\htdocs\\HoneyPot\\app\\log_handler.py";
        $activity = "Comment submitted: " . $comment;

        // Construct raw shell command (no escaping for honeypot vulnerability)
        $command = "\"$pythonPath\" \"$scriptPath\" \"$ip_address\" \"$username\" \" \" \"$user_agent\" \"$activity\"";


    } else {
        echo "Error submitting comment: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>
