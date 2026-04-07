import reflex as rx
import pandas as pd

# Load CSV
data = pd.read_csv("cleaned_data.csv")

class SearchState(rx.State):
    search_query: str = ""

    @rx.var
    def filtered_products(self) -> list[dict]:
        results = []

        for _, row in data.iterrows():
           if self.search_query.lower() in str(row["Name"]).lower():
                results.append({
                    "name": row["Name"],
                    "desc": str(row.get("Category", "No category"))
                })

        return results


class LoginState(rx.State):
    def handle_login(self, form_data: dict):
        password = form_data.get("password")

        if len(password) < 6:
            return rx.toast.error("Password must be at least 6 characters")

        return rx.toast.success("Login Successful!")


def product_card(item):
    return rx.box(
        rx.text(item["name"], font_weight="bold"),
        rx.text(item["desc"]),
        border="1px solid gray",
        padding="10px"
    )


def product_grid():
    return rx.grid(
        rx.foreach(
            SearchState.filtered_products,
            lambda item: product_card(item)
        ),
        columns="4",
        spacing="4",
        width="100%",
    )


def search_bar():
    return rx.input(
        placeholder="Search products...",
        on_change=SearchState.set_search_query
    )


def index():
    return rx.vstack(
        rx.heading("AI E-Commerce"),
        search_bar(),
        product_grid()
    )


def login():
    return rx.form(
        rx.vstack(
            rx.heading("Login"),
            rx.input(name="email", placeholder="Email"),
            rx.input(name="password", type="password"),
            rx.button("Login", type="submit"),
        ),
        on_submit=LoginState.handle_login
    )


app = rx.App()
app.add_page(index)
app.add_page(login, route="/login")