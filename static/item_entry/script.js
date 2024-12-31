let table_forming = document.querySelector('.tablesss');
const container = document.getElementById('test');
// console.log(container);
let data = [
    1, 'ABC Traders', '12345', '9876543210', 'Shirt', '1001', 'M', 500.0, 800.0, 50,
    2, 'XYZ Supplies', '67890', '1234567890', 'Trousers', '1002', 'L', 700.0, 1100.0, 30,
    3, 'PQR Wholesale', '11111', '4561237890', 'Jacket', '2003', 'XL', 1200.0, 1800.0, 15,
    4, 'LMN Retail', '22222', '7894561230', 'Jeans', '3004', 'S', 600.0, 900.0, 40,
    5, 'DEF Corporation', '33333', '3216549870', 'Cap', '4005', 'Free', 200.0, 350.0, 100,
    6, 'GHI Imports', '44444', '6547891230', 'Shoes', '5006', '42', 1500.0, 2500.0, 20,
    7, 'JKL Distributors', '55555', '9873216540', 'T-shirt', '6007', 'M', 400.0, 600.0, 75,
    8, 'MNO Supplies', '66666', '1237894560', 'Sweater', '7008', 'L', 1000.0, 1500.0, 25,
    9, 'RST Exporters', '77777', '7891234560', 'Scarf', '8009', 'One Size', 300.0, 500.0, 60,
    10, 'UVW Traders', '88888', '3219876540', 'Hat', '9010', 'Adjustable', 250.0, 450.0, 80
];

let id = [];
let party_name = [];
let bill_no = [];
let barcode = [];
let item_name = [];
let article_no = [];
let size = [];
let purchase_price = [];
let sale_price = [];
let quantity = [];

// Loop through the data array and extract values into respective arrays
for (let i = 0; i < data.length; i += 10) {
    id.push(data[i]);
    party_name.push(data[i + 1]);
    bill_no.push(data[i + 2]);
    barcode.push(data[i + 3]);
    item_name.push(data[i + 4]);
    article_no.push(data[i + 5]);
    size.push(data[i + 6]);
    purchase_price.push(data[i + 7]);
    sale_price.push(data[i + 8]);
    quantity.push(data[i + 9]);
}
let htmlContent = ''; // Initialize the variable to store the concatenated HTML

for (let i = 0; i < id.length; i++) {
    // Concatenate the HTML string after each iteration
    htmlContent += `
        <tr>
            <td>${id[i]}</td>
            <td>${barcode[i]}</td>
            <td>${item_name[i]}</td>
            <td>${article_no[i]}</td>
            <td>${size[i]}</td>
            <td>${purchase_price[i]}</td>
            <td>${sale_price[i]}</td>
            <td>${quantity[i]}</td>
            <td>${party_name[i]}</td>
            <td>${bill_no[i]}</td>
            <td>
                <button class="btn btn-primary btn-sm me-2">Edit</button>
                <button class="btn btn-danger btn-sm">Delete</button>
            </td>
        </tr>`;
}
console.log(htmlContent);
// At the end of the loop, you can output the result
table_forming.innerHTML=htmlContent;