(function () {
    var jquery_version = '3.4.1';
    var site_url = 'https://127.0.0.1:8000/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {
        // load CSS, 用一个随机数参数防止浏览器返回一个缓存文件
        var css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
        });
        jQuery('head').append(css);

        // custom HTML, 包含当前网页中找到的图片 
        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
        // 添加 HTML 到 当前网站的 <body> 中
        jQuery('body').append(box_html);

        // close event: 通过 jQuery selectors，当用户点击 close link 时删除上面的 HTML
        jQuery('#bookmarklet #close').click(function(){
            jQuery('#bookmarklet').remove();
        });

        // find images and display them
        jQuery.each(jQuery('img[src$="jpg"]'),function(index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height)
            {
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('<a href="#"><img src="'+image_url +'" /></a>');
            }
        })
    };

    // Check if jQuery is loaded
    if (typeof window.jQuery != 'undefined') {
        bookmarklet();
    } else {
        // Check for conflicts
        var conflicts = typeof window.$ != 'undefined';
        // Create the script and point to Google API
        var script = document.createElement('script');
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' + jquery_version + "/jquery.min.js";
        // Add the script to the 'head' for processing
        document.head.appendChild(script);
        // Create a way to wait until script loading
        var attempts = 15;
        (function () {
            // Check again if jQuery is undefined
            if (typeof window.jQuery == 'undefined') {
                if (--attempts > 0) {
                    // Calls himself in a few milliseconds
                } else {
                    // Too much attempts to load, send error
                    alert('An error occurred while loading jQuery')
                }
            } else {
                bookmarklet();
            }
        })();
    }
})()
