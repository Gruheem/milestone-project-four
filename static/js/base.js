document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.toast').forEach(function(toast) {
        new bootstrap.Toast(toast, {
            autohide: false
        }).show();
    });
});