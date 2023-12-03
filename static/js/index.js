function onlySpaces(str)
{
    return str.trim().length === 0;
}

$(document).ready(function(){
    document.getElementById("loading").setAttribute("hidden",false);

    $("form").on("submit",function(event){

        var msg = $("#input").val();

        if(onlySpaces(msg)==false){
            document.getElementById("changer").setAttribute("hidden",false);
            document.getElementById("loading").removeAttribute("hidden");
            document.getElementById("resultdiv").setAttribute("hidden",false);

            $.ajax({
                data:{
                    res:msg,
                },
                type:"POST",
                url:"/predict",
            }).done(function(data){
                var msg = data;

                document.getElementById("loading").setAttribute("hidden",false);
                document.getElementById("resultdiv").removeAttribute("hidden");
                document.getElementById("output").textContent = msg;
            })
        }
        else{
            document.getElementById("resultdiv").setAttribute("hidden",false);
            document.getElementById("changer").removeAttribute("hidden");
        }
        event.preventDefault();
    });

    $("#copyBtn").click(function(){
        navigator.clipboard.writeText($("#output").val());

        alert("Copied to Clipboard");
    });
});

