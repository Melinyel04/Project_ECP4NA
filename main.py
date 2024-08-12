import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Presença em Sala de Aula"

    # Funções de Check-In e Check-Out
    def check_in(e):
        student_id = student_id_field.value
        if student_id:
            message.value = f"Check-in realizado para o aluno ID: {student_id}"
            page.update()
        else:
            message.value = "Por favor, insira o ID do aluno."
            page.update()

    def check_out(e):
        student_id = student_id_field.value
        if student_id:
            message.value = f"Check-out realizado para o aluno ID: {student_id}"
            page.update()
        else:
            message.value = "Por favor, insira o ID do aluno."
            page.update()

    # Campo para ID do Aluno
    student_id_field = ft.TextField(label="ID do Aluno")

    # Botões de Check-In e Check-Out
    check_in_button = ft.ElevatedButton(text="Check-In", on_click=check_in)
    check_out_button = ft.ElevatedButton(text="Check-Out", on_click=check_out)

    # Mensagem de Feedback
    message = ft.Text()

    # Layout da Página
    page.add(
        student_id_field,
        check_in_button,
        check_out_button,
        message,
    )

ft.app(target=main)
