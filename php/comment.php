<?php
session_start();
include '../db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Check if the user is logged in and get the username
    if (isset($_SESSION['username'])) {
        $username = $_SESSION['username'];
    } else {
        $username = "Anonymous";
    }

    $comment = mysqli_real_escape_string($conn, $_POST['comment']);
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $ip_address = $_SERVER['REMOTE_ADDR'];

    // Save comment to the database using a prepared statement
    $stmt = $conn->prepare("INSERT INTO comments (username, comment) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $comment);

    if ($stmt->execute()) {
        echo "Comment submitted successfully!";

        // Log the comment submission
        $activity = "Comment submitted: " . $comment;
        $command = "python ../app/log_handler.py '$ip_address' '$username' '' '$user_agent' '$activity'";
        exec($command);
    } else {
        echo "Error submitting comment: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>
