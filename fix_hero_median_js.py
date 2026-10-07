import re

with open('code/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix hero-median-time
js = js.replace('document.getElementById("hero-median-time").textContent = apptMetrics.median_time_to_appointment_human || "< 2 hrs";', '// hero-median-time removed')

with open('code/frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
