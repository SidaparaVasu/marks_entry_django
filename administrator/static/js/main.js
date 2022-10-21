// Fetching semesters from selecting course
$("#fetch_semesters").change(function () {
    var url = $("#courses_form").attr("data-semester-url"); 
    var course_id = $(this).val(); 
    $.ajax({                      
        url: url,                  
        data: {
            'course_id': course_id     
        },
        success: function (data) { 
            $("#dropdown-semesters").html(data); 
            console.log("semesters are fetched")
        },
        error: function(data){
            console.log("error")
        }
    });
});