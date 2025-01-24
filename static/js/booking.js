    const yogaClassDropdown = document.getElementById('yoga_class');
    const scheduleDropdown = document.getElementById('class_schedule');
    const dateDropdown = document.getElementById('booking_date');

    yogaClassDropdown.addEventListener('change', function () {
        const classId = this.value;
        if (classId) {
            // Fetch class schedules
            fetch(`/api/schedules/${classId}/`)
                .then(response => response.json())
                .then(data => {
                    scheduleDropdown.innerHTML = '<option value="">Select a day and time</option>';
                    data.schedules.forEach(schedule => {
                        const option = document.createElement('option');
                        option.value = schedule.id;
                        option.textContent = `${schedule.day_of_week} at ${schedule.start_time}`;
                        scheduleDropdown.appendChild(option);
                    });
                    scheduleDropdown.disabled = false;
                });
        } else {
            scheduleDropdown.innerHTML = '<option value="">Select a day and time</option>';
            scheduleDropdown.disabled = true;
        }
        dateDropdown.innerHTML = '<option value="">Select a date</option>';
        dateDropdown.disabled = true;
    });

    scheduleDropdown.addEventListener('change', function () {
        fetch('/api/valid-dates/')
            .then(response => response.json())
            .then(data => {
                dateDropdown.innerHTML = '<option value="">Select a date</option>';
                data.dates.forEach(date => {
                    const option = document.createElement('option');
                    option.value = date;
                    option.textContent = date;
                    dateDropdown.appendChild(option);
                });
                dateDropdown.disabled = false;
            });
    });

