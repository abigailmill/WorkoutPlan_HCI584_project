# a placeholder for user workout logs
workout_logs = []

def log_workout(day, exercises_completed):
    workout_logs.append({'day': day, 'exercises': exercises_completed})

log_workout(1, ['Jumping Jacks', 'Knee Push-ups'])
log_workout(2, ['Squats', 'Knee Push-ups'])
print(workout_logs)
