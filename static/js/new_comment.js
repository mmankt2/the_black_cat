
// Submit post on submit
$(function(){
    var frm = $('.new-comment-form');
    
    frm.submit(function(ev){
        ev.preventDefault();
        var blog_id = $(this).attr('blog_id').val();
        console.log(blog_id);
        alert(blog_id);
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function(data){
                //alert(data);
                $('.new_comment').val('');
                $('#comment-text-'+blog_id).prepend(data);
            }
        });
    });
});

// $(document).ready(function(){

//     $('input').click(function(){
//         alert(this.attr('blog_id').val());
//         var frm = $('#new-comment-form-'+this.blog_id.val());
        
//         frm.submit(function(ev){
//             ev.preventDefault();
//             var blog_id = $('#blog_id').val();
//             console.log(blog_id);
//             alert(blog_id);

//             //submit post on submit
//             $.ajax({
//                 type: frm.attr('method'),
//                 url: frm.attr('action'),
//                 data: frm.serialize(),
//                 success: function(data){
//                     //alert(data);
//                     $('#new_comment').val('');
//                     $('#comment-text-'+blog_id).prepend(data);
//                 }
//             });
//         });
//     });
// })