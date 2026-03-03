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