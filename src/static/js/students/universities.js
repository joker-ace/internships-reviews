var s2faculties = false;
$(document).ready(function () {

    var s2universities = $("#university").select2({
        placeholder: "Select your university",
        theme: "bootstrap"
    });

    s2universities.on("change", function () {
        // on select, find all faculties of the selected university
        var url = $("#university_faculties_url").val();
        var data = s2universities.serialize() + '&' + csrf();
        $.post(
            url,
            data,
            function (data) {
                if (data.result) {
                    var faculties = [];
                    data.result.forEach(function (faculty) {
                        faculties.push({
                            id: faculty.id,
                            text: faculty.name
                        });
                    });
                    if (s2faculties) {
                        $("#faculty").select2("destroy");
                        s2faculties = false;
                    }

                    $("#faculty").select2({
                        placeholder: "Select your faculty",
                        theme: "bootstrap",
                        tags: true,
                        data: faculties
                    });
                    s2faculties = true;
                }
            },
            "json"
        );
    });
});