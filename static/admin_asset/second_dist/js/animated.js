;(function($){


    function init(e){

        var el = $(e)
        var original_str = el.data('placeholder')
        var index = 0
        var area = $('textarea')
        var current_str = ''

        if(original_str){
            var interv = setInterval(function(){
                el.val(current_str)
                current_str += original_str.substr(index, 1)
                index++
                if(index > original_str.length){
                    clearInterval(interv)
                    el.addClass('done')
                }
            }, 66)
        }


        el.focusin(function(){
            if(!$(this).hasClass('first')){
                el.val('')
                el.addClass('first')
                el.removeClass('done')
                el.attr('placeholder', original_str)
            }
        })

    }

    $.fn.introducing = function(options) {

	    var defaults = {};
        var settings = $.extend( {}, defaults, options );

        return this.each(function(i, e){
            init(e)
        });
    };

})(jQuery)