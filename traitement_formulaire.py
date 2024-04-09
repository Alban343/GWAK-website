import smtplib

def send_email(email):
    # Adresses e-mail de réception (séparées par des virgules si plusieurs)
    to = ["gwaktrio@gmail.com"]

    # Sujet de l'e-mail
    subject = "Nouveau message depuis votre site web"

    # Contenu de l'e-mail
    message = f"Adresse e-mail du contact : {email}"

    # Configuration du serveur SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "gwaktrio@gmail.com"
    smtp_password = "charlielove56"

    # Envoyer l'e-mail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to, f"Subject: {subject}\n\n{message}")
        print("Votre e-mail a été envoyé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'envoi de l'e-mail : {e}")

# Appeler la fonction avec l'adresse e-mail saisie dans le formulaire
email = input("Veuillez saisir votre adresse e-mail : ")
send_email(email)