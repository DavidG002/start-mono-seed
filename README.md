# Start Mono Seed
A barebones Nx monorepo with Next.js, Django, Pants, and Docker Compose—ready for local dev on HTTP/HTTPS.

## Features
- **Frontend**: Next.js (`https://localhost/`).
- **Backend**: Django with admin (`https://localhost/admin/`).
- **Build**: Nx and Pants—monorepo tooling.
- **Deploy**: Docker Compose—HTTP (`80`) and HTTPS (`443`) with self-signed certs.
- **Superuser**: Auto-created (`admin`/`password`)—customizable.

## Prerequisites
- Node.js (18+)
- Python (3.10+)
- pnpm
- Docker + Docker Compose
- **Note**: On Windows, use WSL (Windows Subsystem for Linux) for consistency with Pants and Nx. Linux and macOS work natively.

## Setup
1. Clone: `git clone https://github.com/DavidG002/start-mono-seed.git`  
   Then: `cd start-mono-seed`  
2. Install: `pnpm install`  
3. Certs (Optional): Copy self-signed certs to `infra/certs/` (e.g., `fullchain.pem`, `privkey.pem`).  
   Or generate: `cd infra && openssl req -x509 -newkey rsa:4096 -keyout certs/privkey.pem -out certs/fullchain.pem -days 365 -nodes -subj "/CN=localhost"`  
4. Build and Run: `pnpm nx docker-compose-up-build infra`  
5. Access: Frontend at `http://localhost/` or `https://localhost/` (accept cert warning), Admin at `https://localhost/admin/` (default: `admin`/`password`)

## Customize
- **Superuser**: Edit `apps/backend/django/create_superuser.py`—e.g., `'myadmin', 'myemail@example.com', 'mypassword'`.
- **Certs**: Replace `infra/certs/` with production certs (e.g., Let’s Encrypt).
- **Deploy**: Extend with CI/CD—see GitHub Actions for ideas.

## Notes
- Uses SQLite—persisted via volumes (`django-db`).
- HTTPS—self-signed for dev—swap for real certs in prod.

## Commands
- **Pants**:  
  - `pants tailor`—Setup initial Pants config (optional, used early).  
  - `pants package`—Build packages (superseded by Docker).  
- **Nx (Local)**:  
  - `pnpm nx serve next`—Run Next.js locally (non-Docker).  
  - `pnpm nx serve django`—Run Django locally (non-Docker).  
- **Nx Docker**:  
  - `pnpm nx docker-build next`—Build Next.js Docker image.  
  - `pnpm nx docker-build django`—Build Django Docker image.  
  - `pnpm nx docker-down next`—Stop Next.js container.  
  - `pnpm nx docker-down django`—Stop Django container.  
  - `pnpm nx docker-compose-up-build infra`—Build and start Compose stack.  
  - `pnpm nx docker-compose-down infra`—Stop Compose stack.

## Customize
- **Superuser**: Edit `apps/backend/django/create_superuser.py`—e.g., `'myadmin', 'myemail@example.com', 'mypassword'`.
- **Certs**: Replace `infra/certs/` with production certs (e.g., Let’s Encrypt).
- **Deploy**: Extend with CI/CD—see GitHub Actions for ideas.

## Notes
- Uses SQLite—persisted via volumes (`django-db`).
- HTTPS—self-signed for dev—swap for real certs in prod.