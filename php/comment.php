<?php
session_start();
include '../db.php';

// Enable error reporting
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = isset($_SESSION['username']) ? $_SESSION['username'] : "Anonymous";

    $comment = mysqli_real_escape_string($conn, $_POST['comment']);
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $ip_address = $_SERVER['REMOTE_ADDR'];

    // Save comment
    $stmt = $conn->prepare("INSERT INTO comments (username, comment) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $comment);

    if ($stmt->execute()) {
        echo "Comment submitted successfully!";

        // Log the comment submission
        $pythonPath = "C:\\Users\\PMLS\\Documents\\anaconda\\python.exe";
        $scriptPath = "C:\\xampp\\htdocs\\honeypot\\HoneyPot-Bevri\\app\\log_handler.py";
        $activity = "Comment submitted: " . $comment;

        // Construct raw shell command (no escaping for honeypot vulnerability)
        $command = "\"$pythonPath\" \"$scriptPath\" \"$ip_address\" \"$username\" \" \" \"$user_agent\" \"$activity\"";

        // Execute and capture output
        exec($command . " 2>&1", $output, $return_var);

        if ($return_var !== 0) {
            echo " Logging failed:\n" . implode("\n", $output);
        } else {
            echo " Logging succeeded!";
        }

    } else {
        echo "Error submitting comment: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>
