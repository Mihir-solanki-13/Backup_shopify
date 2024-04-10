// import React from 'react';

// function Card() {
//   // Sample data for rows
//   const rows = [
//     { id: 1, name: 'Product' },
//     { id: 2, name: 'Smart Collections' },
//     { id: 3, name: 'Custom Collections' },
//     { id: 4, name: 'Themes' },
//     { id: 5, name: 'Blogs' },
//     { id: 6, name: 'Files' },
//     { id: 7, name: 'Saved Searches' },
//     { id: 8, name: 'Pages' },
//     { id: 9, name: 'Inventories' },
//     { id: 10, name: 'Policies' },
//     { id: 11, name: 'Shipping Zones' },
//     { id: 12, name: 'Customers' },
//     { id: 13, name: 'Orders' }
//   ];

//   // Click handler for rows
//   const handleRowClick = (id) => {
//     alert(`Clicked row with ID: ${id}`);
//   };

//   return (
//     <div className="card-container">
//       <div className="card">
//         <div className="card-header">
//           <h2>Backup Your Data</h2>
//         </div>
//         <div className="card-body">
//           {rows.map(row => (
//             <a key={row.id} href="#" onClick={() => handleRowClick(row.id)} className="row">
//               <div className="row-cell">
//                 <h4><strong>{row.name}</strong></h4>
//               </div>
//             </a>
//           ))}
//         </div>
//       </div>
//       <style>
//         {`
//           .card-container {
//             display: flex;
//             justify-content: center;
//             align-items: center;
//             min-height: 100vh;
//           }

//           .card {
//             border: 1px solid #ccc;
//             border-radius: 5px;
//             width: 80%;
//             max-width: 600px;
//             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
//           }

//           .card-header {
//             background-color: #f0f0f0;
//             padding: 10px;
//             border-bottom: 1px solid #ccc;
//             border-radius: 5px 5px 0 0;
//           }

//           .card-header h2 {
//             margin: 0;
//             font-family: Arial, sans-serif;
//           }

//           .card-body {
//             padding: 20px;
//           }

//           .row {
//             margin-bottom: 5px;
//             text-decoration: none;
//             color: inherit;
//             font-family: Arial, sans-serif; /* Change font family */
//             font-size: 14px; /* Adjust font size */
//           }

//           .row:hover {
//             background-color: #f0f0f0;
//           }

//           .row-cell {
//             padding: 13px; /* Reduce padding */
//             border: 1px solid #ccc;
//             border-radius: 5px;
//             background-color: #f9f9f9;
//           }

//           .row-cell h4 {
//             margin: 0;
//           }
//         `}
//       </style>
//     </div>
//   );
// }

// export default Card;
