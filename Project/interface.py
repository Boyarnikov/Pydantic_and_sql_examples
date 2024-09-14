import flet as ft
from models import User
from database import create_connection, create_table, add_user

DB_FILE = "users.db"


def main(page: ft.Page):
    page.title = "User Registration"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    conn = create_connection(DB_FILE)
    create_table(conn)

    def submit_user(e):
        try:
            user_data = User(
                name=name_input.value,
                email=email_input.value,
                age=int(age_input.value),
                address=address_input.value
            )
            user_id = add_user(conn, user_data)
            page.add(ft.Text(f"User added with ID: {user_id}"))

            name_input.value = ""
            email_input.value = ""
            age_input.value = ""
            address_input.value = ""
            page.update()
        except Exception as ex:
            page.add(ft.Text(f"Error: {ex}", color=ft.colors.RED))

    name_input = ft.TextField(label="Name")
    email_input = ft.TextField(label="Email")
    age_input = ft.TextField(label="Age")
    address_input = ft.TextField(label="Address")

    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_user)

    page.add(
        name_input,
        email_input,
        age_input,
        address_input,
        submit_button
    )

    def close_connection(e):
        if conn:
            conn.close()

    page.on_close = close_connection


if __name__ == "__main__":
    ft.app(target=main)
