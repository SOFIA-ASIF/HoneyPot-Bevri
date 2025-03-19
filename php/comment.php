<?php
include 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $comment = $_POST['comment'];
    $ip = $_SERVER['REMOTE_ADDR'];
    $ua = $_SERVER['HTTP_USER_AGENT'];
    $params = "comment=$comment";

    shell_exec("python3 ../app/log_handler.py $ip '$ua' '/php/comment.php' '$params'");

    $query = "INSERT INTO comments (comment) VALUES ('$comment')";
    mysqli_query($conn, $query);
}
?>

<form method="POST" action="">
    <h2>Leave a Comment</h2>
    <textarea name="comment" placeholder="Your comment here"></textarea><br>
    <button type="submit">Submit</button>
</form>

<h3>Comments:</h3>
<?php
$result = mysqli_query($conn, "SELECT * FROM comments");
while ($row = mysqli_fetch_assoc($result)) {
    echo "<p>{$row['comment']}</p>";  // vulnerable to XSS
}
?>
