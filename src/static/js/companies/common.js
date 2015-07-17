$(document).ready(function () {

    $(document).on('change', '.btn-file :file', function () {
        var label = $(this).val().replace(/\\/g, '/').replace(/.*\//, '');
        $(this).trigger('fileselect', [label]);
    });

    $('.btn-file :file').on('fileselect', function (event, label) {
        var input = $('#file_name');
        if (input.length) {
            input.val(label);
        }
    });
});