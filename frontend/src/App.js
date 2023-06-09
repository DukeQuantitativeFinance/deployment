import React, { useState, useEffect } from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';

import './App.css';
import DiscreteHome from './discrete_exchange/DiscreteHome';
import DiscreteSubmit from './discrete_exchange/DiscreteSubmit';
import DiscreteResults from './discrete_exchange/DiscreteResults';
import DiscreteStart from './discrete_exchange/DiscreteStart';
import CustomerFlowSubmit from './customer_flow/CustomerFlowSubmit';
import CustomerFlowResults from './customer_flow/CustomerFlowResults';

function App() {
  const [id, setId] = useState(null);

  return (
    <div className='App'>
      <Routes>
        {/* DISCRETE EXCHANGE HOME PAGE */}
        <Route
          exact
          path={'/discrete'}
          element={<DiscreteHome />}
        />

        {/* DISCRETE EXCHANGE SUBMIT PAGE */}
        <Route
          exact
          path={'/discrete/submit'}
          element={
            <DiscreteSubmit
              id={id}
              setId={setId}
            />
          }
        />

        {/* DISCRETE EXCHANGE RESULTS PAGE */}
        <Route
          exact
          path={'/discrete/results'}
          element={
            <DiscreteResults 
              id={id}
              setId={setId}
            />
          }
        />

        {/* DISCRETE EXCHANGE START PAGE */}
        <Route
          exact
          path={'/discrete/start'}
          element={<DiscreteStart />}
        />

        {/* CUSTOMER FLOW HOME PAGE */}
        <Route
          exact
          path={'/customer-flow'}
          // element={< />}
        />

        {/* CUSTOMER FLOW SUBMIT PAGE */}
        <Route
          exact
          path={'/customer-flow/submit'}
          element={
            <CustomerFlowSubmit
              id={id}
              setId={setId}
            />
          }
        />

        {/* CUSTOMER FLOW RESULTS PAGE */}
        <Route
          exact
          path={'/customer-flow/results'}
          element={
            <CustomerFlowResults 
              id={id}
              setId={setId}
            />
          }
        />

        {/* CUSTOMER FLOW START PAGE */}
        <Route
          exact
          path={'/customer-flow/start'}
          element={<DiscreteStart />}
        />
      </Routes>
    </div>
  );
}

export default App;
