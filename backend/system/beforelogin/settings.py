import re

def verificar_senha(senha):
    exigencias = []

    if len(senha) < 8:
        exigencias.append("A senha deve ter pelo menos 8 caracteres.")

    if not any(c.isupper() for c in senha):
        exigencias.append("A senha deve conter pelo menos uma letra maiúscula.")

    if not any(c.islower() for c in senha):
        exigencias.append("A senha deve conter pelo menos uma letra minúscula.")

    if not any(c.isdigit() for c in senha):
        exigencias.append("A senha deve conter pelo menos um número.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        exigencias.append("A senha deve conter pelo menos um caractere especial (!@#$%^&*(),.?\":{}|<>).")

    if exigencias:
        return "<br>".join(exigencias)

    return None

