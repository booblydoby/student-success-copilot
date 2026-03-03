# Student Success Copilot

Hybrid AI system that generates a weekly study plan, predicts academic risk, and explains its decisions using Search, Rule-Based reasoning, and Machine Learning.

---

## Project Structure

```
student-success-copilot/
├── planner/
├── rules/
├── ml/
├── ui/
├── data/
├── tests/
├── models/
├── run_demo.py
├── requirements.txt
└── README.md
```

---

## Input Schema

### User Information

```json
{
  "user_id": 1,
  "gender": "male",
  "confidence": 4,
  "stress": 2,
  "attendance_rate": 0.9,
  "availability": [
    {
      "day": "Monday",
      "hours_available": 3
    }
  ]
}
```

### Tasks

```json
[
  {
    "task_id": "apple",
    "course": "AI",
    "deadline_days": 3,
    "estimated_hours": 5,
    "difficulty": 3
  }
]
```

---

## Output Schema

```json
{
  "weekly_plan": [
    {
      "day": "Monday",
      "task_id": "apple",
      "allocated_hours": 2
    }
  ],
  "risk_level": "Low",
  "risk_probability": 0.25,
  "explanation": "Task apple scheduled early due to close deadline.",
  "follow_up_question": "Would you like to increase study intensity this week?"
}
```

---

## Setup Instructions

1. Clone repository  
2. Create virtual environment  

   python -m venv venv  

3. Activate  

   venv\Scripts\activate  

4. Install dependencies  

   pip install -r requirements.txt  

---

## Run Demo

```
python run_demo.py data/demo_scenarios.json
```