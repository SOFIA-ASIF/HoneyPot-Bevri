<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'];
    $comment = $_POST['comment'];

    // ⚠️ Vulnerable: No sanitization (XSS)
    file_put_contents("logs/attacks.log", "XSS Attempt: $name - $comment\n", FILE_APPEND);
}
header("Location: index.html");
exit();
?>
