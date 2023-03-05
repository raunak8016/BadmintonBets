import React from 'react';
import { useState, useEffect } from 'react';

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
        <div>
           <h2>Data</h2>
            {(typeof data.rankings === 'undefined') ? (
                <p>Loading...</p>
            ):(
                data.rankings.map((member, index) => (
                    <p key={index}>{member}</p>
                ))
            )}
        </div>
    );
}

export default Data;