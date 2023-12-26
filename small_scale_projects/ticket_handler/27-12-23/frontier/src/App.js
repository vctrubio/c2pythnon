import React, { useState, useEffect } from 'react';
import api from './api'
import TicketCard from './comp_card';

function App() {
  const [tickets, setTickets] = useState([])
  const [formTicket, setFormTicket] = useState({
    name: '',
    price: '',
    quantity: '',
    paid: false,
    person_id: 1,
  })

  const getTickets = async () => {
    const response = await api.get('/tickets/')
    setTickets(response.data)
  }

  useEffect(() => {
    getTickets();
  }, []);

  return (
    <div>
      <div>
        <h1>Tickets</h1>
        <ul style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '10px' }}>
          {tickets.map(ticket => (
            <ul key={ticket.id} style={{ listStyleType: 'none' }}>
              <TicketCard ticket={ticket} />
            </ul>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;

// delete, create, and then sort 