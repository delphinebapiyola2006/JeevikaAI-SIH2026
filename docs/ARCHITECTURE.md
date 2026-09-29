# Architecture

```text
Beneficiary
   |
Voice / Text
   |
ASR / Language Layer
Browser Web Speech API + optional BHASHINI
   |
Profile Extraction
   |
Education / Occupation / Skills / Interests / Mobility / Preference / Location
   |
Skill Gap + NSQF Role Matching
   |
Explainable Recommendation Engine
   |
Local Opportunity Signal
   |
Training / Job / Enterprise Pathway
   |
TTS / Voice Response
```

Prototype recommendation weights:
- 35% skill similarity
- 20% interest similarity
- 15% education compatibility
- 15% role/NSQF suitability
- 10% local opportunity signal
- 5% mobility compatibility

These are prototype design choices, not official SIH scoring criteria.
