<?php
// Vérifier si le formulaire a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Vérifier si l'adresse e-mail a été spécifiée
    if (!empty($_POST["email"])) {
        // Récupérer l'adresse e-mail saisie dans le formulaire
        $email = $_POST["email"];

        // Adresses e-mail de réception (séparées par des virgules si plusieurs)
        $to = "votre@email.com";

        // Sujet de l'e-mail
        $subject = "Nouveau message depuis votre site web";

        // Contenu de l'e-mail
        $message = "Adresse e-mail du contact : " . $email;

        // En-têtes de l'e-mail
        $headers = "From: " . $email . "\r\n";
        $headers .= "Reply-To: " . $email . "\r\n";

        // Envoyer l'e-mail
        if (mail($to, $subject, $message, $headers)) {
            echo "Votre e-mail a été envoyé avec succès.";
        } else {
            echo "Une erreur s'est produite lors de l'envoi de l'e-mail.";
        }
    } else {
        echo "Veuillez saisir une adresse e-mail.";
    }
}
?>