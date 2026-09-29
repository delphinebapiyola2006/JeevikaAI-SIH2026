# JeevikaAI — SIH 2026 MVP v2

**AI-Driven Voice Assistant for Livelihood Mapping and NSQF-Aligned Skilling Recommendations**

This version is a richer, judge-facing MVP with a light professional visual system inspired by the supplied reference image (white workspace, muted indigo hero, rose accent).

## What changed in v2

- Redesigned Overview / landing page with a clear AI livelihood command flow instead of a static landing screen.
- English + Tamil voice assessment.
- Guided 7-question conversational assessment that converts answers into structured profile fields.
- Voice micro-challenge for a basic work-style signal; the feature is intentionally beyond simple speech-to-text.
- Career Passport / My Profile with editable fields, readiness score, skill matrix and live save.
- Saving the profile automatically recalculates recommendations using the latest profile.
- Recommendation cards now show only personalized pathway information; no beneficiary-facing DEMO label.
- Opportunity Map now has district filters, mapped place cards, demand signals and multiple pilot districts.
- Admin Analytics includes program funnel, sector distribution, current recommendation activity, export snapshot and governance checks.
- Added JSON export from Admin Analytics.
- Seed path fixed so `datasets/` resolves correctly inside the extracted project.

## Run

### Backend

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload --port 8000
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Backend docs: `http://127.0.0.1:8000/docs`

### Frontend

Open a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the Vite URL, normally `http://localhost:5173`.

## Voice assessment

- Choose **Tamil** or **English**.
- Allow microphone permission in Chrome.
- Use **Speak answer** for each guided question.
- The transcript is converted into structured fields such as education, skills, interests, mobility and employment preference.
- The micro-challenge adds a simple work-style signal.
- Browser speech recognition is an MVP boundary. For production, connect an approved ASR/language service such as BHASHINI through the backend service boundary.

## Important data note

`datasets/opportunities.csv` contains **synthetic prototype livelihood signals** for demonstrating the map. The UI does not call them live vacancies. Before a real deployment or final evidence claim, replace them with verified government/partner data and verify current NSQF/QP/NOS references.
