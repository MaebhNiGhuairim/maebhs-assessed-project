/**
 * @jest-environment jsdom
 */

describe('DOM Interaction Tests', () => {
    beforeEach(() => {
        document.body.innerHTML = `
            <form id="bookingForm">
                <input type="date" id="bookingDate">
                <input type="time" id="bookingTime">
                <input type="number" id="participants">
                <button type="submit">Submit</button>
            </form>
        `;
    });

    test('form submission with valid data', () => {
        const form = document.getElementById('bookingForm');
        const dateInput = document.getElementById('bookingDate');
        const timeInput = document.getElementById('bookingTime');
        const participantsInput = document.getElementById('participants');

        // Set valid values
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        dateInput.value = tomorrow.toISOString().split('T')[0];
        timeInput.value = '14:00';
        participantsInput.value = '2';

        // Mock form submission
        let formSubmitted = false;
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            formSubmitted = true;
        });

        form.submit();
        expect(formSubmitted).toBe(true);
    });
});
