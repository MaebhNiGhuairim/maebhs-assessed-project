// Updated booking.js
document.addEventListener("DOMContentLoaded", function () {
    const yogaClassDropdown = document.getElementById('yoga_class');
    const scheduleDropdown = document.getElementById('class_schedule');
    const dateDropdown = document.getElementById('booking_date');

    // Get API URLs from hidden div ======== NEW CODE ========
    const apiUrls = document.getElementById('api-urls').dataset;
    // =======================================================

    if (yogaClassDropdown && scheduleDropdown && dateDropdown) {
        yogaClassDropdown.addEventListener('change', function () {
            const classId = this.value;
            if (classId) {
                // Modified fetch URL ======== UPDATED CODE ========
                const schedulesUrl = apiUrls.schedulesUrl.replace('0', classId);
                fetch(schedulesUrl)
                // =================================================
                    .then(response => {
                        if (!response.ok) throw new Error('Network response was not ok');
                        return response.json();
                    })
                    .then(data => {
                        scheduleDropdown.innerHTML = '<option value="">Select a day and time</option>';
                        data.schedules.forEach(schedule => {
                            const option = document.createElement('option');
                            option.value = schedule.id;
                            option.textContent = `${schedule.day_of_week} at ${schedule.start_time}`;
                            scheduleDropdown.appendChild(option);
                        });
                        scheduleDropdown.disabled = false;
                    })
                    .catch(error => console.error('Error fetching schedules:', error));
            } else {
                scheduleDropdown.innerHTML = '<option value="">Select a day and time</option>';
                scheduleDropdown.disabled = true;
            }
        });

        scheduleDropdown.addEventListener('change', function () {
            const scheduleId = this.value;
            if (scheduleId) {
                // ========== UPDATED FETCH CALL ==========
                fetch(`${apiUrls.datesUrl}?schedule_id=${scheduleId}`)
                    .then(response => {
                        if (!response.ok) throw new Error('Failed to fetch dates');
                        return response.json();
                    })
                    .then(data => {
                        dateDropdown.innerHTML = '<option value="">Select a date</option>';
                        data.dates.forEach(date => {
                            const option = document.createElement('option');
                            option.value = date;
                            option.textContent = date;
                            dateDropdown.appendChild(option);
                        });
                        dateDropdown.disabled = false;
                    })
                    .catch(error => {
                        console.error('Error fetching available dates:', error);
                        dateDropdown.innerHTML = '<option value="">Error loading dates</option>';
                    });
            } else {
                dateDropdown.innerHTML = '<option value="">Select a date</option>';
                dateDropdown.disabled = true;
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const classeshero = document.querySelector('.classes-hero');
    console.log(classeshero)
    if (classeshero) {
        const cards = document.querySelectorAll('.card');

        cards.forEach(card => {
            card.addEventListener('click', function() {
                const paragraph = this.querySelector('.card-paragraph');
                if (paragraph.style.display === 'block') {
                    paragraph.style.display = 'none';
                } else {
                    paragraph.style.display = 'block';
                }
            });
        });
    }
});