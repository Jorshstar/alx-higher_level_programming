$(document).ready(function(){
    function translateHello() {
        let languageCode = $('#language_code').val();
        let apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
        $.get(apiUrl, function(data) {
            $('#hello').text(data.hello);
        });
    }
    $('#btn_translate').click(translateHello);
    $('#language_code').keypress(function(e) {
        if (e.which === 13) {
            translateHello();
        }
    });
});
