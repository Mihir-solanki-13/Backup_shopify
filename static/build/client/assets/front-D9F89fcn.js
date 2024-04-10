import{j as e}from"./jsx-runtime-DDP7-w6c.js";function n(){const a=[{id:1,name:"Product"},{id:2,name:"Smart Collections"},{id:3,name:"Custom Collections"},{id:4,name:"Themes"},{id:5,name:"Blogs"},{id:6,name:"Files"},{id:7,name:"Saved Searches"},{id:8,name:"Pages"},{id:9,name:"Inventories"},{id:10,name:"Policies"},{id:11,name:"Shipping Zones"},{id:12,name:"Customers"},{id:13,name:"Orders"}],d=r=>{alert(`Clicked row with ID: ${r}`)};return e.jsxs("div",{className:"card-container",children:[e.jsxs("div",{className:"card",children:[e.jsx("div",{className:"card-header",children:e.jsx("h2",{children:"Backup Your Data"})}),e.jsx("div",{className:"card-body",children:a.map(r=>e.jsx("a",{href:"#",onClick:()=>d(r.id),className:"row",children:e.jsx("div",{className:"row-cell",children:e.jsx("h4",{children:e.jsx("strong",{children:r.name})})})},r.id))})]}),e.jsx("style",{children:`
          .card-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
          }

          .card {
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 80%;
            max-width: 600px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
          }

          .card-header {
            background-color: #f0f0f0;
            padding: 10px;
            border-bottom: 1px solid #ccc;
            border-radius: 5px 5px 0 0;
          }

          .card-header h2 {
            margin: 0;
            font-family: Arial, sans-serif;
          }

          .card-body {
            padding: 20px;
          }

          .row {
            margin-bottom: 5px;
            text-decoration: none;
            color: inherit;
            font-family: Arial, sans-serif; /* Change font family */
            font-size: 14px; /* Adjust font size */
          }

          .row:hover {
            background-color: #f0f0f0;
          }

          .row-cell {
            padding: 13px; /* Reduce padding */
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
          }

          .row-cell h4 {
            margin: 0;
          }
        `})]})}export{n as default};
