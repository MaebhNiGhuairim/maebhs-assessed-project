// Updated booking.js
document.addEventListener("DOMContentLoaded", function () {
    const yogaClassSelect = document.getElementById('yoga_class');
    const scheduleSelect = document.getElementById('class_schedule');
    const dateSelect = document.getElementById('booking_date');
    const apiUrls = document.getElementById('api-urls').dataset;

    // Function to reset dependent fields
    function resetDependentFields(fromSchedule = false) {
        if (!fromSchedule) {
            scheduleSelect.innerHTML = '<option value="">Select a time</option>';
            scheduleSelect.disabled = true;
        }
        dateSelect.innerHTML = '<option value="">Select a date</option>';
        dateSelect.disabled = true;
    }

    if (yogaClassSelect && scheduleSelect && dateSelect) {
        yogaClassSelect.addEventListener('change', function () {
            const classId = this.value;
            resetDependentFields();

            if (classId) {
                // Replace the '0' in the URL with the actual class ID
                const schedulesUrl = apiUrls.schedulesUrl.replace('0', classId);
                
                fetch(schedulesUrl)
                    .then(response => response.json())
                    .then(data => {
                        scheduleSelect.innerHTML = '<option value="">Select a time</option>';
                        data.schedules.forEach(schedule => {
                            const option = document.createElement('option');
                            option.value = schedule.id;
                            option.textContent = `${schedule.day_of_week} at ${schedule.start_time}`;
                            scheduleSelect.appendChild(option);
                        });
                        scheduleSelect.disabled = false;
                    })
                    .catch(error => console.error('Error:', error));
            }
        });

        scheduleSelect.addEventListener('change', function() {
            const scheduleId = this.value;
            dateSelect.innerHTML = '<option value="">Select a date</option>';
            dateSelect.disabled = true;

            if (scheduleId) {
                fetch(`${apiUrls.datesUrl}?schedule_id=${scheduleId}`)
                    .then(response => response.json())
                    .then(data => {
                        data.dates.forEach(date => {
                            const dateObj = new Date(date);
                            const formattedDate = dateObj.toLocaleDateString('en-GB', {
                                weekday: 'long',
                                day: '2-digit',
                                month: 'long',
                                year: 'numeric'
                            });
                            const option = document.createElement('option');
                            option.value = date;  // Keep the YYYY-MM-DD format for the value
                            option.textContent = formattedDate;
                            dateSelect.appendChild(option);
                        });
                        dateSelect.disabled = false;
                    })
                    .catch(error => console.error('Error:', error));
            }
        });

        // If there are pre-selected values (e.g., after form validation error)
        if (yogaClassSelect.value) {
            yogaClassSelect.dispatchEvent(new Event('change'));
            // Wait for the schedules to load before triggering date population
            setTimeout(() => {
                if (scheduleSelect.value) {
                    scheduleSelect.dispatchEvent(new Event('change'));
                }
            }, 500);
        }
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

