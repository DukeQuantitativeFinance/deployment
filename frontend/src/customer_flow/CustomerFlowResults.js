import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function CustomerFlowResults(props) {
    const [id, setId] = useState(null);
    const [balance, setBalance] = useState(null);
    const [position, setPosition] = useState([]);
    const [netWorth, setNetWorth] = useState(0);

    const nav = useNavigate();

    useEffect(() => {
        setId(props.id);
    }, [props.id])

    axios.post('http://127.0.0.1:5000/customer-flow/results', {
            userId: props.id,
            gameId: 'test_game',
        }, {
            headers: {
                "Content-Type": "multipart/form-data",
            }
        }
    ).then((response) => {
        console.log("response: ", response);
        if (!balance) {
            setBalance(response.data.balance);
            setPosition(response.data.position);
            setNetWorth(response.data.netWorth);
        }
    }).catch((response) => {
        console.log("pnl not found");
    });

    function viewSubmit() {
        nav('/customer-flow/submit');
    }

    return (
        <div>
            View the results of the game
            <br />
            Your id: {props.id}
            <br />
            Your balance: {balance}
            Your position: {position}
            Your netWorth: {netWorth}
            <br />
            <button onClick={viewSubmit}>
                Back
            </button>
        </div>
    );
}

export default CustomerFlowResults;
