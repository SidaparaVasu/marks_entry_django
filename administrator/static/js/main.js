// Fetching courses from selecting institute
$("#dropdown-institutes").change(function () {
    var url = $("#student_form").attr("data-course-url"); 
    var institute_id = $(this).val(); 
    $.ajax({                      
        url: url,                  
        data: {
            'institute_id': institute_id     
        },
        success: function(data) { 
            $("#dropdown-courses").html(data); 
            console.log("courses are fetched")
        },
        error: function(data){
            console.log("error")
        }
    });
});

// Fetching batch from selecting course
$("#dropdown-courses").change(function () {
    var url = $("#student_form").attr("data-batch-url"); 
    var course_id = $(this).val(); 
    $.ajax({                      
        url: url,                  
        data: {
            'course_id': course_id     
        },
        success: function(data) { 
            $("#dropdown-batches").html(data); 
            console.log("batches are fetched")
        },
        error: function(data){
            console.log(course_id)
        }
    });
});

// Fetching semester from selecting course (note: this is for student.html page)
$("#dropdown-courses").change(function () {
    var url = $("#student_form").attr("data-semester-url"); 
    var course_id = $(this).val(); 
    $.ajax({                      
        url: url,                  
        data: {
            'course_id': course_id     
        },
        success: function(data) { 
            $("#dropdown-semesters").html(data); 
            console.log("semesters are fetched")
        },
        error: function(data){
            console.log("error")
        }
    });
});

// Fetching semester from selecting course (note: this is for subject.html page)
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

// Fetching student from selecting semester (note: this is for marks_entry.html page)
$("#dropdown-semesters").change(function () {
    var url = $(".marks_entry_form").attr("data-student-url"); 
    var institute_id = $('#dropdown-institutes').val(); 
    var course_id = $('#dropdown-courses').val(); 
    var batch_id = $('#dropdown-batches').val(); 
    var semester_id = $('#dropdown-semesters').val(); 
    $.ajax({                      
        url: url,                  
        data: {
            'institute_id': institute_id,
            'course_id': course_id,
            'batch_id': batch_id,
            'semester_id': semester_id,     
        },
        success: function (data) { 
            $("#get-students").html(data); 
            console.log(institute_id, course_id, batch_id, semester_id)
        },
        error: function(data){
            console.log("error")
        }
    });
});