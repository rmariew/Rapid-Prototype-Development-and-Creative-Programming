<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <?php
    $num1 = $_GET["num1"];
    $num2 = $_GET["num2"];
    $operation = $_GET["operation"];

    if($operation == "add"){
        printf($num1 + $num2);
    }
    else if($operation == "subtract"){
        printf($num1 - $num2);
    }
    else if($operation == "multiply"){
        printf($num1 * $num2);
    }
    else{
        if($num2 == 0){
            printf("You cannot divide by 0");
        }
        else{
            printf($num1/$num2);
        }
    }
    ?>
</body>
</html>