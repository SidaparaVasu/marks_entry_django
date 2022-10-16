$(document).ready(function(){
        
    $(".getSem").click(function(){
        let course_id = $(this).val();
        let csrf = $('input[name=csrfmiddlewaretoken]').val()
        console.log(course_id);

        myData = { course_id: course_id, csrfmiddlewaretoken: csrf },
        $.ajax({
            url: "{% url 'fetch_semesters' %}",
            type: 'POST',
            data: myData,
            dataType: "json",
            success: function(data){
                console.log(data.status)
                if (data.status == 'recvd'){
                    console.log(response.data)
                    console.log("data sended")
                }
                if (data.status == 0){
                    console.log("unable to send data")
                }
            },
            error: function(data){
                console.log(data.status)
                // alert("fail");
            }
        });
    });
});