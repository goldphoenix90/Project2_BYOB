  function buildCharts() {
    d3.json(`/sampleinfo`).then((data) => {
      const otu_ids = data.beer_name;
      const otu_labels = data.category_labels;
      const values = data.category_totals;
      const abv = data.abv;
  
      // Build a Bubble Chart
      var bubbleLayout = {
        margin: { t: 0 },
        hovermode: "closest",
        xaxis: {
          title: "Categories",
          color: "white",
      },
        yaxis: {
          title: "Alcohol by Volume",
          color: "white"
        },
        paper_bgcolor: 'rgba(0,0,0,0)',
       plot_bgcolor: 'rgba(0,0,0,0)'
      };
      var bubbleData = [
        {
          x: otu_labels,
          y: abv,
          text: otu_ids,
          mode: "markers",
          marker: {
            size: abv,
            color: "gold",
            colorscale: "Earth"
          }
        }
      ];
  
      Plotly.plot("bubble", bubbleData, bubbleLayout);
  
      // Build a Pie Chart
      // HINT: You will need to use slice() to grab the top 10 sample_values,
      // otu_ids, and labels (10 each).
      var pieData = [
        {
          values: values,
          labels: otu_ids,
          hovertext: otu_labels,
          hoverinfo: "hovertext",
          
          type: "pie"
        }
      ];
  
      var pieLayout = {
        margin: { t: 0, l: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)'
      };
  
      Plotly.plot("pie", pieData, pieLayout);
    });
  }
  buildCharts();
  // function init() {
  //   // Grab a reference to the dropdown select element
  //   var selector = d3.select("#selDataset");
  
  //   // Use the list of sample names to populate the select options
  //   d3.json("/names").then((sampleNames) => {
  //     sampleNames.forEach((sample) => {
  //       selector
  //         .append("option")
  //         .text(sample)
  //         .property("value", sample);
  //     });
  
  //     // Use the first sample from the list to build the initial plots
  //     const firstSample = sampleNames[0];
  //     buildCharts(firstSample);
  //     // buildMetadata(firstSample);
  //   });
  // }
  
  // function optionChanged(newSample) {
  //   // Fetch new data each time a new sample is selected
  //   buildCharts(newSample);
  //   buildMetadata(newSample);
  // }
  
  // Initialize the dashboard
  
  