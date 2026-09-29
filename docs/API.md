# API

Base URL: `http://127.0.0.1:8000`

- GET `/api/health`
- GET `/api/languages`
- GET `/api/roles?search=solar`
- GET `/api/opportunities?district=Coimbatore`
- POST `/api/profile`
- POST `/api/recommend`
- GET `/api/dashboard`

Example recommendation body:
```json
{
  "name": "Demo Beneficiary",
  "language": "Tamil",
  "education": "12th",
  "family_occupation": "Agriculture",
  "current_occupation": "Agriculture",
  "skills": ["vegetable cultivation", "basic electrical"],
  "interests": ["solar installation"],
  "mobility": "Local",
  "employment_preference": "Self Employment",
  "district": "Coimbatore"
}
```
