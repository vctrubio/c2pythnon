from dash import Dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from controller import Ticket, add_ticket, delete_ticket, print_all_tickets, engine

app = Dash(__name__)

# Configure the database connection
DATABASE_URL = "postgresql://client:password@localhost:5432/tickets_python"
app.server.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app.server)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    category = db.Column(db.Enum('A', 'B', 'C', 'D'), default='D')
    quantity = db.Column(db.Integer, default=1)

# Create database tables
db.create_all()

# Dash layout
app.layout = html.Div([
    html.H1("Ticket Management"),
    
    # Add Ticket Form
    html.Div([
        html.H3("Add New Ticket"),
        dcc.Input(id='ticket-name', type='text', placeholder='Enter ticket name'),
        dcc.Input(id='ticket-price', type='number', placeholder='Enter ticket price'),
        dcc.Dropdown(
            id='ticket-category',
            options=[
                {'label': 'Jardeniria', 'value': 'A'},
                {'label': 'Gasolina', 'value': 'B'},
                {'label': 'Vivienda', 'value': 'C'},
                {'label': 'Other', 'value': 'D'}
            ],
            value='D',
            placeholder="Select category"
        ),
        dcc.Input(id='ticket-quantity', type='number', value=1),
        html.Button('Add Ticket', id='add-ticket-button'),
    ]),
    
    # Display All Tickets
    html.Div([
        html.H3("All Tickets"),
        html.Table(
            id='tickets-table',
            children=[
                html.Tr([
                    html.Th("ID"),
                    html.Th("Name"),
                    html.Th("Price"),
                    html.Th("Paid"),
                    html.Th("Category"),
                    html.Th("Quantity"),
                    html.Th("Actions"),
                ]),
            ],
        ),
    ]),
])

# Callback to add a new ticket
@app.callback(
    Output('tickets-table', 'children'),
    [Input('add-ticket-button', 'n_clicks')],
    [State('ticket-name', 'value'),
     State('ticket-price', 'value'),
     State('ticket-category', 'value'),
     State('ticket-quantity', 'value')]
)
def add_ticket(n_clicks, name, price, category, quantity):
    if not n_clicks:
        raise PreventUpdate

    # Perform the add_ticket operation here
    with db.session_scope() as session:
        ticket = Ticket(name=name, price=price, category=category, quantity=quantity)
        session.add(ticket)
        session.commit()

    # Update the table with all tickets
    return generate_table(get_all_tickets())

# Callback to display all tickets
@app.callback(
    Output('tickets-table', 'children'),
    [Input('add-ticket-button', 'n_clicks')]
)
def display_all_tickets(n_clicks):
    if not n_clicks:
        raise PreventUpdate

    # Update the table with all tickets
    return generate_table(get_all_tickets())

# Helper function to generate HTML table from tickets
def generate_table(tickets):
    rows = []
    for ticket in tickets:
        rows.append(html.Tr([
            html.Td(ticket.id),
            html.Td(ticket.name),
            html.Td(ticket.price),
            html.Td("Paid" if ticket.paid else "Not Paid"),
            html.Td(ticket.category),
            html.Td(ticket.quantity),
            html.Td(html.Button('Update', id=f'update-button-{ticket.id}')),
            html.Td(html.Button('Delete', id=f'delete-button-{ticket.id}')),
        ]))
    return rows

if __name__ == '__main__':
    app.run_server(debug=True)
