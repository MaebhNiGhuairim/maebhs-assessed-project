const { validateBookingForm } = require('../bookingValidation');

describe('Booking Form Validation', () => {
    // Test 1: Valid input
    test('should accept valid booking details', () => {
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        const result = validateBookingForm(
            tomorrow.toISOString().split('T')[0],
            '14:00',
            '2'
        );
        
        expect(result.isValid).toBe(true);
    });

    // Test 2: Missing date
    test('should reject empty date', () => {
        const result = validateBookingForm('', '14:00', '2');
        expect(result.isValid).toBe(false);
        expect(result.message).toBe('Date is required');
    });

    // Test 3: Past date
    test('should reject past date', () => {
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        
        const result = validateBookingForm(
            yesterday.toISOString().split('T')[0],
            '14:00',
            '2'
        );
        
        expect(result.isValid).toBe(false);
        expect(result.message).toBe('Date must be in the future');
    });

    // Test 4: Invalid participants number
    test('should reject invalid number of participants', () => {
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        const result = validateBookingForm(
            tomorrow.toISOString().split('T')[0],
            '14:00',
            '11'
        );
        
        expect(result.isValid).toBe(false);
        expect(result.message).toBe('Participants must be between 1 and 10');
    });
});
