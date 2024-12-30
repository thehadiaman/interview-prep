# Appointment Booking Widget

## Overview
The Appointment Booking Widget is a JavaScript-based widget that allows users to book an appointment through a form interface embedded on a web page. It lets users input their name, phone number, preferred date, and time slot for the appointment. The widget interacts with an API to fetch available slots for the selected date and submit the booking request.

## Features
- **Name and Phone Input**: Users can enter their name and phone number.
- **Date Selection**: Users can choose an appointment date from a date picker.
- **Time Slot Selection**: Available time slots are dynamically populated based on the selected date.
- **Form Submission**: After selecting a slot, users can submit the form to book an appointment.
- **Error and Success Messages**: Displays a success or error message based on the booking response.

## How to Use

### 1. Include the Required Files

Make sure to include the necessary HTML, CSS, and JavaScript files in your project:

#### HTML

Add the following HTML code to your webpage where you want to display the booking widget.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Booking</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div id="appointment-booking-widget"></div>

    <script src="./appointment-booking.js"></script>
    <script>
        // Initialize the appointment booking widget with the API base URL
        initBookingWidget({ apiBaseUrl: 'http://localhost:5000/api' });
    </script>
</body>
</html>
