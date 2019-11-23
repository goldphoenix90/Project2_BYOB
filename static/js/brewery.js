var url = "/sampleinfo";

function buildPlot() {
 d3.json(url).then((data) => {
   const longitude = data.longitude;
   const latitude = data.latitude;
   const zipcode = data.zip_code;
   const brewery_name = data.brewery_name;

   var geodata = [{
    type: 'scattergeo',
    locationmode: 'World',
    lat: latitude,
    lon: longitude,
    text: brewery_name,
    marker: {
        size: 18,
        line: {
            color: 'green',
            width: 1
        },
    }
}];

var geolayout = {
    title: 'Brewery Locations',
    showlegend: false,
    geo: {
        scope: 'world',
        projection: {
            type: 'natural earth'
        },
        showland: true,
        landcolor: 'rgb(217, 230, 242)',
        subunitwidth: 0.5,
        countrywidth: 1,
        subunitcolor: 'green',
        countrycolor: 'orange'
    },
};
Plotly.plot("mapid", geodata, geolayout, {showLink: false});

});
}
buildPlot();