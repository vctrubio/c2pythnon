import React, { useState, useEffect } from 'react';
import api from './api'

const App = () => {
  const [transactions, setTransactions] = useState([])
  const [formData, setFormData] = useState({
    amount: '',
    category: '',
    description: '',
    is_income: false
  }); //must be the same as model in the backend

  const fetchTransactions = async () => {
    try {
      const response = await api.get('/transactions/')
      setTransactions(response.data);
    } catch (error) {
      console.error('Error fetching transactions:', error);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value
    })
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    if (!formData.amount || !formData.category || !formData.description) {
      alert('Please fill out all fields');
      return;
    }

    try {
      await api.post('/transactions/', formData);
      fetchTransactions();
      setFormData({
        amount: '',
        category: '',
        description: '',
        is_income: false
      });
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  }

  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href='#'>
            Finance App
          </a>
        </div>
      </nav>
      <div className='container'>
        <form onSubmit={handleFormSubmit}>

          <div className='mb-3'>
            <label htmlFor='amount' className='form-label'>
              Amount
            </label>
            <input type='text' className='form-control' id='amount' name='amount' onChange={handleInputChange} value={formData.amount} />
          </div>

          <div className='mb-3'>
            <label htmlFor='category' className='form-label'>
              category
            </label>
            <input type='text' className='form-control' id='category' name='category' onChange={handleInputChange} value={formData.category} />
          </div>

          <div className='mb-3'>
            <label htmlFor='description' className='form-label'>
              description
            </label>
            <input type='text' className='form-control' id='description' name='description' onChange={handleInputChange} value={formData.description} />
          </div>

          <div className='mb-3'>
            <label htmlFor='is_income' className='form-label'>
              Income?
            </label>
            <input type='checkbox' id='is_income' name='is_income' onChange={handleInputChange} value={formData.is_income} />
          </div>

          <button type='submit' className='btn btn-primary'>
            SUBMIT
          </button>
        </form>

        <table className='table table-striped table-bordered table-hover'>
          <thead>
            <tr>
              <th scope='col'>Amount</th>
              <th scope='col'>Category</th>
              <th scope='col'>Description</th>
              <th scope='col'>Income?</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((transaction) => (
              <tr key={transaction.id}>
                <td>{transaction.amount}</td>
                <td>{transaction.category}</td>
                <td>{transaction.description}</td>
                <td>{transaction.is_income ? 'Yes' : 'No'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default App;