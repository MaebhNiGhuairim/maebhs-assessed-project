// edit_booking.js
document.addEventListener("DOMContentLoaded", function () {
    const dateDropdown = document.getElementById('booking_date');

    // Get API URLs from hidden div ======== NEW CODE ========
    const apiUrls = document.getElementById('api-urls').dataset;
    // =======================================================

    const scheduleElement = document.getElementById('class-schedule-data')
    const scheduleId = scheduleElement.dataset.scheduleId;

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


});
