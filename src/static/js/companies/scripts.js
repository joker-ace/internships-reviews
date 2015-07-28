function clearErrorMessageFor(input) {
    input.closest('.form-group').removeClass('has-error');
    input.parent().find('span.error-message').remove();
}

$(document).ready(function () {
    comapnyAutocompleteUrl = '/api/autocomplete-company-name';
    cityAutocompleteUrl = '/api/autocomplete-city-name';
    // ///////////////////////////////////////////////////////////////////
    $("#company").select2({
        placeholder: "Start typing a company name",
        theme: "bootstrap",
        tags: true,
        allowClear: true,
        minimumInputLength: 1,
        ajax: {
            //How long the user has to pause their typing before sending the next request
            delay: 250,
            closeOnSelect: true,
            url: comapnyAutocompleteUrl,
            dataType: 'json',
            processResults: function (data) {
                var results = [];
                if (data && data.count) {
                    data.items.forEach(function (company) {
                        results.push({
                            id: company.name,
                            text: company.name
                        })
                    });
                }
                return {
                    results: results
                };
            }
        }
    }).on("change", function () {
        clearErrorMessageFor($(this));
    });
    // ///////////////////////////////////////////////////////////////////

    $("#province").select2({
        placeholder: "Select a province",
        theme: "bootstrap",
        allowClear: true
    }).on("change", function () {
        clearErrorMessageFor($(this));
        $("#city").select2("val", null);
    });

    // ///////////////////////////////////////////////////////////////////
    $("#city").select2({
        placeholder: "Start typing a city name",
        theme: "bootstrap",
        tags: true,
        allowClear: true,
        minimumInputLength: 1,
        ajax: {
            //How long the user has to pause their typing before sending the next request
            delay: 250,
            closeOnSelect: true,
            url: cityAutocompleteUrl,
            dataType: 'json',
            data: function (params) {
                var province = $("#province").select2("val");
                return {
                    q: params.term,
                    province: province
                }
            },
            processResults: function (data) {
                var results = [];
                if (data && data.count) {
                    data.items.forEach(function (city) {
                        results.push({
                            id: city.name,
                            text: city.name
                        });
                    });
                }
                return {
                    results: results
                }
            }
        }
    }).on("change", function () {
        clearErrorMessageFor($(this));
    });

    $("#recommendation-rating").raty({
        cancel: true,
        number: 10,
        scoreName: 'recommendation',
        score: function () {
            return $(this).attr('data-score');
        }
    });

    $("#apply-learnt-things-rating").raty({
        cancel: true,
        number: 10,
        scoreName: 'apply_skills',
        score: function () {
            return $(this).attr('data-score');
        }
    });

    $("#learn-new-rating").raty({
        cancel: true,
        number: 10,
        scoreName: 'learn_new',
        score: function () {
            return $(this).attr('data-score');
        }
    });

});