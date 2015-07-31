var s2faculties = null;

function onFacultiesDataReceived(data) {
    if (data && data.count) {
        var faculties = [];
        data.items.forEach(function (faculty) {
            faculties.push({
                id: faculty.id,
                text: faculty.name
            });
        });

        if (s2faculties) {
            s2faculties.select2("destroy").find('option').remove();
            s2faculties.append($('<option>'));
        }
        $("#row-faculty").show('slow', function () {
            s2faculties = $("#faculty").select2({
                placeholder: "Select your faculty",
                theme: "bootstrap",
                tags: true,
                data: faculties
            });
            s2faculties.on('change', function() {
                $("#btn-save-university").removeAttr("disabled");
            })
        });
    }
}
$(document).ready(function () {

    var s2universities = $("#university").select2({
        placeholder: "Select your university",
        theme: "bootstrap"
    });

    s2universities.on("change", function () {
        // on select, find all faculties of the selected university
        var url = $("#university_faculties_url").val();
        var data = s2universities.serialize() + '&' + csrf();
        $.post(url, data, onFacultiesDataReceived, "json");
    });
});