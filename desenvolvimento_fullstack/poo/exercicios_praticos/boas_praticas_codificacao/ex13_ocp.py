# ============================================
# EXERCÍCIO 13 – OCP (OPEN-CLOSED PRINCIPLE)
# --------------------------------------------
# O código deve permitir adicionar novos tipos 
# sem alterar as classes existentes.
# ============================================


class Messenger:
    def send(self, message: str):
        raise NotImplementedError("Implementa metodo send()")


class MailMessenger(Messenger):
    def send(self, message: str):
        print(f"Envio de Email: {message}")


class SmsMessenger(Messenger):
    def send(self, message: str):
        print(f"Envio de Mensagem: {message}")


class NotificationService:
    def __init__(self, messenger: Messenger):
        self.messenger = messenger

    def notify(self, message: str):
        self.messenger.send(message)


# ======================
# TESTANDO O CÓDIGO
# ======================
if __name__ == "__main__":
    mail = NotificationService(MailMessenger())
    mail.notify("Bem vinda(o) Fulano")

    sms = NotificationService(SmsMessenger())
    sms.notify("Seu código é 649")