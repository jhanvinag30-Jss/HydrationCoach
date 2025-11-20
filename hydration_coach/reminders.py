def get_hourly_reminders(start_hour,end_hour):
  reminders=() #list
  for hour in range(start/-hour,end_hour+1):
    reminders.append(f"Remember:Drink water at {hour}:00")
    return reminders
