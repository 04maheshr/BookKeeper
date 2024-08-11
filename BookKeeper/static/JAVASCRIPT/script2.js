async function search_button(event) {
    var search_input = document.getElementById('search-input').value;
    console.log(search_input);

    try {
        const response = await fetch("/search", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ search: search_input })
        });
        const data = await response.json();
        const content = data.data;
        const tableBody = document.getElementById("book-details-table-values");
        tableBody.innerHTML = '';

        content.forEach(row => {
            const rowElement = document.createElement("tr");
            row.forEach((cellData, index) => {
                const cell = document.createElement("td");
                cell.textContent = cellData;
                rowElement.appendChild(cell);
                if (index === 0) {
                    cell.setAttribute("contenteditable", "false"); // make regNo non-editable
                } else {
                    cell.setAttribute("contenteditable", "true"); // make other cells editable
                }
            });
            
            const editCell = document.createElement("td");
            const editButton = document.createElement("button");
            editButton.textContent = "Edit";
            editButton.onclick = () => saveChanges(rowElement);
            editCell.appendChild(editButton);
            rowElement.appendChild(editCell);

            tableBody.appendChild(rowElement);
        });
    } catch (error) {
        console.error("Error:", error);
    }
}

async function saveChanges(row) {
    const cells = row.getElementsByTagName("td");
    const regNo = cells[0].textContent || null;
    const rackNo = cells[1].textContent || null;
    const rackSide = cells[2].textContent || null;
    const rowNo = cells[3].textContent || null;
    const pagupuEn = cells[4].textContent || null;
    const pathivuEn = cells[5].textContent || null;
    const title = cells[6].textContent || null;
    const author = cells[7].textContent || null;
    const year = cells[8].textContent || null;
    const rate = cells[9].textContent || null;
    console.log(rackNo)

    try {
        const response = await fetch("/update", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                regNo, 
                pathivuEn, 
                pagupuEn, 
                title, 
                author, 
                rate, 
                year, 
                rackNo, 
                rackSide, 
                rowNo 
            })
        });
        const data = await response.json();
        alert(data.message);
    } catch (error) {
        console.error("Error:", error);
    }
}

