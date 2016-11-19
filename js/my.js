/*
* light : 0 pour éteindre; 1 pour allumer
*/
function changeLight(val) {
	var url = "light.php?val="+val;
	//alert(url);
    $.get(url, function(data) {
        $("#light").html(data);
    }).fail(function() {
        console.log( "error" );
    })
    .always(function() {
        //alert( "finished" );
    });

}
