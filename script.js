const div = document.getElementById("player-1");
const tooltip = document.getElementById("tooltip-1");


div.addEventListener("mouseover", function(event) {
    // Show the tooltip
    tooltip.style.display = "block";
  });

  div.addEventListener("mouseout", function() {
    // Hide the tooltip
    tooltip.style.display = "none";
  });