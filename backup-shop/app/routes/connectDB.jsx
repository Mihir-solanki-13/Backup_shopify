// Shopify Remix project
import React, { useState } from 'react';
import axios from 'axios';

function Card() {
    const [selectedObjectType, setSelectedObjectType] = useState('');
    const [restoreId, setRestoreId] = useState('');

    const handleBackup = () => {
        if ('True') {
            axios.get(`http://127.0.0.1:8000/backup/products/`)
                .then(response => {
                    console.log(response.data);
                    // Handle success
                })
                .catch(error => {
                    console.error(error);
                    // Handle error
                });
        } else {
            console.error('Please select an object type');
        }
    };

    const handleRestore = () => {
        if (restoreId) {
            axios.get(`http://your-django-api-url/api/restore`)
                .then(response => {
                    console.log(response.data);
                    // Handle success
                })
                .catch(error => {
                    console.error(error);
                    // Handle error
                });
        } else {
            console.error('Please provide an ID for restore');
        }
    };

    return (
        <div className="card-container">
            {/* Your card component content */}
            <button onClick={handleBackup}>Backup</button>
            <button onClick={handleRestore}>Restore</button>
        </div>
    );
}

export default Card;
