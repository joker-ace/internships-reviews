$(document).ready(function () {

    // ///////////////////////////////////////////////////////////////////
    $("#company").select2({
        placeholder: "Select your company or type a new one",
        theme: "bootstrap",
        tags: true
    }).on("change", function () {
        $(this).closest('.form-group').removeClass('has-error');
        $(this).parent().find('span.error-message').remove();
    });
    // ///////////////////////////////////////////////////////////////////

    $("#province").select2({
        placeholder: "Select province",
        theme: "bootstrap"
    }).on("change", function () {
        $(this).closest('.form-group').removeClass('has-error');
        $(this).parent().find('span.error-message').remove();
    });

    // ///////////////////////////////////////////////////////////////////
    $("#city").select2({
        placeholder: "Select city",
        theme: "bootstrap",
        tags: true
    }).on("change", function () {
        $(this).closest('.form-group').removeClass('has-error');
        $(this).parent().find('span.error-message').remove();
    });
});