```markdown
# my-website

A small static website served by nginx, packaged as a Docker image and published to GitHub Container Registry.

Features
- Responsive static site (HTML/CSS/JS)
- Light/dark theme toggle persisted in localStorage
- Small service worker for offline-first caching
- Dockerfile using nginx:stable-alpine
- GitHub Actions workflow that builds + pushes image to ghcr.io

Local usage
1. Build:
   docker build -t my-website:latest .

2. Run:
   docker run --rm -p 8080:80 my-website:latest
   Open http://localhost:8080

3. Using docker-compose:
   docker compose up --build
   Open http://localhost:8080

Permissions for CI (if pushing image to ghcr)
- The workflow uses the repository's GITHUB_TOKEN to push to ghcr.io. In the repository settings enable Actions workflow permissions:
  Settings → Actions → General → Workflow permissions → set to "Read and write permissions" and enable "Allow GitHub Actions to create and approve pull requests" if relevant.
- The workflow sets packages: write permission; if you prefer Docker Hub, see the alternative instructions in the "CI" section below.

Repository creation
Option A (recommended, if you want to run locally):
- Create the repo on GitHub (private), then run the Git commands in the project folder shown below.

Option B (I can create and push for you)
- I can create the private repository and push these files if you prefer to grant me permission to do so.

CI / Publishing
- The included workflow builds and pushes images to ghcr.io as:
  ghcr.io/<your-org-or-username>/my-website:latest
- Make sure workflow permissions allow packages write (described above).

If you want me to create and push the repo for you, tell me and I’ll proceed once you grant me permission.
```