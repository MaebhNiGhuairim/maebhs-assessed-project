function validateBookingForm(date, time, participants) {
    // Check if date is not empty and is in the future
    if (!date) {
        return { isValid: false, message: 'Date is required' };
    }

    const selectedDate = new Date(date);
    const today = new Date();
    if (selectedDate < today) {
        return { isValid: false, message: 'Date must be in the future' };
    }

    // Check if time is provided
    if (!time) {
        return { isValid: false, message: 'Time is required' };
    }

    // Check if participants is a number between 1 and 10
    const participantsNum = parseInt(participants);
    if (isNaN(participantsNum) || participantsNum < 1 || participantsNum > 10) {
        return { isValid: false, message: 'Participants must be between 1 and 10' };
    }

    return { isValid: true, message: 'Validation successful' };
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { validateBookingForm };
}
