# CUATSHackathon2025
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/University_of_Cambridge_coat_of_arms.svg/1200px-University_of_Cambridge_coat_of_arms.svg.png" 
       alt="University of Cambridge" height="110">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/cambridge-ats/brand/main/logos/cuats-logo-black.png" 
       alt="Cambridge University Algorithmic Trading Society" height="110">
</p>

<h1 align="center">CUATS AlgoTrade Hackathon 2025</h1>

<p align="center">
Algorithmic trading strategy developed for the 
<strong>Cambridge University Algorithmic Trading Society (CUATS)</strong> Hackathon 2025.
<br>
Ranked <strong>Top 10 / 70+ teams</strong>.
</p>

---

## 🚀 Overview

This repository contains my Python implementation for CUATS AlgoTrade Hackathon 2025.  
The goal was to design a derivatives trading strategy operating on a **simulated order book** using **REST-like APIs** and **spot price signals**.

The challenge required:

- Building a **robust pricing model** under limited data  
- Managing and updating **live working orders**  
- Handling **latency, partial fills, and adversarial competition**  
- Structuring the strategy for **low-latency deployment on hardware** (e.g., Raspberry Pi)  

---

## 🧠 Problem Description

Participants were provided with:

- A derivatives **order book simulation** (bid/ask, L1/L2 depth)
- Streaming **spot price feeds**
- REST endpoints to:
  - Retrieve order book snapshots
  - Place / update / cancel orders
  - Track positions & PnL

The task:  
> Detect short-lived market inefficiencies and trade them profitably  
while controlling inventory, latency, and risk.

---

## 🛠️ Approach

### **1. Pricing & Signal Logic**
- Derived fair value from spot price movements and simple greeks intuition  
- Used conservative predictors to avoid overfitting in volatile scenarios

### **2. Execution Strategy**
- Maintained tight working quotes around fair value  
- Aggressively re-quoted when spot price shifted  
- Prevented inventory runaway via risk-adjusted spreads  

### **3. Latency Optimisation**
- Minimized redundant API calls  
- Ensured strategy remained state-light  
- Code prepared for deployment on **Raspberry Pi** (achieved ~10× latency reduction in final tests)

---

## 📂 Repository Structure

| File | Description |
|------|-------------|
| `dl659-CUATSHackathon2025-01.py` | Early baseline logic (pricing tests) |
| `dl659-CUATSHackathon2025-02.py` | Order management experiments |
| `dl659-CUATSHackathon2025-03.py` | Inventory-aware quoting |
| `dl659-CUATSHackathon2025-04.py` | Latency-reduced version |
| `dl659-CUATSHackathon2025-05.py` | **Final strategy submitted to CUATS** |

---

## ▶️ Getting Started

### **Requirements**
- Python 3.10+
- Standard libraries:
  - `requests`, `json`, `time`, `math`
- No special external dependencies required in most scripts

### **Running**
```bash
python dl659-CUATSHackathon2025-05.py
