# HydrationCoach – Flowchart

            ┌──────────────────────┐
            │      Start Program    │
            └──────────┬───────────┘
                       │
                       ▼
        ┌────────────────────────────────┐
        │ Import modules & configuration │
        └────────────────────────────────┘
                       │
                       ▼
       ┌─────────────────────────────────┐
       │  Get user details (name,        │
       │  weight, reminder interval)     │
       └─────────────────────────────────┘
                       │
                       ▼
     ┌────────────────────────────────────┐
     │ Calculate daily water requirement  │
     │  water = weight * 35 ml            │
     └────────────────────────────────────┘
                       │
                       ▼
       ┌─────────────────────────────────┐
       │ Convert to liters and milliliters│
       └─────────────────────────────────┘
                       │
                       ▼
         ┌──────────────────────────────┐
         │  Display calculated output   │
         └──────────────────────────────┘
                       │
                       ▼
       ┌──────────────────────────────────┐
       │ Start reminder simulation        │
       │ (wait interval → print message)  │
       └──────────────────────────────────┘
                       │
                       ▼
             ┌───────────────────┐
             │      End Program  │
             └───────────────────┘