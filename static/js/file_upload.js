g$(".custom-file-input").on("change", function () {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

var form = document.getElementById("form")
form.addEventListener("submit", function (e) {
    if (!form.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
    }
    form.classList.add("was-validated");
}, false)