# 🚀 BMSCE LMS Auto-Solver — Complete Setup & Execution Guide

Welcome! This automated tool solves and submits competitive coding problems on BMSCE LMS (`https://lms.bmsce.in`).

All verified solutions up to Week 6 are pre-cached in `solutions.json`. **No AI / Groq API key is required** to run already-solved problems!

---

## 📋 Prerequisites

Before running the tool, make sure you have installed:
1. **[Git](https://git-scm.com/downloads)**
2. **[Node.js (LTS version 18+)](https://nodejs.org/)**

---

## ⚡ Quick Start (3 Steps)

### Step 1: Clone the Repository
Open your terminal (PowerShell, Command Prompt, or Terminal) and run:
```bash
git clone https://github.com/lalitsureliya-2005/LMS-solver.git
cd LMS-solver
```

---

### Step 2: Install Dependencies
Run the following commands to install packages and download the browser binary:
```bash
npm install
npx playwright install chromium
```

---

### Step 3: Run the Solver

#### Option A: Interactive Menu (Recommended)
```bash
npm run solve-all
```
*(On Windows, you can also simply double-click the `run.bat` file).*

You will be prompted to choose your login method:
- **`1` — Email + Password:** Enter your BMSCE email and LMS password directly in the terminal (passwords are masked with `*` and never saved).
- **`2` — Sign in with Google:** A browser window opens on the LMS login page. Click **"Sign in with Google"** and complete your login yourself. The browser then closes automatically and starts solving.

---

## 🎯 Specific Commands

| Task | Command | Description |
|------|---------|-------------|
| **Interactive Menu** | `npm run solve-all` | Recommended for first-time users (interactive prompts) |
| **Solve Week 6 Only** | `npm run solve:week6` | Submits only Week 6 problems (skips earlier weeks) |
| **Solve All Problems** | `npm run solve:all` | Submits all problems, automatically skipping already-accepted ones |
| **Google Sign-in Direct** | `npm run solve:google` | One command that opens browser for Google login, then solves |
| **Solve Single Problem** | `node solve.js <number>` | Solves a specific problem by 1-based number (e.g. `node solve.js 85`) |
| **Watch Visually (Debug)**| `npm run solve:debug` | Opens a visible browser window so you can watch code being entered |

---

## 💡 Important Notes

- **Already Solved Problems:** The script automatically detects and skips problems you have already got `Accepted` on.
- **No Password Stored:** Your password is never saved to disk or `.env`.
- **For New Problems:** Pre-cached solutions are included for Weeks 1–6. A `.env` file with `GROQ_API_KEY` is only needed if new future problems are added that don't have solutions yet.
