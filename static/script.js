// populate states against selected country
$(document).ready(function () {
    $('#country').change(testMessage);

    function testMessage() {
        var url = $("#search-form").attr("states-url");
        var countryId = $(this).val();

        $.ajax({
            url: url,
            data: {
                'country': countryId
            },
            success: function (data) {
                $("#states").html(data);
            }
        });
    }
});

// Phone Checkbox true/false
$('#checkbox-value').text($('#phone').val());
$("#phone").on('change', function () {
    if ($(this).is(':checked')) {
        $(this).attr('value', 'true');
    } else {
        $(this).attr('value', 'false');
    }
    $('#checkbox-value').text($('#checkbox1').val());
});

// Email Checkbox true/false
$('#checkbox-value').text($('#email').val());
$("#email").on('change', function () {
    if ($(this).is(':checked')) {
        $(this).attr('value', 'true');
    } else {
        $(this).attr('value', 'false');
    }
    $('#checkbox-value').text($('#checkbox1').val());
});