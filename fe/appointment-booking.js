function initBookingWidget({ apiBaseUrl }) {
    const widget = document.getElementById('appointment-booking-widget');
    widget.innerHTML = `
        <div class="card">
            <div class="card-body">
                <h3 class="card-title">Book an Appointment</h3>
                <form id="booking-form">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input type="text" class="form-control" id="name" placeholder="Enter your name" required>
                    </div>
                    <div class="mb-3">
                        <label for="phone" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="phone" placeholder="Enter your phone number" required>
                    </div>
                    <div class="mb-3">
                        <label for="date" class="form-label">Date</label>
                        <input type="date" class="form-control" id="date" required>
                    </div>
                    <div class="mb-3">
                        <label for="slot" class="form-label">Slot</label>
                        <select class="form-select" id="slot" required>
                            <option value="">Select Slot</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary">Book</button>
                </form>
                <div id="message" class="mt-3"></div>
            </div>
        </div>
    `;

    async function fetchAvailableSlots(date) {
        const response = await fetch(`${apiBaseUrl}/available-slots?date=${date}`);
        const { slots } = await response.json();
        const timeSlotSelect = document.getElementById('slot');
        timeSlotSelect.innerHTML = '<option value="">Select Slot</option>';
        slots.forEach(slot => {
            const option = document.createElement('option');
            option.value = slot;
            option.textContent = slot;
            timeSlotSelect.appendChild(option);
        });
    }

    document.getElementById('date').addEventListener('change', async (e) => {
        const date = e.target.value;
        fetchAvailableSlots(date);
    });

    document.getElementById('booking-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const date = document.getElementById('date').value;
        const slot = document.getElementById('slot').value;

        const response = await fetch(`${apiBaseUrl}/book`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, phone, date, slot })
        });

        const result = await response.json();
        const messageDiv = document.getElementById('message');
        if (response.ok) {
            messageDiv.innerHTML = `
                <div class="alert alert-success" role="alert">
                    ${result.message}
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    ${result.error || 'An error occurred'}
                </div>
            `;
        }

        if (response.ok) {
            fetchAvailableSlots(date);
        }
    });
}
