# Student Success Copilot

Hybrid AI system that generates a weekly study plan, predicts academic risk, and explains its decisions using Search, Rule-Based reasoning, and Machine Learning.

---

## Project Structure

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

---

## Input Schema

### User Information
{
  "user_id": int,
  "gender": "male/female",
  "confidence": 1-5,
  "stress": 1-5,
  "attendance_rate": 0.0-1.0,
  "availability": [
    {
      "day": "Monday",
      "hours_available": 3
    }
  ]
}

### Tasks
[
  {
    "task_id": "apple",
    "course": "AI",
    "deadline_days": 3,
    "estimated_hours": 5,
    "difficulty": 1-5
  }
]

---

## Output Schema

{
  "weekly_plan": [
    {
      "day": "Monday",
      "task_id": "apple",
      "allocated_hours": 2
    }
  ],
  "risk_level": "Low/Medium/High",
  "risk_probability": 0.0-1.0,
  "explanation": "Text explanation",
  "follow_up_question": "If needed"
}

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

python run_demo.py data/demo_scenarios.json