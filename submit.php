<?php
include '../db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Directly using POST data without escaping (vulnerable to SQL injection)
    $comment = $_POST['comment'];
    $username = $_POST['username'];

    // Store the comment (vulnerable query)
    $query = "INSERT INTO comments (username, comment) VALUES ('$username', '$comment')";
    if (mysqli_query($conn, $query)) {
        // Log the submission
        $ip_address = $_SERVER['REMOTE_ADDR'];
        $user_agent = $_SERVER['HTTP_USER_AGENT'];
        $activity = "Comment submitted by user: $username";

        // Use escapeshellarg to handle special characters properly
        $command = "python ../app/log_handler.py " . escapeshellarg($ip_address) . " " . escapeshellarg($username) . " 'N/A' " . escapeshellarg($user_agent) . " " . escapeshellarg($activity);
        shell_exec($command);

        echo "Comment submitted successfully.";
    } else {
        echo "Error: " . mysqli_error($conn);
    }
}
?>
