# 🗺️ Route Finder — Graph + BFS + DFS

A Python-based DSA project that finds routes between cities using **Graph Traversal, Breadth-First Search (BFS), and Depth-First Search (DFS)**.

The project demonstrates how fundamental data structures such as **Queue and Stack** can be used to solve real-world route-finding problems.

---

## 📌 Project Overview

Route Finder represents cities as vertices/nodes and connections between cities as edges in an **undirected graph**.

Users can:

* View the city map
* Find routes using BFS
* Find routes using DFS
* Compare BFS and DFS
* Add new cities
* Add connections between cities

---

## 🚀 Features

### 1. Display City Map

Displays all cities and their connected neighbouring cities.

### 2. BFS Route Finder

Uses **Breadth-First Search** with a Queue to explore the graph level by level.

BFS is useful for finding the shortest path in an unweighted graph.

### 3. DFS Route Finder

Uses **Depth-First Search** with a Stack to explore the graph deeply before backtracking.

### 4. BFS vs DFS Comparison

The project allows users to compare:

* Traversal order
* Route found
* Number of cities visited
* Route length

### 5. Add New City

Users can add new cities dynamically.

### 6. Add City Connection

Users can create connections between existing cities.

### 7. Input Validation

The program handles invalid city names and invalid menu choices.

---

## 🧠 DSA Concepts Used

| Concept | Usage                             |
| ------- | --------------------------------- |
| Graph   | Represents cities and connections |
| Queue   | Used by BFS                       |
| Stack   | Used by DFS                       |
| BFS     | Level-by-level graph traversal    |
| DFS     | Depth-first graph traversal       |
| Set     | Tracks visited cities             |
| List    | Stores routes and neighbours      |

---

## 🔵 Breadth-First Search (BFS)

BFS explores neighbouring nodes level by level.

### Data Structure

**Queue — FIFO (First In, First Out)**

### Time Complexity

```text
O(V + E)
```

Where:

* `V` = number of vertices/cities
* `E` = number of edges/connections

---

## 🟢 Depth-First Search (DFS)

DFS explores one path deeply before backtracking.

### Data Structure

**Stack — LIFO (Last In, First Out)**

### Time Complexity

```text
O(V + E)
```

Where:

* `V` = number of vertices/cities
* `E` = number of edges/connections

---

## 🏗️ Project Structure

```text
Route-Finder-DSA/
│
├── route_finder.py
└── README.md
```

---

## 💻 Technologies Used

* Python
* Data Structures & Algorithms
* Graph
* BFS
* DFS
* Queue
* Stack

---

## ▶️ How to Run

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd Route-Finder-DSA
```

### Step 3: Run the program

```bash
python route_finder.py
```

---

## 📋 Main Menu

```text
=================================================================
                  🗺️ ROUTE FINDER
                 GRAPH + BFS + DFS
=================================================================
1. Display City Map
2. Find Route using BFS
3. Find Route using DFS
4. Compare BFS and DFS
5. Add New City
6. Add City Connection
7. Exit
=================================================================
```

---

## 🎯 Sample Route

Example:

```text
Starting city: Bangalore
Destination city: Mysore
```

Possible route:

```text
Bangalore → Ramanagara → Channapatna → Mandya → Mysore
```

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Representing real-world problems using graphs
* Implementing BFS using a queue
* Implementing DFS using a stack
* Tracking visited nodes
* Finding paths between nodes
* Comparing graph traversal algorithms
* Building an interactive Python CLI application

---

## 🔮 Future Improvements

Possible future versions could include:

* Weighted graphs
* Dijkstra's shortest path algorithm
* Distance and travel-time calculation
* Graph visualization
* More cities and connections
* Map-based interface
* Interactive route visualization

---

## 👩‍💻 Author

**Sania**

Built as a Data Structures and Algorithms project using Python.
