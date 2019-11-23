function buildTable(tableData) {
    // adding table rows and cells to add data from data.js into table format
    var tbody = d3.select('tbody');
    tbody.html('');
    tableData.forEach((report) => {
        console.log(report);
        // tbody.html('');
        var row = tbody.append('tr');
        Object.entries(report).forEach(([key, value]) => {
            console.log(key, value);
            var cell = row.append('td');
            cell.text(value);
            //         });
            //     })
            // }


            // activating the click button/event listener and form

            var button = d3.select('#filter-btn');

            button.on('click', function () {
                // d3.event.preventDefault()
                var inputField = d3.select('#category');
                var inputValue = inputField.property('value');
                console.log('Filter click', inputValue);

                var filteredData = tableData.filter(item => item.category_labels.toLowerCase() === inputValue.toLowerCase());

                console.log(filteredData);

                var outcome = d3.select('#filters');
                tbody.html("")
                filteredData.forEach((entry) => {
                    console.log(entry);
                    var row = tbody.append('tr');

                    Object.entries(entry).forEach(([key, value]) => {
                        console.log(key, value);
                        var cell = row.append('td');
                        cell.text(value);
                    });
                });

            });

        });
    })
}

function init() {
    d3.json(`/beerinfo`).then((data) => {
        buildTable(data);
        // Object.entries(data).forEach(([key, value]) => {
        //         console.log(key, value);
    })
}
init()

