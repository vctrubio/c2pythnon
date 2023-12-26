import React from 'react';

const TicketCard = ({ ticket }) => {
  return (
    <div className="card" style={{ width: '18rem' }}>
      <div className="card-body">
        <h5 className="card-title">{ticket.name}</h5>
        <h6 className="card-subtitle mb-2 text-muted">Ticket ID: {ticket.id}</h6>
        <p className="card-text">Price: ${ticket.price}</p>
        <p className="card-text">Quantity: {ticket.quantity}</p>
        <p className="card-text">Paid: {ticket.paid ? 'Yes' : 'No'}</p>
        <p className="card-text">Person ID: {ticket.person_id}</p>
      </div>
    </div>
  );
};

export default TicketCard;