# Redis Demo

# 1. Prerequisites

Make sure you have installed:

- Docker
- Docker Compose
- A modern browser

---

# 2. Start the environment

Clone the repository:

```bash
git clone git@github.com:Eliie58/Redis-Demo.git
cd Redis-Demo
```

Start all services:

```bash
docker compose up -d
```

This will start:

- [Flask application](http://localhost:5000)
- Redis server
- [Redis Insight](http://localhost:5540)
- [Jupyter Lab](http://localhost:8889/?token=token)

---

# 3. Redis Insight (Database Explorer)

Open:

http://localhost:5540

Use it to:

- Inspect keys
- Monitor data structures
- Debug your Redis operations
- Watch Pub/Sub activity in real-time

No login is required (default setup).

---

# 4. Jupyter Lab (Workshop Environment)

Open:

http://localhost:8889/?token=token

Steps:

1. Navigate to the `work/` folder
2. Open the provided notebook
3. Execute the cells step by step
4. Follow the instructions to understand Redis concepts

This notebook will help you:

- Test Redis commands
- Understand data structures
- Validate expected behavior

---

# 5. Your Main Task

Open the file:

[redis_api.py](app/app/redis_api.py)

## Goal

You must implement all functions marked with:

# TODO: implement

---

## What you will build

You will implement:

### 👤 Speakers

- Store and retrieve speaker profiles

### 📅 Sessions

- Time-based session scheduling (sorted by timestamp)

### ❓ Q&A System

- FIFO question queue per session

### 🏆 Leaderboard

- Real-time scoring system

### 🏷️ Tags

- Session tagging + reverse indexing

### 📢 Live Announcements

- Pub/Sub messaging + persistent history

---

## ⚠️ Rules

- Do NOT change function signatures
- Use Redis data structures correctly (no Python-side sorting/filtering)
- Prefer Redis operations over Python logic
- Each feature must be implemented using the appropriate Redis type

---

# 6. Test your progress

Once you implement functions, open:

http://localhost:5000

You will see:

- Speaker management UI
- Session scheduler
- Live Q&A system
- Leaderboard
- Real-time announcements

Everything is connected to your Redis implementation.

---

# 7. Stop and cleanup environment

To stop all services:

```bash
docker compose stop
```

To fully remove containers, volumes, and networks:

```bash
docker compose down -v --remove-orphans
```

---

# Optional full reset

If you want a clean restart:

```bash
docker compose down -v
docker system prune -f
```

---

# Learning outcomes

By the end of this workshop, you will understand:

- Redis data structures (Hash, List, Set, Sorted Set)
- Pub/Sub messaging systems
- Real-time backend architecture
- Event-driven web applications
- Flask + Redis integration patterns

---
