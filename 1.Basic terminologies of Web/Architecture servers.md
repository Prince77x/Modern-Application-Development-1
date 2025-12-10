# 🏗 Web Application Architecture

A **Web Application Architecture** defines **how the components of a web app (frontend, backend, database, server, APIs, etc.) interact** to deliver functionality to users.



# 🖥 Client-Server and Peer-to-Peer (P2P) Models

These are the two most common **network/application architectures**.

---

## 🖥 Client-Server Model

### 🔑 Concept
- In **Client-Server**, one central machine (**Server**) provides services/data.  
- Other machines (**Clients**) request and use those services.

### ⚙️ Working
1. Client sends a **request** (e.g., open Gmail).  
2. Server processes it (fetches email from database).  
3. Server sends a **response** back to client.

### ✅ Features
- **Centralized control** (server manages data).  
- Easy to manage & secure.  
- Scalable, but server may become a bottleneck.

### 📌 Examples
- Web Apps/browsing (Google, Facebook, Amazon)  
- Banking systems  
- Email services
- Databases  


00
---

## 🔗 Peer-to-Peer (P2P) Model

### 🔑 Concept
- In **P2P**, each computer (peer) acts as **both client and server**.  
- No central server → all peers share resources directly.

### ⚙️ Working
1. One peer requests a file.  
2. Another peer provides the file directly.  
3. Communication happens **peer-to-peer**.

### ✅ Features
- **Decentralized** (no single server).  
- Resource sharing (bandwidth, storage).  
- Harder to control and secure.

### 📌 Examples
- Torrent file sharing (BitTorrent)  
- Blockchain & Cryptocurrencies (Bitcoin, Ethereum)  
- Multiplayer games (LAN)
- IPFS ,Tahoe(distributed file systum)

## What is design pattern?

-  A Design Pattern is a **reusable** solution to a common software design problem.
It is **not code**, but a **template** or best practice for solving problems in software design.

- Think of it as a **proven recipe** that developers can follow instead of reinventing the wheel.

### look at the email example
 **Models** -> Store emails on server, index,ready to manupulate 

 **view** -> Display list of emails ,read individual emails

 **controllers** -> sort emails,delete ,archive in server


# 🏗 MVC (Model-View-Controller) Paradigm

**Definition:**  
**MVC (Model-View-Controller)** is a **software design pattern** that separates an application into **three interconnected components**:  

1. **Model** – Handles data and business logic.  
2. **View** – Handles the user interface and presentation.  
3. **Controller** – Handles user input and interaction between Model and View.  

This separation allows **modular, maintainable, and scalable applications**.   

---

## 🔑 Components of MVC

### 1️⃣ Model
- Represents the **data and business logic** of the application.  
- Responds to **requests from the Controller** to update or retrieve data.  
- Not concerned with how data is displayed.

**Example:**  
- In an e-commerce app, the **Product Model** manages product info, prices, inventory.  

---

### 2️⃣ View
- Represents the **UI / presentation layer**.  
- Displays data from the Model to the user.  
- Updates automatically when Model changes (in some frameworks).

**Example:**  
- Product page showing **images, price, and description**.  

---

### 3️⃣ Controller
- Acts as a **bridge between Model and View**.  
- Handles **user input**, manipulates data in the Model, and updates the View.

**Example:**  
- When a user adds a product to the cart, Controller updates the Model and refreshes the View.  

---

## 🔄 Flow of MVC

- User use **controller** -> to manupulate **Model** ->that update **views**-> that user sees
 
### Other design patterns

- Model-view-Adapter
- model-view-presenter
- model-view-viewmodel
- Hierarchical MVC
- .
- .


- Each has its use ,but fundamentals are very similar 