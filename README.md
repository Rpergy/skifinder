# skifinder
  While planning routes for my family while skiing in Vail, I thought it would be cool to create an application that can automatically do this. My end goal was to be able to select a starting and ending point, and the program would tell you the shortest path between the two. <br><br>
  This project uses graph traversal and Dijkstra's Algorithm (https://brilliant.org/wiki/dijkstras-short-path-finder/) in order to find the shorest path. Every ski map is represented as a graph of verticies, all connected by edges. I have written a tool with Pygame that helps me easily create maps for different ski resorts. 
  <br><br>
  Eventually, I'd like to turn this project into a full-fledged app that someone could use for themselves while skiing.
<br><br>
# futute features
  I have decided to put this project on hold for now to start working on my long list of other projects, but I have ideas for a variety of different features that could possibly be implemented in the future. <br>Here are some of them:
  - Generate paths bised around different parameters (avoid all lifts, avoid certain trail difficulties)
  - Access an API that will remove certain lifts and trails from the map depending on if they are open or closed for the day
  - Change the weights of each edge to reflect the average speed travelled on a trail, instead of the total distance
  - Add multiple stops on a path, requiring certain nodes to be traversed through
<br>

# development screenshots
<img src="Testing Resources/samplemap_graph.png">
<p style="text-align:center">Basic graph used for testing Dijkstra's Algorithm</p>

<img src="Testing Resources/plotTestMap.png">
<p style="text-align:center">The first map created with the map editor</p>

<img src="Testing Resources/finalApp.png">
<p style="text-align:center">Final application</p>
