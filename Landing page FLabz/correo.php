<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $recipient = "proyectos@fantazylabz.tech"; // Cambia esto a tu dirección de correo electrónico deseada
    $subject = $_POST["asunto"];
    $senderEmail = $_POST["correo"];
    $message = $_POST["mensaje"];
    
    $headers = "From: $senderEmail\r\n";
    $headers .= "Reply-To: $senderEmail\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

    $body = "
    <html>
    <head>
        <title>$subject</title>
    </head>
    <body>
        <p><b>Email:</b> $senderEmail</p>
        <p><b>Mensaje:</b></p>
        <p>$message</p>
    </body>
    </html>
    ";

    if (mail($recipient, $subject, $body, $headers)) {
        echo "¡Email enviado exitosamente!";
    } else {
        echo "No se pudo enviar el correo electrónico.";
    }
}
?>
