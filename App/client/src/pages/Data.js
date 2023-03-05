import React from 'react';
import { useState, useEffect } from 'react';
import '../styles/pages.css';

function Data() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch('/rankings').then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    
    return (
        <div className='page'>
           <h2>Data</h2>
            {(typeof data.rankings === 'undefined') ? (
                <p><img src={require('../assets/loading.gif')} alt="loading" id='loader'/></p>
            ):(
                data.rankings.map((member, index) => (
                    <p key={index}>{member[0]}</p>
                ))
            )}
        </div>
    );
}

export default Data;