function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const app = new Vue({
    el: '#app',
    data: {
        tickets: [],
        vehicles: [],
        vehiclePkSelected: 0,
        vehicleSelectedPayment: 0,
        modal: {},
        ticketSelected: undefined,
    },
    watch: {
        vehiclePkSelected: function (val, oldVal) {
            if (val != 0) {
                const vehicleFiltered = this.vehicles.find(v => v.pk == this.vehiclePkSelected);

                if (vehicleFiltered !== undefined) {
                    this.vehicleSelectedPayment = vehicleFiltered.vehicle_type.payment_per_night;
                }
            }
        }
    },
    methods: {
        register: function (event) {
            fetch("/ticket/register", {
                method: "POST",
                credentials: "same-origin",
                body: JSON.stringify({
                    vehicle_id: document.getElementById("vehicle").value,
                    amount: document.getElementById("amount").value,
                    paid: document.getElementById("paid").checked
                }),
                headers: new Headers({
                    'X-CSRFToken': getCookie("csrftoken"),
                    'Content-Type': 'application/json',
                    "Accept": "application/json",
                })
            })
                .then(res => res.json())
                .then(() => this.loadTickets())
                .then(() => this.closeModal());
        },
        loadTickets: function () {
            fetch("/tickets/today")
                .then(res => res.json())
                .then(data => this.tickets = data);
        },
        reloadVehicles: function () {
            fetch("/vehicle")
                .then(res => res.json())
                .then(data => this.vehicles = data)
                .then(() => {
                    M.FormSelect.init(document.querySelectorAll('select'))
                });
        },
        closeModal: function () {
            this.modal.close();
        },
        selectTicket: function(ticketPk, event) {
            let lastTicketSelected = this.ticketSelected;
            this.ticketSelected = this.tickets.find(t => t.pk == ticketPk);

            if (this.ticketSelected === lastTicketSelected) {
                this.ticketSelected = undefined;
            }
        }
    },
    mounted: function () {
        this.loadTickets();
        this.reloadVehicles();
        M.Modal.init(document.querySelectorAll(".modal"));
        this.modal = M.Modal.getInstance(document.getElementById('newModal'));
    }
});
