let x, y, z;
let a = 0.2, b = 0.2, c = 5.7;
let dt = 0.01;

function setup() {
  createCanvas(800, 600);
  background(0);
  
  // Initialize the variables
  x = random(-20, 20);
  y = random(-20, 20);
  z = random(0, 40);
}

function draw() {
  // Adjust the Rössler system equations
  let dx = -y - z;
  let dy = x + a * y;
  let dz = b + z * (x - c);
  
  // Update the variables
  x += dx * dt;
  y += dy * dt;
  z += dz * dt;
  
  // Map the Rössler system variables to the canvas
  let px = map(x, -30, 30, 0, width);
  let py = map(y, -30, 30, height, 0);
  
  // Draw the point
  stroke(255, 100);
  strokeWeight(1);
  point(px, py);
}
