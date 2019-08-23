$(document).ready(function () {

    $('#slider').on('input', function () {

        var value = $(this).val()
        $('#range_here').text('Value: ' + value)

        req = $.ajax({
            url: '/get_data',
            type: 'POST',
            data: {
                value: value
            }
        }); //ajax

        req.done(function (data) {

            $('#result_here').fadeOut(1000).fadeIn(1000);
            $('#range_here').fadeOut(1000).fadeIn(1000);
            $('#result_here').text('Result: ' + data)

        }); //show returned number

    }); //slider input

}); //doc.ready