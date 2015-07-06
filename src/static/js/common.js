function csrf() {
    return $('input[name="csrfmiddlewaretoken"]').serialize();
}