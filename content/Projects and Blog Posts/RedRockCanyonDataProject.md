## Red Rock Canyon Data Project

Hello. Welcome to my Red Rock Canyon project Notebook.

The purpose of this notebook is to display both data scraping, cleaning and visualization skills by using one of my hobbies as a topic. As a Las Vegas local, hiking is one of my favorite parts about the city I live in. In this notebook I will be using the Red Rock Canyon website to data set of hikes/trails located in the canyon. I hope you enjoy.

-Richard Henderson


```python
#Importing dependencies...

from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import requests

```


```python
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


trails_page = requests.get(url = 'https://www.redrockcanyonlv.org/lasvegas/hikes-trails/', headers = user_agent).text
trails_soup = BeautifulSoup(trails_page, 'html.parser')
print(trails_soup)

#Above code allows us the parse the page from a URL of our choice.
```

    <!DOCTYPE html>

    <html lang="en-US">
    <head>
    <meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible"/><meta content="telephone=no" name="format-detection"/><title>Hikes &amp; Trails - Round-Trip Distances &amp; Times | Red Rock Canyon Las Vegas</title>
    <script type="text/javascript">var ajaxurl = "https://www.redrockcanyonlv.org/wp-admin/admin-ajax.php";</script>
    <!-- All in One SEO 4.1.5.3 -->
    <meta content="Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application." name="description">
    <meta content="max-image-preview:large" name="robots"/>
    <link href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/" rel="canonical"/>
    <link href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/page/2/" rel="next"/>
    <script class="aioseo-schema" type="application/ld+json">
    			{"@context":"https:\/\/schema.org","@graph":[{"@type":"WebSite","@id":"https:\/\/www.redrockcanyonlv.org\/#website","url":"https:\/\/www.redrockcanyonlv.org\/","name":"Red Rock Canyon Las Vegas","inLanguage":"en-US","publisher":{"@id":"https:\/\/www.redrockcanyonlv.org\/#organization"}},{"@type":"Organization","@id":"https:\/\/www.redrockcanyonlv.org\/#organization","name":"Red Rock Canyon Las Vegas","url":"https:\/\/www.redrockcanyonlv.org\/"},{"@type":"BreadcrumbList","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#breadcrumblist","itemListElement":[{"@type":"ListItem","@id":"https:\/\/www.redrockcanyonlv.org\/#listItem","position":1,"item":{"@type":"WebPage","@id":"https:\/\/www.redrockcanyonlv.org\/","name":"Home","description":"Red Rock Canyon features a one-way 13-mile scenic drive, a Visitor Center offering information and interpretation about recreation opportunities, hiking and trails, wildlife, vegetation, geology, cultural resources and much more.","url":"https:\/\/www.redrockcanyonlv.org\/"},"nextItem":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#listItem"},{"@type":"ListItem","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#listItem","position":2,"item":{"@type":"WebPage","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/","name":"Hikes &amp; Trails - Round-Trip Distances &amp; Times","description":"Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application.","url":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/"},"previousItem":"https:\/\/www.redrockcanyonlv.org\/#listItem"}]},{"@type":"CollectionPage","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#collectionpage","url":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/","name":"Hikes & Trails - Round-Trip Distances & Times | Red Rock Canyon Las Vegas","description":"Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application.","inLanguage":"en-US","isPartOf":{"@id":"https:\/\/www.redrockcanyonlv.org\/#website"},"breadcrumb":{"@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#breadcrumblist"}}]}
    		</script>
    <!-- All in One SEO -->
    <style id="critical-path-css" type="text/css">
    			body,html{width:100%;height:100%;margin:0;padding:0}.page-preloader{top:0;left:0;z-index:999;position:fixed;height:100%;width:100%;text-align:center}.preloader-preview-area{animation-delay:-.2s;top:50%;-ms-transform:translateY(100%);transform:translateY(100%);margin-top:10px;max-height:calc(50% - 20px);opacity:1;width:100%;text-align:center;position:absolute}.preloader-logo{max-width:90%;top:50%;-ms-transform:translateY(-100%);transform:translateY(-100%);margin:-10px auto 0 auto;max-height:calc(50% - 20px);opacity:1;position:relative}.ball-pulse>div{width:15px;height:15px;border-radius:100%;margin:2px;animation-fill-mode:both;display:inline-block;animation:ball-pulse .75s infinite cubic-bezier(.2,.68,.18,1.08)}.ball-pulse>div:nth-child(1){animation-delay:-.36s}.ball-pulse>div:nth-child(2){animation-delay:-.24s}.ball-pulse>div:nth-child(3){animation-delay:-.12s}@keyframes ball-pulse{0%{transform:scale(1);opacity:1}45%{transform:scale(.1);opacity:.7}80%{transform:scale(1);opacity:1}}.ball-clip-rotate-pulse{position:relative;-ms-transform:translateY(-15px) translateX(-10px);transform:translateY(-15px) translateX(-10px);display:inline-block}.ball-clip-rotate-pulse>div{animation-fill-mode:both;position:absolute;top:0;left:0;border-radius:100%}.ball-clip-rotate-pulse>div:first-child{height:36px;width:36px;top:7px;left:-7px;animation:ball-clip-rotate-pulse-scale 1s 0s cubic-bezier(.09,.57,.49,.9) infinite}.ball-clip-rotate-pulse>div:last-child{position:absolute;width:50px;height:50px;left:-16px;top:-2px;background:0 0;border:2px solid;animation:ball-clip-rotate-pulse-rotate 1s 0s cubic-bezier(.09,.57,.49,.9) infinite;animation-duration:1s}@keyframes ball-clip-rotate-pulse-rotate{0%{transform:rotate(0) scale(1)}50%{transform:rotate(180deg) scale(.6)}100%{transform:rotate(360deg) scale(1)}}@keyframes ball-clip-rotate-pulse-scale{30%{transform:scale(.3)}100%{transform:scale(1)}}@keyframes square-spin{25%{transform:perspective(100px) rotateX(180deg) rotateY(0)}50%{transform:perspective(100px) rotateX(180deg) rotateY(180deg)}75%{transform:perspective(100px) rotateX(0) rotateY(180deg)}100%{transform:perspective(100px) rotateX(0) rotateY(0)}}.square-spin{display:inline-block}.square-spin>div{animation-fill-mode:both;width:50px;height:50px;animation:square-spin 3s 0s cubic-bezier(.09,.57,.49,.9) infinite}.cube-transition{position:relative;-ms-transform:translate(-25px,-25px);transform:translate(-25px,-25px);display:inline-block}.cube-transition>div{animation-fill-mode:both;width:15px;height:15px;position:absolute;top:-5px;left:-5px;animation:cube-transition 1.6s 0s infinite ease-in-out}.cube-transition>div:last-child{animation-delay:-.8s}@keyframes cube-transition{25%{transform:translateX(50px) scale(.5) rotate(-90deg)}50%{transform:translate(50px,50px) rotate(-180deg)}75%{transform:translateY(50px) scale(.5) rotate(-270deg)}100%{transform:rotate(-360deg)}}.ball-scale>div{border-radius:100%;margin:2px;animation-fill-mode:both;display:inline-block;height:60px;width:60px;animation:ball-scale 1s 0s ease-in-out infinite}@keyframes ball-scale{0%{transform:scale(0)}100%{transform:scale(1);opacity:0}}.line-scale>div{animation-fill-mode:both;display:inline-block;width:5px;height:50px;border-radius:2px;margin:2px}.line-scale>div:nth-child(1){animation:line-scale 1s -.5s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(2){animation:line-scale 1s -.4s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(3){animation:line-scale 1s -.3s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(4){animation:line-scale 1s -.2s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(5){animation:line-scale 1s -.1s infinite cubic-bezier(.2,.68,.18,1.08)}@keyframes line-scale{0%{transform:scaley(1)}50%{transform:scaley(.4)}100%{transform:scaley(1)}}.ball-scale-multiple{position:relative;-ms-transform:translateY(30px);transform:translateY(30px);display:inline-block}.ball-scale-multiple>div{border-radius:100%;animation-fill-mode:both;margin:2px;position:absolute;left:-30px;top:0;opacity:0;margin:0;width:50px;height:50px;animation:ball-scale-multiple 1s 0s linear infinite}.ball-scale-multiple>div:nth-child(2){animation-delay:-.2s}.ball-scale-multiple>div:nth-child(3){animation-delay:-.2s}@keyframes ball-scale-multiple{0%{transform:scale(0);opacity:0}5%{opacity:1}100%{transform:scale(1);opacity:0}}.ball-pulse-sync{display:inline-block}.ball-pulse-sync>div{width:15px;height:15px;border-radius:100%;margin:2px;animation-fill-mode:both;display:inline-block}.ball-pulse-sync>div:nth-child(1){animation:ball-pulse-sync .6s -.21s infinite ease-in-out}.ball-pulse-sync>div:nth-child(2){animation:ball-pulse-sync .6s -.14s infinite ease-in-out}.ball-pulse-sync>div:nth-child(3){animation:ball-pulse-sync .6s -70ms infinite ease-in-out}@keyframes ball-pulse-sync{33%{transform:translateY(10px)}66%{transform:translateY(-10px)}100%{transform:translateY(0)}}.transparent-circle{display:inline-block;border-top:.5em solid rgba(255,255,255,.2);border-right:.5em solid rgba(255,255,255,.2);border-bottom:.5em solid rgba(255,255,255,.2);border-left:.5em solid #fff;transform:translateZ(0);animation:transparent-circle 1.1s infinite linear;width:50px;height:50px;border-radius:50%}.transparent-circle:after{border-radius:50%;width:10em;height:10em}@keyframes transparent-circle{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}.ball-spin-fade-loader{position:relative;top:-10px;left:-10px;display:inline-block}.ball-spin-fade-loader>div{width:15px;height:15px;border-radius:100%;margin:2px;animation-fill-mode:both;position:absolute;animation:ball-spin-fade-loader 1s infinite linear}.ball-spin-fade-loader>div:nth-child(1){top:25px;left:0;animation-delay:-.84s;-webkit-animation-delay:-.84s}.ball-spin-fade-loader>div:nth-child(2){top:17.05px;left:17.05px;animation-delay:-.72s;-webkit-animation-delay:-.72s}.ball-spin-fade-loader>div:nth-child(3){top:0;left:25px;animation-delay:-.6s;-webkit-animation-delay:-.6s}.ball-spin-fade-loader>div:nth-child(4){top:-17.05px;left:17.05px;animation-delay:-.48s;-webkit-animation-delay:-.48s}.ball-spin-fade-loader>div:nth-child(5){top:-25px;left:0;animation-delay:-.36s;-webkit-animation-delay:-.36s}.ball-spin-fade-loader>div:nth-child(6){top:-17.05px;left:-17.05px;animation-delay:-.24s;-webkit-animation-delay:-.24s}.ball-spin-fade-loader>div:nth-child(7){top:0;left:-25px;animation-delay:-.12s;-webkit-animation-delay:-.12s}.ball-spin-fade-loader>div:nth-child(8){top:17.05px;left:-17.05px;animation-delay:0s;-webkit-animation-delay:0s}@keyframes ball-spin-fade-loader{50%{opacity:.3;transform:scale(.4)}100%{opacity:1;transform:scale(1)}}		</style>
    <link href="//www.google.com" rel="dns-prefetch"/>
    <link href="//s.w.org" rel="dns-prefetch"/>
    <link href="https://www.redrockcanyonlv.org/feed/" rel="alternate" title="Red Rock Canyon Las Vegas » Feed" type="application/rss+xml"/>
    <link href="https://www.redrockcanyonlv.org/comments/feed/" rel="alternate" title="Red Rock Canyon Las Vegas » Comments Feed" type="application/rss+xml"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/images/favicon.png" rel="shortcut icon"/>
    <link href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/feed/" rel="alternate" title="Red Rock Canyon Las Vegas » Hikes &amp; Trails - Round-Trip Distances &amp; Times Category Feed" type="application/rss+xml"/>
    <script type="text/javascript">window.abb = {};php = {};window.PHP = {};PHP.ajax = "https://www.redrockcanyonlv.org/wp-admin/admin-ajax.php";PHP.wp_p_id = "";var mk_header_parallax, mk_banner_parallax, mk_page_parallax, mk_footer_parallax, mk_body_parallax;var mk_images_dir = "https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/images",mk_theme_js_path = "https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js",mk_theme_dir = "https://www.redrockcanyonlv.org/wp-content/themes/jupiter",mk_captcha_placeholder = "Enter Captcha",mk_captcha_invalid_txt = "Invalid. Try again.",mk_captcha_correct_txt = "Captcha correct.",mk_responsive_nav_width = 1220,mk_vertical_header_back = "Back",mk_vertical_header_anim = "1",mk_check_rtl = true,mk_grid_width = 1200,mk_ajax_search_option = "fullscreen_search",mk_preloader_bg_color = "#fff",mk_accent_color = "#841617",mk_go_to_top =  "false",mk_smooth_scroll =  "true",mk_preloader_bar_color = "#841617",mk_preloader_logo = "https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png";mk_typekit_id   = "",mk_google_fonts = ["Cabin:100italic,200italic,300italic,400italic,500italic,600italic,700italic,800italic,900italic,100,200,300,400,500,600,700,800,900"],mk_global_lazyload = true;</script> <style type="text/css">
    	.wp-pagenavi{float:left !important; }
    	</style>
    <link href="https://www.redrockcanyonlv.org/wp-includes/css/dashicons.min.css" id="dashicons-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/wunderground/assets/css/wunderground.css" id="wunderground-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/jquery-colorbox/themes/theme6/colorbox.css" id="colorbox-theme6-css" media="screen" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-includes/css/dist/block-library/style.min.css" id="wp-block-library-css" media="all" rel="stylesheet" type="text/css"/>
    <style id="wp-block-library-theme-inline-css" type="text/css">
    #start-resizable-editor-section{display:none}.wp-block-audio figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-audio figcaption{color:hsla(0,0%,100%,.65)}.wp-block-code{font-family:Menlo,Consolas,monaco,monospace;color:#1e1e1e;padding:.8em 1em;border:1px solid #ddd;border-radius:4px}.wp-block-embed figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-embed figcaption{color:hsla(0,0%,100%,.65)}.blocks-gallery-caption{color:#555;font-size:13px;text-align:center}.is-dark-theme .blocks-gallery-caption{color:hsla(0,0%,100%,.65)}.wp-block-image figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-image figcaption{color:hsla(0,0%,100%,.65)}.wp-block-pullquote{border-top:4px solid;border-bottom:4px solid;margin-bottom:1.75em;color:currentColor}.wp-block-pullquote__citation,.wp-block-pullquote cite,.wp-block-pullquote footer{color:currentColor;text-transform:uppercase;font-size:.8125em;font-style:normal}.wp-block-quote{border-left:.25em solid;margin:0 0 1.75em;padding-left:1em}.wp-block-quote cite,.wp-block-quote footer{color:currentColor;font-size:.8125em;position:relative;font-style:normal}.wp-block-quote.has-text-align-right{border-left:none;border-right:.25em solid;padding-left:0;padding-right:1em}.wp-block-quote.has-text-align-center{border:none;padding-left:0}.wp-block-quote.is-large,.wp-block-quote.is-style-large{border:none}.wp-block-search .wp-block-search__label{font-weight:700}.wp-block-group.has-background{padding:1.25em 2.375em;margin-top:0;margin-bottom:0}.wp-block-separator{border:none;border-bottom:2px solid;margin-left:auto;margin-right:auto;opacity:.4}.wp-block-separator:not(.is-style-wide):not(.is-style-dots){width:100px}.wp-block-separator.has-background:not(.is-style-dots){border-bottom:none;height:1px}.wp-block-separator.has-background:not(.is-style-wide):not(.is-style-dots){height:2px}.wp-block-table thead{border-bottom:3px solid}.wp-block-table tfoot{border-top:3px solid}.wp-block-table td,.wp-block-table th{padding:.5em;border:1px solid;word-break:normal}.wp-block-table figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-table figcaption{color:hsla(0,0%,100%,.65)}.wp-block-video figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-video figcaption{color:hsla(0,0%,100%,.65)}.wp-block-template-part.has-background{padding:1.25em 2.375em;margin-top:0;margin-bottom:0}#end-resizable-editor-section{display:none}
    </style>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/events-manager/includes/css/events_manager.css" id="events-manager-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/wp-fullcalendar/includes/css/main.css" id="wp-fullcalendar-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/min/full-styles.6.10.0.css" id="theme-styles-css" media="all" rel="stylesheet" type="text/css"/>
    <style id="theme-styles-inline-css" type="text/css">

    			#wpadminbar {
    				-webkit-backface-visibility: hidden;
    				backface-visibility: hidden;
    				-webkit-perspective: 1000;
    				-ms-perspective: 1000;
    				perspective: 1000;
    				-webkit-transform: translateZ(0px);
    				-ms-transform: translateZ(0px);
    				transform: translateZ(0px);
    			}
    			@media screen and (max-width: 600px) {
    				#wpadminbar {
    					position: fixed !important;
    				}
    			}

    body { background-color:#fff; } .hb-custom-header #mk-page-introduce, .mk-header { background-color:#2b6ca3;background-image:url(https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-header-bg.jpg);background-position:center center;background-size:cover;-webkit-background-size:cover;-moz-background-size:cover; } .hb-custom-header > div, .mk-header-bg { background:-webkit-linear-gradient(top,#ffffff 0%, #eeeeee 100%);background:linear-gradient(to bottom,#ffffff 0%, #eeeeee 100%) } .mk-classic-nav-bg { background:-webkit-linear-gradient(top,#ffffff 0%, #eeeeee 100%);background:linear-gradient(to bottom,#ffffff 0%, #eeeeee 100%) } .master-holder-bg { background-color:#fff; } #mk-footer { background-color:#7d909f; } #mk-boxed-layout { -webkit-box-shadow:0 0 px rgba(0, 0, 0, ); -moz-box-shadow:0 0 px rgba(0, 0, 0, ); box-shadow:0 0 px rgba(0, 0, 0, ); } .mk-news-tab .mk-tabs-tabs .is-active a, .mk-fancy-title.pattern-style span, .mk-fancy-title.pattern-style.color-gradient span:after, .page-bg-color { background-color:#fff; } .page-title { font-size:30px; color:#ffffff; text-transform:uppercase; font-weight:700; letter-spacing:2px; } .page-subtitle { font-size:16px; line-height:100%; color:#e5e5e5; font-size:16px; text-transform:none; } .mk-header { border-bottom:1px solid #ededed; } .header-style-1 .mk-header-padding-wrapper, .header-style-2 .mk-header-padding-wrapper, .header-style-3 .mk-header-padding-wrapper { padding-top:136px; } .mk-process-steps[max-width~="950px"] ul::before { display:none !important; } .mk-process-steps[max-width~="950px"] li { margin-bottom:30px !important; width:100% !important; text-align:center; } .mk-event-countdown-ul[max-width~="750px"] li { width:90%; display:block; margin:0 auto 15px; } body { font-family:Cabin } @font-face { font-family:'star'; src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.eot'); src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.eot?#iefix') format('embedded-opentype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.woff') format('woff'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.ttf') format('truetype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.svg#star') format('svg'); font-weight:normal; font-style:normal; } @font-face { font-family:'WooCommerce'; src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.eot'); src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.eot?#iefix') format('embedded-opentype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.woff') format('woff'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.ttf') format('truetype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.svg#WooCommerce') format('svg'); font-weight:normal; font-style:normal; }
    </style>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/css/mkhb-render.css" id="mkhb-render-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/css/mkhb-row.css" id="mkhb-row-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/css/mkhb-column.css" id="mkhb-column-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/uploads/mk_assets/theme-options-production-1638917485.css" id="theme-options-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/jupiter-donut/assets/css/shortcodes-styles.min.css" id="jupiter-donut-shortcodes-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter-child/style.css" id="mk-style-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/wp-pagenavi-style/css/css3_gray_glossy.css" id="wp-pagenavi-style-css" media="all" rel="stylesheet" type="text/css"/>
    <script id="jquery-core-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/jquery.min.js" type="text/javascript"></script>
    <script id="jquery-migrate-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/jquery-migrate.min.js" type="text/javascript"></script>
    <script id="jquery-ui-core-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/core.min.js" type="text/javascript"></script>
    <script id="jquery-ui-menu-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/menu.min.js" type="text/javascript"></script>
    <script id="regenerator-runtime-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/vendor/regenerator-runtime.min.js" type="text/javascript"></script>
    <script id="wp-polyfill-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/vendor/wp-polyfill.min.js" type="text/javascript"></script>
    <script id="wp-dom-ready-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/dom-ready.min.js" type="text/javascript"></script>
    <script id="wp-hooks-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/hooks.min.js" type="text/javascript"></script>
    <script id="wp-i18n-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/i18n.min.js" type="text/javascript"></script>
    <script id="wp-i18n-js-after" type="text/javascript">
    wp.i18n.setLocaleData( { 'text direction\u0004ltr': [ 'ltr' ] } );
    </script>
    <script id="wp-a11y-js-translations" type="text/javascript">
    ( function( domain, translations ) {
    	var localeData = translations.locale_data[ domain ] || translations.locale_data.messages;
    	localeData[""].domain = domain;
    	wp.i18n.setLocaleData( localeData, domain );
    } )( "default", { "locale_data": { "messages": { "": {} } } } );
    </script>
    <script id="wp-a11y-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/a11y.min.js" type="text/javascript"></script>
    <script id="jquery-ui-autocomplete-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var uiAutocompleteL10n = {"noResults":"No results found.","oneResult":"1 result found. Use up and down arrow keys to navigate.","manyResults":"%d results found. Use up and down arrow keys to navigate.","itemSelected":"Item selected."};
    /* ]]> */
    </script>
    <script id="jquery-ui-autocomplete-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/autocomplete.min.js" type="text/javascript"></script>
    <script id="wunderground-widget-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var WuWidget = {"apiKey":"3ffab52910ec1a0e","_wpnonce":"e05fa5b9e4","ajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php","is_admin":"","subdomain":"www"};
    /* ]]> */
    </script>
    <script id="wunderground-widget-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/wunderground/assets/js/widget.min.js" type="text/javascript"></script>
    <script id="colorbox-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var jQueryColorboxSettingsArray = {"jQueryColorboxVersion":"4.6.2","colorboxInline":"false","colorboxIframe":"false","colorboxGroupId":"","colorboxTitle":"","colorboxWidth":"false","colorboxHeight":"false","colorboxMaxWidth":"false","colorboxMaxHeight":"false","colorboxSlideshow":"false","colorboxSlideshowAuto":"false","colorboxScalePhotos":"false","colorboxPreloading":"false","colorboxOverlayClose":"false","colorboxLoop":"true","colorboxEscKey":"true","colorboxArrowKey":"true","colorboxScrolling":"true","colorboxOpacity":"0.85","colorboxTransition":"elastic","colorboxSpeed":"350","colorboxSlideshowSpeed":"2500","colorboxClose":"close","colorboxNext":"next","colorboxPrevious":"previous","colorboxSlideshowStart":"start slideshow","colorboxSlideshowStop":"stop slideshow","colorboxCurrent":"{current} of {total} images","colorboxXhrError":"This content failed to load.","colorboxImgError":"This image failed to load.","colorboxImageMaxWidth":"false","colorboxImageMaxHeight":"false","colorboxImageHeight":"false","colorboxImageWidth":"false","colorboxLinkHeight":"false","colorboxLinkWidth":"false","colorboxInitialHeight":"100","colorboxInitialWidth":"300","autoColorboxJavaScript":"","autoHideFlash":"true","autoColorbox":"","autoColorboxGalleries":"true","addZoomOverlay":"","useGoogleJQuery":"","colorboxAddClassToLinks":""};
    /* ]]> */
    </script>
    <script id="colorbox-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/jquery-colorbox/js/jquery.colorbox-min.js" type="text/javascript"></script>
    <script id="colorbox-wrapper-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/jquery-colorbox/js/jquery-colorbox-wrapper-min.js" type="text/javascript"></script>
    <script id="jquery-ui-mouse-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/mouse.min.js" type="text/javascript"></script>
    <script id="jquery-ui-sortable-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/sortable.min.js" type="text/javascript"></script>
    <script data-no-minify="" data-noptimize="" id="mk-webfontloader-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js/plugins/wp-enqueue/min/webfontloader.js" type="text/javascript"></script>
    <script id="mk-webfontloader-js-after" type="text/javascript">
    WebFontConfig = {
    	timeout: 2000
    }

    if ( mk_typekit_id.length > 0 ) {
    	WebFontConfig.typekit = {
    		id: mk_typekit_id
    	}
    }

    if ( mk_google_fonts.length > 0 ) {
    	WebFontConfig.google = {
    		families:  mk_google_fonts
    	}
    }

    if ( (mk_google_fonts.length > 0 || mk_typekit_id.length > 0) && navigator.userAgent.indexOf("Speed Insights") == -1) {
    	WebFont.load( WebFontConfig );
    }

    </script>
    <script id="jquery-ui-datepicker-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/datepicker.min.js" type="text/javascript"></script>
    <script id="jquery-ui-datepicker-js-after" type="text/javascript">
    jQuery(document).ready(function(jQuery){jQuery.datepicker.setDefaults({"closeText":"Close","currentText":"Today","monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Previous","dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"dateFormat":"MM d, yy","firstDay":1,"isRTL":false});});
    </script>
    <script id="jquery-ui-resizable-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/resizable.min.js" type="text/javascript"></script>
    <script id="jquery-ui-draggable-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/draggable.min.js" type="text/javascript"></script>
    <script id="jquery-ui-controlgroup-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/controlgroup.min.js" type="text/javascript"></script>
    <script id="jquery-ui-checkboxradio-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/checkboxradio.min.js" type="text/javascript"></script>
    <script id="jquery-ui-button-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/button.min.js" type="text/javascript"></script>
    <script id="jquery-ui-dialog-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/dialog.min.js" type="text/javascript"></script>
    <script id="events-manager-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var EM = {"ajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php","locationajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php?action=locations_search","firstDay":"1","locale":"en","dateFormat":"mm\/dd\/yy","ui_css":"https:\/\/www.redrockcanyonlv.org\/wp-content\/plugins\/events-manager\/includes\/css\/jquery-ui.min.css","show24hours":"0","is_ssl":"1","txt_search":"Search","txt_searching":"Searching...","txt_loading":"Loading..."};
    /* ]]> */
    </script>
    <script id="events-manager-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/events-manager/includes/js/events-manager.js" type="text/javascript"></script>
    <script id="jquery-ui-selectmenu-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/selectmenu.min.js" type="text/javascript"></script>
    <script id="jquery-ui-tooltip-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/tooltip.min.js" type="text/javascript"></script>
    <script id="moment-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/vendor/moment.min.js" type="text/javascript"></script>
    <script id="moment-js-after" type="text/javascript">
    moment.updateLocale( 'en_US', {"months":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthsShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"weekdays":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"weekdaysShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"week":{"dow":1},"longDateFormat":{"LT":"g:i a","LTS":null,"L":null,"LL":"F j, Y","LLL":"F j, Y g:i a","LLLL":null}} );
    </script>
    <script id="wp-fullcalendar-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var WPFC = {"ajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php?action=WP_FullCalendar","firstDay":"1","wpfc_theme":"","wpfc_limit":"6","wpfc_limit_txt":"","timeFormat":"h(:mm)a","defaultView":"month","weekends":"true","header":{"left":"prev,next today","center":"title","right":"month,basicWeek,basicDay"},"wpfc_qtips":""};
    /* ]]> */
    </script>
    <script id="wp-fullcalendar-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/wp-fullcalendar/includes/js/main.js" type="text/javascript"></script>
    <link href="https://www.redrockcanyonlv.org/wp-json/" rel="https://api.w.org/"/><link href="https://www.redrockcanyonlv.org/wp-json/wp/v2/categories/7" rel="alternate" type="application/json"/><link href="https://www.redrockcanyonlv.org/xmlrpc.php?rsd" rel="EditURI" title="RSD" type="application/rsd+xml"/>
    <link href="https://www.redrockcanyonlv.org/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
    <style type="text/css">
    	 .wp-pagenavi
    	{
    		font-size:12px !important;
    	}
    	</style>
    <link href="/wp-content/uploads/fbrfg/apple-touch-icon.png" rel="apple-touch-icon" sizes="152x152"/>
    <link href="/wp-content/uploads/fbrfg/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
    <link href="/wp-content/uploads/fbrfg/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
    <link href="/wp-content/uploads/fbrfg/manifest.json" rel="manifest"/>
    <link color="#5bbad5" href="/wp-content/uploads/fbrfg/safari-pinned-tab.svg" rel="mask-icon"/>
    <link href="/wp-content/uploads/fbrfg/favicon.ico" rel="shortcut icon"/>
    <meta content="/wp-content/uploads/fbrfg/browserconfig.xml" name="msapplication-config"/>
    <meta content="#ffffff" name="theme-color"/><meta content="" itemprop="author"><meta content="July 27, 2012" itemprop="datePublished"><meta content="February 21, 2020" itemprop="dateModified"/><meta content="Red Rock Canyon Las Vegas" itemprop="publisher"/><script> var isTest = false; </script><meta content="Powered by WPBakery Page Builder - drag and drop page builder for WordPress." name="generator"/>
    <style type="text/css">.grecaptcha-badge {
        display: none !important;
    }</style><meta content="Jupiter Child Theme " name="generator"/><noscript><style> .wpb_animate_when_almost_visible { opacity: 1; }</style></noscript><script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-13102530-33', 'auto');
      ga('send', 'pageview');

    </script>
    </meta></meta></meta></head>
    <body class="archive category category-hikes-trails category-7 wpb-js-composer js-comp-ver-6.7.0 vc_responsive" data-adminbar="" data-rsssl="1" itemscope="itemscope" itemtype="https://schema.org/WebPage">
    <!-- Target for scroll anchors to achieve native browser bahaviour + possible enhancements like smooth scrolling -->
    <div id="top-of-page"></div>
    <div id="mk-boxed-layout">
    <div id="mk-theme-container">
    <header class="mk-header header-style-1 header-align-left toolbar-true menu-hover-2 sticky-style-slide mk-background-stretch full-header" data-header-style="1" data-height="100" data-responsive-height="100" data-sticky-height="55" data-sticky-offset="header" data-sticky-style="slide" data-transparent-skin="" id="mk-header-1" itemscope="itemscope" itemtype="https://schema.org/WPHeader" role="banner">
    <div class="mk-header-holder">
    <div class="mk-header-toolbar">
    <div class="mk-header-toolbar-holder">
    <span class="mk-header-tagline"><a class="button" href="https://goo.gl/maps/X8LKj9bXcMT2" target="_blank">Driving Directions</a> <a class="button" href="https://www.redrockcanyonlv.org/fees/">Fees &amp; Passes</a></span><div class="mk-header-social toolbar-section"><ul><li><a class="mk-simple-rounded facebook-hover" href="https://www.facebook.com/RedRockCanyonLV/" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e0128" data-name="mk-jupiter-icon-simple-facebook" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192.191 92.743v60.485h-63.638v96.181h63.637v256.135h97.069v-256.135h84.168s6.674-51.322 9.885-96.508h-93.666v-42.921c0-8.807 11.565-20.661 23.01-20.661h71.791v-95.719h-83.57c-111.317 0-108.686 86.262-108.686 99.142z"></path></svg></a></li><li><a class="mk-simple-rounded instagram-hover" href="https://www.instagram.com/redrockcanyonlv/" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e01a8" data-name="mk-jupiter-icon-simple-instagram" style=" height:16px; width: 16px; " viewbox="0 0 81.2 81.2" xmlns="http://www.w3.org/2000/svg"><path d="M81,23.9c-0.2-4.3-0.9-7.3-1.9-9.9c-1-2.7-2.4-4.9-4.7-7.2c-2.3-2.3-4.5-3.6-7.2-4.7c-2.6-1-5.5-1.7-9.9-1.9 C53,0,51.6,0,40.6,0c-11,0-12.4,0-16.7,0.2c-4.3,0.2-7.3,0.9-9.9,1.9c-2.7,1-4.9,2.4-7.2,4.7C4.6,9.1,3.2,11.3,2.1,14 c-1,2.6-1.7,5.5-1.9,9.9C0,28.2,0,29.6,0,40.6c0,11,0,12.4,0.2,16.7c0.2,4.3,0.9,7.3,1.9,9.9c1,2.7,2.4,4.9,4.7,7.2 c2.3,2.3,4.5,3.6,7.2,4.7c2.6,1,5.5,1.7,9.9,1.9c4.3,0.2,5.7,0.2,16.7,0.2c11,0,12.4,0,16.7-0.2c4.3-0.2,7.3-0.9,9.9-1.9 c2.7-1,4.9-2.4,7.2-4.7c2.3-2.3,3.6-4.5,4.7-7.2c1-2.6,1.7-5.5,1.9-9.9c0.2-4.3,0.2-5.7,0.2-16.7C81.2,29.6,81.2,28.2,81,23.9z  M73.6,57c-0.2,4-0.8,6.1-1.4,7.5c-0.7,1.9-1.6,3.2-3,4.7c-1.4,1.4-2.8,2.3-4.7,3c-1.4,0.6-3.6,1.2-7.5,1.4 c-4.3,0.2-5.6,0.2-16.4,0.2c-10.8,0-12.1,0-16.4-0.2c-4-0.2-6.1-0.8-7.5-1.4c-1.9-0.7-3.2-1.6-4.7-3c-1.4-1.4-2.3-2.8-3-4.7 C8.4,63.1,7.7,61,7.6,57c-0.2-4.3-0.2-5.6-0.2-16.4c0-10.8,0-12.1,0.2-16.4c0.2-4,0.8-6.1,1.4-7.5c0.7-1.9,1.6-3.2,3-4.7 c1.4-1.4,2.8-2.3,4.7-3c1.4-0.6,3.6-1.2,7.5-1.4c4.3-0.2,5.6-0.2,16.4-0.2c10.8,0,12.1,0,16.4,0.2c4,0.2,6.1,0.8,7.5,1.4 c1.9,0.7,3.2,1.6,4.7,3c1.4,1.4,2.3,2.8,3,4.7c0.6,1.4,1.2,3.6,1.4,7.5c0.2,4.3,0.2,5.6,0.2,16.4C73.9,51.4,73.8,52.7,73.6,57z"></path><path d="M40.6,19.8c-11.5,0-20.8,9.3-20.8,20.8c0,11.5,9.3,20.8,20.8,20.8c11.5,0,20.8-9.3,20.8-20.8 C61.4,29.1,52.1,19.8,40.6,19.8z M40.6,54.1c-7.5,0-13.5-6.1-13.5-13.5c0-7.5,6.1-13.5,13.5-13.5c7.5,0,13.5,6.1,13.5,13.5 C54.1,48.1,48.1,54.1,40.6,54.1z"></path><circle cx="62.3" cy="18.9" r="4.9"></circle></svg></a></li><li><a class="mk-simple-rounded google-hover" href="https://goo.gl/maps/X8LKj9bXcMT2" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e01f7" data-name="mk-jupiter-icon-simple-google" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M431.474-6.4h-139.076c-36.469 0-82.376 5.372-120.846 36.925-29.069 24.875-43.219 59.114-43.219 90.04 0 52.392 40.522 105.507 112.082 105.507 6.749 0 14.135-.686 21.632-1.328-3.378 8.029-6.793 14.751-6.793 26.189 0 20.838 10.801 33.575 20.253 45.692-30.35 2.007-87.08 5.358-128.964 30.86-39.833 23.57-52.019 57.808-52.019 81.997 0 49.736 47.292 96.121 145.196 96.121 116.149 0 177.591-63.83 177.591-127.039 0-46.312-27.009-69.188-56.7-94.055l-24.327-18.787c-7.394-6.081-17.512-14.11-17.512-28.898 0-14.78 10.119-24.211 18.875-32.941 28.358-22.159 56.716-45.677 56.716-95.397 0-51.086-32.433-77.961-47.959-90.719h41.914l43.158-24.166zm-59.352 411.202c0 41.633-34.476 72.537-99.31 72.537-72.228 0-118.831-34.254-118.831-81.953 0-47.728 43.218-63.815 58.056-69.187 28.38-9.445 64.834-10.774 70.908-10.774 6.756 0 10.119 0 15.542.649 51.351 36.29 73.635 54.474 73.635 88.726zm-54.048-216.363c-10.815 10.737-29.07 18.795-45.945 18.795-58.048 0-84.376-74.589-84.376-119.587 0-17.481 3.378-35.597 14.838-49.72 10.808-13.445 29.706-22.182 47.27-22.182 56.049 0 85.102 75.26 85.102 123.623 0 12.116-1.378 33.59-16.889 49.072z"></path></svg></a></li><li><a class="mk-simple-rounded twitter-hover" href="https://twitter.com/RedRockCynLV" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e0264" data-name="mk-jupiter-icon-simple-twitter" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M454.058 213.822c28.724-2.382 48.193-15.423 55.683-33.132-10.365 6.373-42.524 13.301-60.269 6.681-.877-4.162-1.835-8.132-2.792-11.706-13.527-49.679-59.846-89.698-108.382-84.865 3.916-1.589 7.914-3.053 11.885-4.388 5.325-1.923 36.678-7.003 31.749-18.079-4.176-9.728-42.471 7.352-49.672 9.597 9.501-3.581 25.26-9.735 26.93-20.667-14.569 1.991-28.901 8.885-39.937 18.908 3.998-4.293 7.01-9.536 7.666-15.171-38.91 24.85-61.624 74.932-80.025 123.523-14.438-13.972-27.239-25.008-38.712-31.114-32.209-17.285-70.722-35.303-131.156-57.736-1.862 19.996 9.899 46.591 43.723 64.273-7.325-.986-20.736 1.219-31.462 3.773 4.382 22.912 18.627 41.805 57.251 50.918-17.642 1.163-26.767 5.182-35.036 13.841 8.043 15.923 27.656 34.709 62.931 30.82-39.225 16.935-15.998 48.234 15.93 43.565-54.444 56.244-140.294 52.123-189.596 5.08 128.712 175.385 408.493 103.724 450.21-65.225 31.23.261 49.605-10.823 60.994-23.05-17.99 3.053-44.072-.095-57.914-5.846z"></path></svg></a></li></ul><div class="clearboth"></div></div>
    </div>
    </div>
    <div class="mk-header-inner add-header-height">
    <div class="mk-header-bg"></div>
    <div class="mk-toolbar-resposnive-icon"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e0326" data-name="mk-icon-chevron-down" viewbox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1683 808l-742 741q-19 19-45 19t-45-19l-742-741q-19-19-19-45.5t19-45.5l166-165q19-19 45-19t45 19l531 531 531-531q19-19 45-19t45 19l166 165q19 19 19 45.5t-19 45.5z"></path></svg></div>
    <div class="mk-header-nav-container one-row-style menu-hover-style-2" itemscope="itemscope" itemtype="https://schema.org/SiteNavigationElement" role="navigation">
    <nav class="mk-main-navigation js-main-nav"><ul class="main-navigation-ul" id="menu-main-menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home no-mega-menu" id="menu-item-9249"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e41b9" data-name="mk-moon-home-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 304l-96-96v-144h-64v80l-96-96-256 256v16h64v160h160v-96h64v96h160v-160h64z"></path></svg>Home</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-ancestor current-menu-parent menu-item-has-children no-mega-menu" id="menu-item-472"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/redrockcanyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e42b5" data-name="mk-icon-map-marker" style=" height:16px; width: 9.1428571428571px; " viewbox="0 0 1024 1792" xmlns="http://www.w3.org/2000/svg"><path d="M768 640q0-106-75-181t-181-75-181 75-75 181 75 181 181 75 181-75 75-181zm256 0q0 109-33 179l-364 774q-16 33-47.5 52t-67.5 19-67.5-19-46.5-52l-365-774q-33-70-33-179 0-212 150-362t362-150 362 150 150 362z"></path></svg>Plan A Visit</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-9251"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/fees/">Fees &amp; Passes</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-511"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/visitor-information/">Visitor Information</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item" id="menu-item-930"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/">Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-382"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/geology-highlights/">Geology Highlights</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-396"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/weather/">Weather Information</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item no-mega-menu" id="menu-item-862"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e4514" data-name="mk-moon-direction" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M400 192l96-64-96-64h-112v-40c0-13.2-10.8-24-24-24h-16c-13.2 0-24 10.8-24 24v40h-160v128h160v32h-144l-64 48 64 48h144v192h64v-192h128v-96h-128v-32h112z"></path></svg>Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children no-mega-menu" id="menu-item-7306"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/events/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e45e9" data-name="mk-icon-calendar" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M128 1664h288v-288h-288v288zm352 0h320v-288h-320v288zm-352-352h288v-320h-288v320zm352 0h320v-320h-320v320zm-352-384h288v-288h-288v288zm736 736h320v-288h-320v288zm-384-736h320v-288h-320v288zm768 736h288v-288h-288v288zm-384-352h320v-320h-320v320zm-352-864v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm736 864h288v-320h-288v320zm-384-384h320v-288h-320v288zm384 0h288v-288h-288v288zm32-480v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm384-64v1280q0 52-38 90t-90 38h-1408q-52 0-90-38t-38-90v-1280q0-52 38-90t90-38h128v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h384v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h128q52 0 90 38t38 90z"></path></svg>Events</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-7311"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/event-calendar/">Event Calendar</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-7304"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/upcoming-events/">Upcoming Events List</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children no-mega-menu" id="menu-item-9453"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/programs/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e479c" data-name="mk-moon-map-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M0 96l160-64v384l-160 64zm352 0v384l-160-53.333v-384zm160-64v384l-128 51.2v-384z"></path></svg>Programs</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9391"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/red-rock-canyon-a-to-z/">Red Rock Canyon A To Z</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9390"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/wildlife-wednesday/">Wildlife Wednesday</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9389"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/flower-friday/">Flower Friday</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-9417"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/jackson-the-burro/">Jackson the Red Rock Canyon Burro</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-1226"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/tortoise-habitat/">Tortoise Habitat</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-9416"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/artist-in-residence/">Artist In Residence Program</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page no-mega-menu" id="menu-item-1184"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/shop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e49a7" data-name="mk-icon-shopping-cart" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M640 1536q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm896 0q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm128-1088v512q0 24-16 42.5t-41 21.5l-1044 122q1 7 4.5 21.5t6 26.5 2.5 22q0 16-24 64h920q26 0 45 19t19 45-19 45-45 19h-1024q-26 0-45-19t-19-45q0-14 11-39.5t29.5-59.5 20.5-38l-177-823h-204q-26 0-45-19t-19-45 19-45 45-19h256q16 0 28.5 6.5t20 15.5 13 24.5 7.5 26.5 5.5 29.5 4.5 25.5h1201q26 0 45 19t19 45z"></path></svg>Shop</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children no-mega-menu" id="menu-item-5076"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e4b02" data-name="mk-moon-users" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M367.497 402.687c-9.476-1.494-9.692-27.327-9.692-27.327s27.844-27.328 33.912-64.076c16.326 0 26.407-39.069 10.082-52.814.681-14.47 20.984-113.588-81.799-113.588-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.816-144.503 54.658-144.503 109.313h384c0-54.655-113.979-104.497-144.503-109.313zm-195.47 8.718c22.047-13.575 48.813-26.154 70.769-33.712-7.876-11.216-16.647-26.468-22.165-44.531-7.703-6.283-13.972-15.266-17.999-26.301-4.033-11.052-5.561-23.426-4.304-34.842.902-8.196 3.239-15.833 6.825-22.544-2.175-23.293-3.707-69.017 26.224-102.366 11.607-12.933 26.278-22.23 43.85-27.843-3.137-32.38-19.58-70.385-83.227-70.385-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.817-144.503 54.659-144.503 109.314h164.798c2.355-1.537 4.753-3.07 7.229-4.595z"></path></svg>About</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-89"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/contact-us/">Contact Us</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9279"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/news/">News</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-5079"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/">Our Mission</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-5078"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/opportunities/">Opportunities</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-1114"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/frequently-asked-questions/">FAQ</a></li>
    </ul>
    </li>
    </ul></nav>
    <div class="main-nav-side-search">
    <a class="mk-search-trigger add-header-height mk-fullscreen-trigger" href="#"><i class="mk-svg-icon-wrapper"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e4d7f" data-name="mk-icon-search" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1152 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></i></a>
    </div>
    </div>
    <div class="mk-nav-responsive-link">
    <div class="mk-css-icon-menu">
    <div class="mk-css-icon-menu-line-1"></div>
    <div class="mk-css-icon-menu-line-2"></div>
    <div class="mk-css-icon-menu-line-3"></div>
    </div>
    </div> <div class="header-logo fit-logo-img add-header-height logo-is-responsive logo-has-sticky">
    <a href="https://www.redrockcanyonlv.org/" title="Red Rock Canyon Las Vegas">
    <img alt="" class="mk-desktop-logo dark-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    <img alt="" class="mk-desktop-logo light-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    <img alt="" class="mk-resposnive-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    <img alt="" class="mk-sticky-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    </a>
    </div>
    <div class="mk-header-right">
    </div>
    </div>
    <div class="mk-responsive-wrap">
    <nav class="menu-main-menu-container"><ul class="mk-responsive-nav" id="menu-main-menu-1"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home" id="responsive-menu-item-9249"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e615c" data-name="mk-moon-home-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 304l-96-96v-144h-64v80l-96-96-256 256v16h64v160h160v-96h64v96h160v-160h64z"></path></svg>Home</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-ancestor current-menu-parent menu-item-has-children" id="responsive-menu-item-472"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/redrockcanyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e625e" data-name="mk-icon-map-marker" style=" height:16px; width: 9.1428571428571px; " viewbox="0 0 1024 1792" xmlns="http://www.w3.org/2000/svg"><path d="M768 640q0-106-75-181t-181-75-181 75-75 181 75 181 181 75 181-75 75-181zm256 0q0 109-33 179l-364 774q-16 33-47.5 52t-67.5 19-67.5-19-46.5-52l-365-774q-33-70-33-179 0-212 150-362t362-150 362 150 150 362z"></path></svg>Plan A Visit</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6393" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-9251"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/fees/">Fees &amp; Passes</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-511"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/visitor-information/">Visitor Information</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item" id="responsive-menu-item-930"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/">Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-382"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/geology-highlights/">Geology Highlights</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-396"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/weather/">Weather Information</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item" id="responsive-menu-item-862"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6676" data-name="mk-moon-direction" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M400 192l96-64-96-64h-112v-40c0-13.2-10.8-24-24-24h-16c-13.2 0-24 10.8-24 24v40h-160v128h160v32h-144l-64 48 64 48h144v192h64v-192h128v-96h-128v-32h112z"></path></svg>Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children" id="responsive-menu-item-7306"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/events/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6757" data-name="mk-icon-calendar" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M128 1664h288v-288h-288v288zm352 0h320v-288h-320v288zm-352-352h288v-320h-288v320zm352 0h320v-320h-320v320zm-352-384h288v-288h-288v288zm736 736h320v-288h-320v288zm-384-736h320v-288h-320v288zm768 736h288v-288h-288v288zm-384-352h320v-320h-320v320zm-352-864v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm736 864h288v-320h-288v320zm-384-384h320v-288h-320v288zm384 0h288v-288h-288v288zm32-480v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm384-64v1280q0 52-38 90t-90 38h-1408q-52 0-90-38t-38-90v-1280q0-52 38-90t90-38h128v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h384v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h128q52 0 90 38t38 90z"></path></svg>Events</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6895" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-7311"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/event-calendar/">Event Calendar</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-7304"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/upcoming-events/">Upcoming Events List</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children" id="responsive-menu-item-9453"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/programs/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6a91" data-name="mk-moon-map-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M0 96l160-64v384l-160 64zm352 0v384l-160-53.333v-384zm160-64v384l-128 51.2v-384z"></path></svg>Programs</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6be6" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9391"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/red-rock-canyon-a-to-z/">Red Rock Canyon A To Z</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9390"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/wildlife-wednesday/">Wildlife Wednesday</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9389"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/flower-friday/">Flower Friday</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-9417"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/jackson-the-burro/">Jackson the Red Rock Canyon Burro</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-1226"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/tortoise-habitat/">Tortoise Habitat</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-9416"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/artist-in-residence/">Artist In Residence Program</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-1184"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/shop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6e89" data-name="mk-icon-shopping-cart" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M640 1536q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm896 0q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm128-1088v512q0 24-16 42.5t-41 21.5l-1044 122q1 7 4.5 21.5t6 26.5 2.5 22q0 16-24 64h920q26 0 45 19t19 45-19 45-45 19h-1024q-26 0-45-19t-19-45q0-14 11-39.5t29.5-59.5 20.5-38l-177-823h-204q-26 0-45-19t-19-45 19-45 45-19h256q16 0 28.5 6.5t20 15.5 13 24.5 7.5 26.5 5.5 29.5 4.5 25.5h1201q26 0 45 19t19 45z"></path></svg>Shop</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children" id="responsive-menu-item-5076"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e6ffa" data-name="mk-moon-users" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M367.497 402.687c-9.476-1.494-9.692-27.327-9.692-27.327s27.844-27.328 33.912-64.076c16.326 0 26.407-39.069 10.082-52.814.681-14.47 20.984-113.588-81.799-113.588-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.816-144.503 54.658-144.503 109.313h384c0-54.655-113.979-104.497-144.503-109.313zm-195.47 8.718c22.047-13.575 48.813-26.154 70.769-33.712-7.876-11.216-16.647-26.468-22.165-44.531-7.703-6.283-13.972-15.266-17.999-26.301-4.033-11.052-5.561-23.426-4.304-34.842.902-8.196 3.239-15.833 6.825-22.544-2.175-23.293-3.707-69.017 26.224-102.366 11.607-12.933 26.278-22.23 43.85-27.843-3.137-32.38-19.58-70.385-83.227-70.385-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.817-144.503 54.659-144.503 109.314h164.798c2.355-1.537 4.753-3.07 7.229-4.595z"></path></svg>About</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e713a" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-89"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/contact-us/">Contact Us</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9279"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/news/">News</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-5079"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/">Our Mission</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-5078"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/opportunities/">Opportunities</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-1114"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/frequently-asked-questions/">FAQ</a></li>
    </ul>
    </li>
    </ul></nav>
    <form action="https://www.redrockcanyonlv.org/" class="responsive-searchform" method="get">
    <input class="text-input" id="s" name="s" placeholder="Search.." type="text" value=""/>
    <i><input type="submit" value=""/><svg class="mk-svg-icon" data-cacheid="icon-6205c444e73ab" data-name="mk-icon-search" viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1152 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></i>
    </form>
    </div>
    </div>
    <div class="mk-header-padding-wrapper"></div>
    <section class="intro-left" id="mk-page-introduce"><div class="mk-grid"><h1 class="page-title mk-drop-shadow">Hikes &amp; Trails – Round-Trip Distances &amp; Times</h1><div class="page-subtitle">Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application.
    </div><div id="mk-breadcrumbs"><div class="mk-breadcrumbs-inner dark-skin"><span xmlns:v="http://rdf.data-vocabulary.org/#"><span typeof="v:Breadcrumb"><a href="https://www.redrockcanyonlv.org/" property="v:title" rel="v:url">Home</a> / <span rel="v:child" typeof="v:Breadcrumb"><span class="breadcrumb-categoris-holder"><a href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/">Hikes &amp; Trails - Round-Trip Distances &amp; Times</a> <span>/</span> </span></span></span></span></div></div><div class="clearboth"></div></div></section>
    </header>
    <div class="master-holder clearfix" id="theme-page" itemprop="mainContentOfPage" role="main">
    <div class="master-holder-bg-holder">
    <div class="master-holder-bg js-el" id="theme-page-bg"></div>
    </div>
    <div class="mk-main-wrapper-holder">
    <div class="theme-page-wrapper mk-main-wrapper mk-grid right-layout">
    <div class="theme-content" itemprop="mainContentOfPage">
    <section "item":".mk-isotop-item"}"="" class="js-loop js-el clearfix mk-blog-container mk-newspaper-wrapper mag-one-column mk-blog-container-lazyload js-loop--loaded" container":"#loop-2",="" data-grid-config="{" data-loop-iterator="10" data-loop-posts="" data-max-pages="1" data-mk-component="Grid" data-pagination-style="1" id="loop-2" itemscope="itemscope" itemtype="https://schema.org/Blog">
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-794 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-794">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/moenkopi-loop/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-794 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-150x150.jpg 150w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Moenkopi-Trail-WB-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/moenkopi-loop/" rel="bookmark">Moenkopi Loop</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/moenkopi-loop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e8a95" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">1</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-796 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-796">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/calico-hills/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-796 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/89847837_10212334377592928_2798931110497615872_o-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/calico-hills/" rel="bookmark">Calico Hills</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/calico-hills/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e8f18" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">2</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-798 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-798">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/calico-tanks/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-798 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Calico-Tank-WB-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/calico-tanks/" rel="bookmark">Calico Tanks</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/calico-tanks/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e9390" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">3</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-800 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-800">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/turtlehead-peak/">
    <img alt="Turtle Head Peak" class="attachment-500x500 size-500x500 colorbox-800 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/turtle-head-peak-trails-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/turtlehead-peak/" rel="bookmark">Turtlehead Peak</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/turtlehead-peak/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e9832" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">4</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-803 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-803">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/keystone-thrust/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-803 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/img_8972-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/keystone-thrust/" rel="bookmark">Keystone Thrust</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/keystone-thrust/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444e9cde" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">5</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-805 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-805">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/white-rock-willow-springs/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-805 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-195x195.jpg 195w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Red-Rock-Canyon-National-Conservation-Area-104-266x266.jpg 266w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/white-rock-willow-springs/" rel="bookmark">White Rock – Willow Springs</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/white-rock-willow-springs/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ea21a" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">6</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9663 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9663">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/grand-circle-loop/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9663 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-550x550.jpg 550w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-195x195.jpg 195w, https://www.redrockcanyonlv.org/wp-content/uploads/grand-cirle-2-150x150.jpg 150w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/grand-circle-loop/" rel="bookmark">Grand Circle Loop</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/grand-circle-loop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ea86c" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">7</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-807 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-807">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/white-rock-la-madre-spring-loop/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-807 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/LaMadre-Spring-WB-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/white-rock-la-madre-spring-loop/" rel="bookmark">White Rock Mountain Loop</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/white-rock-la-madre-spring-loop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444eacee" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">8</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-812 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-812">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/willow-springs-loop/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-812 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-195x195.jpg 195w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Willow-Springs-Agave-Roasting-Pit-WB-266x266.jpg 266w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/willow-springs-loop/" rel="bookmark">Willow Spring Loop</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/willow-springs-loop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444eb15f" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">9</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-814 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-814">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/la-madre-spring/">
    <img alt="La Madre Springs" class="attachment-500x500 size-500x500 colorbox-814 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-195x195.jpg 195w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/la-madre-springs-266x266.jpg 266w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/la-madre-spring/" rel="bookmark">La Madre Spring</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/la-madre-spring/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444eb5f8" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">10</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9666 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9666">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/petroglyph-wall-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9666 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/petroglyph-wall-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/petroglyph-wall-trail/" rel="bookmark">Petroglyph Wall</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/petroglyph-wall-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444eba6e" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">11</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9669 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9669">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/north-peak-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9669 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/img_4992-500x500.jpeg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/img_4992-500x500.jpeg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/img_4992-300x300.jpeg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/img_4992-266x266.jpeg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/img_4992-195x195.jpeg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/north-peak-trail/" rel="bookmark">North Peak</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/north-peak-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ebf04" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">12</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9672 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9672">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/bridge-mountain-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9672 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/bridge-mtn-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/bridge-mountain-trail/" rel="bookmark">Bridge Mountain</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/bridge-mountain-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ec36a" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">13</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-810 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-810">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/lost-creek-childrens-discovery/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-810 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/doi_8666-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/doi_8666-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/doi_8666-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/doi_8666-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/doi_8666-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/lost-creek-childrens-discovery/" rel="bookmark">Lost Creek – Children’s Discovery</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/lost-creek-childrens-discovery/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ec87e" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">14</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-816 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-816">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/smyc/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-816 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Lost-Creek-Hike-Discovery-Trail-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/smyc/" rel="bookmark">SMYC</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/smyc/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ecd17" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">15</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-818 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-818">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/ice-box-canyon/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-818 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Ice-Box-Canyon-WB-3-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/ice-box-canyon/" rel="bookmark">Ice Box Canyon</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/ice-box-canyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ed18c" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">16</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-820 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-820">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/dales/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-820 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Dales-Trail-Scenery-WB-2-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/dales/" rel="bookmark">Dale’s</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/dales/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ed607" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">17</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-822 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-822">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/pine-creek-canyon/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-822 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-019-WB-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/pine-creek-canyon/" rel="bookmark">Pine Creek Canyon</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/pine-creek-canyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444edb12" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">18</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-824 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-824">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/fire-ecology/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-824 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Fire-Ecology-View-from-Pine-Creek-WB-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/fire-ecology/" rel="bookmark">Fire Ecology</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/fire-ecology/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444edfab" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">19</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-828 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-828">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/arnight/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-828 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-550x550.jpg 550w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Arnight-WB-3-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/arnight/" rel="bookmark">Arnight</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/arnight/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ee42c" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">20</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-830 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-830">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/knoll/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-830 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-550x550.jpg 550w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Pine-Creek-Trail-047-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/knoll/" rel="bookmark">Knoll</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/knoll/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ee8c7" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">21</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-826 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-826">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/oak-creek-canyon/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-826 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-45x45.jpg 45w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-550x550.jpg 550w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-150x150.jpg 150w, https://www.redrockcanyonlv.org/wp-content/uploads/2012/07/Oak-Creek-WB-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/oak-creek-canyon/" rel="bookmark">Oak Creek Canyon</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/oak-creek-canyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444eed6c" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">22</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9675 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9675">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/oak-creek-cutoff/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9675 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-195x195.jpg 195w, https://www.redrockcanyonlv.org/wp-content/uploads/oak-creek-cutoff-550x550.jpg 550w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/oak-creek-cutoff/" rel="bookmark">Middle Oak Creek</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/oak-creek-cutoff/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ef1af" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">23</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9678 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9678">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/south-oak-creek/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9678 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/south-oak-creek-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/south-oak-creek/" rel="bookmark">South Oak Creek</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/south-oak-creek/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444ef5d4" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">24</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-832 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-832">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/first-creek-canyon/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-832 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/20161123_132745-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/first-creek-canyon/" rel="bookmark">First Creek Canyon</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/first-creek-canyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444efa12" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">25</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-9681 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-9681">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/kraft-boulders/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-9681 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-64x64.jpg 64w, https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-60x60.jpg 60w, https://www.redrockcanyonlv.org/wp-content/uploads/kraft-mtn-boulders-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/kraft-boulders/" rel="bookmark">Kraft Mountain Loop Hike</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/kraft-boulders/"><svg class="mk-svg-icon" data-cacheid="icon-6205c444efe81" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">26</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    </section><div class="wp-pagenavi" role="navigation">
    <span class="pages">Page 1 of 2</span><span aria-current="page" class="current">1</span><a class="page larger" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/page/2/" title="Page 2">2</a><a aria-label="Next Page" class="nextpostslink" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/page/2/" rel="next">»</a>
    </div> <div class="clearboth"></div>
    </div>
    <aside class="mk-builtin" id="mk-sidebar" itemscope="itemscope" itemtype="https://schema.org/WPSideBar" role="complementary">
    <div class="sidebar-wrapper">
    <section class="widget widget_text" id="text-21"><div class="widgettitle">Upcoming Events</div> <div class="textwidget"><div class="em-calendar-wrapper" id="em-calendar-122"><table class="em-calendar">
    <thead>
    <tr>
    <td><a class="em-calnav em-calnav-prev" href="/lasvegas/hikes-trails/?ajaxCalendar=1&amp;mo=1&amp;yr=2022" rel="nofollow">&lt;&lt;</a></td>
    <td class="month_name" colspan="5">Feb 2022</td>
    <td><a class="em-calnav em-calnav-next" href="/lasvegas/hikes-trails/?ajaxCalendar=1&amp;mo=3&amp;yr=2022" rel="nofollow">&gt;&gt;</a></td>
    </tr>
    </thead>
    <tbody>
    <tr class="days-names">
    <td>M</td><td>T</td><td>W</td><td>T</td><td>F</td><td>S</td><td>S</td>
    </tr>
    <tr>
    <td class="eventless-pre">
    										31									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/trail-talk-tuesday-pine-creek-8am-2-1-22/" title="Trail Talk Tuesday – Pine Creek">1</a>
    </td>
    <td class="eventless">
    										2									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-3-22/" title="Moenkopi Mornings Guided Hike">3</a>
    </td>
    <td class="eventless">
    										4									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-5-22/" title="Geology Tabletop at Calico I">5</a>
    </td>
    <td class="eventless">
    										6									</td>
    </tr><tr> <td class="eventless">
    										7									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/tabletop-tuesday-mountain-lion-9am-2-8-22/" title="Tabletop Tuesday – Mountain Lion">8</a>
    </td>
    <td class="eventless">
    										9									</td>
    <td class="eventful-today">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-10-22/" title="Moenkopi Mornings Guided Hike">10</a>
    </td>
    <td class="eventless">
    										11									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-12-22/" title="Geology Tabletop at Calico I">12</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/healthy-heart-hike-pine-creek-2-13-22/" title="Healthy Heart Hike – Pine Creek">13</a>
    </td>
    </tr><tr> <td class="eventless">
    										14									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/tabletop-tuesday-canines-of-red-rock-canyon-nca-9am-2-15-22/" title="Tabletop Tuesday – Canines of Red Rock Canyon NCA">15</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/campground-program-gila-monsters-6pm-2-16-22/" title="Campground Program – Gila Monsters">16</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-17-22/" title="Moenkopi Mornings Guided Hike">17</a>
    </td>
    <td class="eventless">
    										18									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-19-22/" title="Geology Tabletop at Calico I">19</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/fossil-ridge-hike-2-20-22/" title="Fossil Ridge Hike">20</a>
    </td>
    </tr><tr> <td class="eventless">
    										21									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/tabletop-tuesday-eagles-9am-2-22-22/" title="Tabletop Tuesday – Eagles">22</a>
    </td>
    <td class="eventless">
    										23									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-24-22/" title="Moenkopi Mornings Guided Hike">24</a>
    </td>
    <td class="eventless">
    										25									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-26-22/" title="Geology Tabletop at Calico I">26</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/healthy-heart-hike-la-madre-spring-2-27-22/" title="Healthy Heart Hike – La Madre Spring">27</a>
    </td>
    </tr><tr> <td class="eventless">
    										28									</td>
    <td class="eventful-post">
    <a href="https://www.redrockcanyonlv.org/events/trail-talk-tuesday-calico-hills-8am-3-1-22/" title="Trail Talk Tuesday – Calico Hills">1</a>
    </td>
    <td class="eventless-post">
    										2									</td>
    <td class="eventless-post">
    										3									</td>
    <td class="eventless-post">
    										4									</td>
    <td class="eventless-post">
    										5									</td>
    <td class="eventful-post">
    <a href="https://www.redrockcanyonlv.org/events/nature-walks-red-spring-7am-3-6-22/" title="Nature Walks – Red Spring">6</a>
    </td>
    </tr>
    </tbody>
    </table></div>
    <a class="button" href="https://www.redrockcanyonlv.org/event-calendar/">View Full Calendar</a></div>
    </section> </div>
    </aside>
    <div class="clearboth"></div>
    </div>
    </div>
    </div>
    <section id="mk-footer-unfold-spacer"></section>
    <section class="" id="mk-footer" itemscope="itemscope" itemtype="https://schema.org/WPFooter" role="contentinfo">
    <div class="footer-wrapper fullwidth-footer">
    <div class="mk-padding-wrapper">
    <div class="mk-col-1-4"><section class="widget widget_text" id="text-26"><div class="widgettitle">Who We Are</div> <div class="textwidget"><p><a href="https://www.redrockcanyonlv.org/our-mission/">Southern Nevada Conservancy</a>, a 501c3 nonprofit organization based in Las Vegas, NV, serves Red Rock Canyon National Conservation Area under a formal agreement with the Bureau of Land Management (BLM) in many ways, including interpretive programming, fee-station management, retail operations, and this website.</p>
    <p><a class="button" href="https://www.redrockcanyonlv.org/redrockcanyon/fees/">Fees &amp; Passes</a></p>
    </div>
    </section></div>
    <div class="mk-col-1-4"><section class="widget widget_nav_menu" id="nav_menu-2"><div class="widgettitle">Visit Red Rock Canyon</div>
    <div class="menu-footer-menu-container"><ul class="menu" id="menu-footer-menu">
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item menu-item-9245" id="menu-item-9245"><a aria-current="page" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/"><svg class="mk-svg-icon" data-cacheid="icon-6205c44503a5e" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Hikes &amp; Trails – Round-Trip Distances &amp; Times</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post menu-item-9247" id="menu-item-9247"><a href="https://www.redrockcanyonlv.org/fees/"><svg class="mk-svg-icon" data-cacheid="icon-6205c44503a5e" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Fees &amp; Passes</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post menu-item-9437" id="menu-item-9437"><a href="https://www.redrockcanyonlv.org/visitor-information/"><svg class="mk-svg-icon" data-cacheid="icon-6205c44503a5e" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Visitor Information</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9246" id="menu-item-9246"><a href="https://www.redrockcanyonlv.org/shop/"><svg class="mk-svg-icon" data-cacheid="icon-6205c44503a5e" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Shop</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9242" id="menu-item-9242"><a href="https://www.redrockcanyonlv.org/event-calendar/"><svg class="mk-svg-icon" data-cacheid="icon-6205c44503a5e" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Event Calendar</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1339" id="menu-item-1339"><a href="https://www.redrockcanyonlv.org/frequently-asked-questions/"><svg class="mk-svg-icon" data-cacheid="icon-6205c44503a5e" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>FAQ</a></li>
    </ul></div></section></div>
    <div class="mk-col-1-4"><section class="widget widget_text" id="text-24"><div class="widgettitle">Operating Hours</div> <div class="textwidget"><p><a href="https://www.redrockcanyonlv.org/red-rock-canyon-is-hot-hot-hot/" rel="noopener" target="_blank"><strong>PLEASE VISIT THIS PAGE FOR CURRENT OPERATING HOURS &amp; FACILITIES.</strong></a></p>
    <p>The Visitor Center is open daily from 9<strong>:00 AM – 4:30 pm</strong>.</p>
    <p>The Scenic Drive is open every day of the year with hours changing slightly according to the season:</p>
    <p><strong>Nov – Feb</strong> – 6:00 AM to 5:00 PM<br/>
    <strong>March</strong> – 6:00 AM to 7:00 PM<br/>
    <strong>Apr – Sep</strong> – 6:00 AM to 8:00 PM<br/>
    <strong>Oct</strong> – 6:00 AM to 7:00 PM</p>
    </div>
    </section></div>
    <div class="mk-col-1-4"><section class="widget widget_text" id="text-25"><div class="widgettitle">Get In Touch</div> <div class="textwidget"><p><strong>Red Rock Canyon</strong><br/>
    <strong>General Information &amp; Questions</strong><br/>
    Phone: <a href="tel:17025155350">+1 (702) 515-5350</a></p>
    <p><strong>Programs &amp; Guided Hikes</strong><br/>
    Phone: <a href="tel:17025155350">+1 (702) 515-5367</a></p>
    <p><strong>Elements Gift &amp; Book Store</strong><br/>
    Phone: <a href="tel:17025155379">+1 (702) 515-5379</a></p>
    <p><a class="button" href="https://goo.gl/maps/X8LKj9bXcMT2" rel="noopener" target="_blank">Driving Directions</a></p>
    </div>
    </section></div>
    <div class="clearboth"></div>
    </div>
    </div>
    <div id="sub-footer">
    <div class="fullwidth-footer">
    <span class="mk-footer-copyright">© Copyright 2017 - <a href="https://www.southernnevadaconservancy.org/" target="_blank">Southern Nevada Conservancy</a> |  All Rights Reserved.  | Website by: <a href="http://www.sitesmartmarketing.com" target="_blank">Site Smart Marketing</a></span>
    </div>
    <div class="clearboth"></div>
    </div>
    </section>
    </div>
    </div>
    <div class="bottom-corner-btns js-bottom-corner-btns">
    </div>
    <div class="mk-fullscreen-search-overlay">
    <a class="mk-fullscreen-close" href="#"><svg class="mk-svg-icon" data-cacheid="icon-6205c44504296" data-name="mk-moon-close-2" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M390.628 345.372l-45.256 45.256-89.372-89.373-89.373 89.372-45.255-45.255 89.373-89.372-89.372-89.373 45.254-45.254 89.373 89.372 89.372-89.373 45.256 45.255-89.373 89.373 89.373 89.372z"></path></svg></a>
    <div class="mk-fullscreen-search-wrapper">
    <p>Start typing and press Enter to search</p>
    <form action="https://www.redrockcanyonlv.org/" id="mk-fullscreen-searchform" method="get">
    <input id="mk-fullscreen-search-input" name="s" type="text" value=""/>
    <i class="fullscreen-search-icon"><svg class="mk-svg-icon" data-cacheid="icon-6205c4450433f" data-name="mk-icon-search" style=" height:25px; width: 23.214285714286px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1152 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></i>
    </form>
    </div>
    </div>
    <style type="text/css"></style><script type="text/javascript">
        php = {
            hasAdminbar: false,
            json: (null != null) ? null : "",
            jsPath: 'https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js'
          };
        </script><script id="google-invisible-recaptcha-js-before" type="text/javascript">
    var renderInvisibleReCaptcha = function() {

        for (var i = 0; i < document.forms.length; ++i) {
            var form = document.forms[i];
            var holder = form.querySelector('.inv-recaptcha-holder');

            if (null === holder) continue;
    		holder.innerHTML = '';

             (function(frm){
    			var cf7SubmitElm = frm.querySelector('.wpcf7-submit');
                var holderId = grecaptcha.render(holder,{
                    'sitekey': '6Lc1tbsZAAAAAA2NJDh7vLq2eDoOGmA2jYsM6-_z', 'size': 'invisible', 'badge' : 'bottomright',
                    'callback' : function (recaptchaToken) {
    					if((null !== cf7SubmitElm) && (typeof jQuery != 'undefined')){jQuery(frm).submit();grecaptcha.reset(holderId);return;}
    					 HTMLFormElement.prototype.submit.call(frm);
                    },
                    'expired-callback' : function(){grecaptcha.reset(holderId);}
                });

    			if(null !== cf7SubmitElm && (typeof jQuery != 'undefined') ){
    				jQuery(cf7SubmitElm).off('click').on('click', function(clickEvt){
    					clickEvt.preventDefault();
    					grecaptcha.execute(holderId);
    				});
    			}
    			else
    			{
    				frm.onsubmit = function (evt){evt.preventDefault();grecaptcha.execute(holderId);};
    			}


            })(form);
        }
    };
    </script>
    <script async="" defer="" id="google-invisible-recaptcha-js" src="https://www.google.com/recaptcha/api.js?onload=renderInvisibleReCaptcha&amp;render=explicit" type="text/javascript"></script>
    <script id="smoothscroll-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js/plugins/wp-enqueue/min/smoothscroll.js" type="text/javascript"></script>
    <script id="theme-scripts-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js/min/full-scripts.6.10.0.js" type="text/javascript"></script>
    <script id="mkhb-render-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/js/mkhb-render.js" type="text/javascript"></script>
    <script id="mkhb-column-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/js/mkhb-column.js" type="text/javascript"></script>
    <script id="jupiter-donut-shortcodes-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var jupiterDonutVars = {"themeDir":"https:\/\/www.redrockcanyonlv.org\/wp-content\/themes\/jupiter","assetsUrl":"https:\/\/www.redrockcanyonlv.org\/wp-content\/plugins\/jupiter-donut\/assets","gridWidth":"1200","ajaxUrl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php","nonce":"5dd3aa9f3e"};
    /* ]]> */
    </script>
    <script id="jupiter-donut-shortcodes-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/jupiter-donut/assets/js/shortcodes-scripts.min.js" type="text/javascript"></script>
    <script id="wp-embed-js" src="https://www.redrockcanyonlv.org/wp-includes/js/wp-embed.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    		jQuery(document).ready(function () {
      equalHeight('article div.mk-blog-meta');
    	//equalHeight('article div.featured-image');

    	//jQuery(window).resize(function(){jQuery('article div.featured-image').removeAttr("style");equalHeight('article div.featured-image');});
    	jQuery(window).resize(function(){jQuery('article div.mk-blog-meta').removeAttr("style");equalHeight('article div.mk-blog-meta');});
    });
    function equalHeight(columnClass){
       var maxHeight = 0;

    jQuery(columnClass).each(function(){
       if (jQuery(this).height() > maxHeight) { maxHeight = jQuery(this).height(); }
    });
    jQuery(columnClass).height(maxHeight);
    }		</script>
    <script type="text/javascript">	window.get = {};	window.get.captcha = function(enteredCaptcha) {
                      return jQuery.get(ajaxurl, { action : "mk_validate_captcha_input", captcha: enteredCaptcha });
                  	};</script>
    </body>
    </html>
    <!--
    Performance optimized by W3 Total Cache. Learn more: https://www.boldgrid.com/w3-total-cache/

    Page Caching using disk: enhanced
    Database Caching 73/208 queries in 0.084 seconds using disk (Request-wide modification query)

    Served from: www.redrockcanyonlv.org @ 2022-02-10 18:04:53 by W3 Total Cache
    -->



```python
#There are actually two pages worth of trails. This does the same thing as above for the second page.
trails_page2 = requests.get(url = 'https://www.redrockcanyonlv.org/lasvegas/hikes-trails/page/2/',headers = user_agent).text
trails_soup2 = BeautifulSoup(trails_page2, 'html.parser')

trails_soup2

```




    <!DOCTYPE html>

    <html lang="en-US">
    <head>
    <meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible"/><meta content="telephone=no" name="format-detection"/><title>Hikes &amp; Trails - Round-Trip Distances &amp; Times | Red Rock Canyon Las Vegas - Part 2</title>
    <script type="text/javascript">var ajaxurl = "https://www.redrockcanyonlv.org/wp-admin/admin-ajax.php";</script>
    <!-- All in One SEO 4.1.5.3 -->
    <meta content="Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application. - Part 2" name="description">
    <meta content="noindex, nofollow, max-image-preview:large" name="robots"/>
    <link href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/page/2/" rel="canonical"/>
    <link href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/" rel="prev"/>
    <script class="aioseo-schema" type="application/ld+json">
    			{"@context":"https:\/\/schema.org","@graph":[{"@type":"WebSite","@id":"https:\/\/www.redrockcanyonlv.org\/#website","url":"https:\/\/www.redrockcanyonlv.org\/","name":"Red Rock Canyon Las Vegas","inLanguage":"en-US","publisher":{"@id":"https:\/\/www.redrockcanyonlv.org\/#organization"}},{"@type":"Organization","@id":"https:\/\/www.redrockcanyonlv.org\/#organization","name":"Red Rock Canyon Las Vegas","url":"https:\/\/www.redrockcanyonlv.org\/"},{"@type":"BreadcrumbList","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/page\/2\/#breadcrumblist","itemListElement":[{"@type":"ListItem","@id":"https:\/\/www.redrockcanyonlv.org\/#listItem","position":1,"item":{"@type":"WebPage","@id":"https:\/\/www.redrockcanyonlv.org\/","name":"Home","description":"Red Rock Canyon features a one-way 13-mile scenic drive, a Visitor Center offering information and interpretation about recreation opportunities, hiking and trails, wildlife, vegetation, geology, cultural resources and much more. - Part 2","url":"https:\/\/www.redrockcanyonlv.org\/"},"nextItem":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#listItem"},{"@type":"ListItem","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/#listItem","position":2,"item":{"@type":"WebPage","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/","name":"Hikes &amp; Trails - Round-Trip Distances &amp; Times","description":"Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application. - Part 2","url":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/"},"previousItem":"https:\/\/www.redrockcanyonlv.org\/#listItem"}]},{"@type":"CollectionPage","@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/page\/2\/#collectionpage","url":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/page\/2\/","name":"Hikes & Trails - Round-Trip Distances & Times | Red Rock Canyon Las Vegas - Part 2","description":"Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application. - Part 2","inLanguage":"en-US","isPartOf":{"@id":"https:\/\/www.redrockcanyonlv.org\/#website"},"breadcrumb":{"@id":"https:\/\/www.redrockcanyonlv.org\/lasvegas\/hikes-trails\/page\/2\/#breadcrumblist"}}]}
    		</script>
    <!-- All in One SEO -->
    <style id="critical-path-css" type="text/css">
    			body,html{width:100%;height:100%;margin:0;padding:0}.page-preloader{top:0;left:0;z-index:999;position:fixed;height:100%;width:100%;text-align:center}.preloader-preview-area{animation-delay:-.2s;top:50%;-ms-transform:translateY(100%);transform:translateY(100%);margin-top:10px;max-height:calc(50% - 20px);opacity:1;width:100%;text-align:center;position:absolute}.preloader-logo{max-width:90%;top:50%;-ms-transform:translateY(-100%);transform:translateY(-100%);margin:-10px auto 0 auto;max-height:calc(50% - 20px);opacity:1;position:relative}.ball-pulse>div{width:15px;height:15px;border-radius:100%;margin:2px;animation-fill-mode:both;display:inline-block;animation:ball-pulse .75s infinite cubic-bezier(.2,.68,.18,1.08)}.ball-pulse>div:nth-child(1){animation-delay:-.36s}.ball-pulse>div:nth-child(2){animation-delay:-.24s}.ball-pulse>div:nth-child(3){animation-delay:-.12s}@keyframes ball-pulse{0%{transform:scale(1);opacity:1}45%{transform:scale(.1);opacity:.7}80%{transform:scale(1);opacity:1}}.ball-clip-rotate-pulse{position:relative;-ms-transform:translateY(-15px) translateX(-10px);transform:translateY(-15px) translateX(-10px);display:inline-block}.ball-clip-rotate-pulse>div{animation-fill-mode:both;position:absolute;top:0;left:0;border-radius:100%}.ball-clip-rotate-pulse>div:first-child{height:36px;width:36px;top:7px;left:-7px;animation:ball-clip-rotate-pulse-scale 1s 0s cubic-bezier(.09,.57,.49,.9) infinite}.ball-clip-rotate-pulse>div:last-child{position:absolute;width:50px;height:50px;left:-16px;top:-2px;background:0 0;border:2px solid;animation:ball-clip-rotate-pulse-rotate 1s 0s cubic-bezier(.09,.57,.49,.9) infinite;animation-duration:1s}@keyframes ball-clip-rotate-pulse-rotate{0%{transform:rotate(0) scale(1)}50%{transform:rotate(180deg) scale(.6)}100%{transform:rotate(360deg) scale(1)}}@keyframes ball-clip-rotate-pulse-scale{30%{transform:scale(.3)}100%{transform:scale(1)}}@keyframes square-spin{25%{transform:perspective(100px) rotateX(180deg) rotateY(0)}50%{transform:perspective(100px) rotateX(180deg) rotateY(180deg)}75%{transform:perspective(100px) rotateX(0) rotateY(180deg)}100%{transform:perspective(100px) rotateX(0) rotateY(0)}}.square-spin{display:inline-block}.square-spin>div{animation-fill-mode:both;width:50px;height:50px;animation:square-spin 3s 0s cubic-bezier(.09,.57,.49,.9) infinite}.cube-transition{position:relative;-ms-transform:translate(-25px,-25px);transform:translate(-25px,-25px);display:inline-block}.cube-transition>div{animation-fill-mode:both;width:15px;height:15px;position:absolute;top:-5px;left:-5px;animation:cube-transition 1.6s 0s infinite ease-in-out}.cube-transition>div:last-child{animation-delay:-.8s}@keyframes cube-transition{25%{transform:translateX(50px) scale(.5) rotate(-90deg)}50%{transform:translate(50px,50px) rotate(-180deg)}75%{transform:translateY(50px) scale(.5) rotate(-270deg)}100%{transform:rotate(-360deg)}}.ball-scale>div{border-radius:100%;margin:2px;animation-fill-mode:both;display:inline-block;height:60px;width:60px;animation:ball-scale 1s 0s ease-in-out infinite}@keyframes ball-scale{0%{transform:scale(0)}100%{transform:scale(1);opacity:0}}.line-scale>div{animation-fill-mode:both;display:inline-block;width:5px;height:50px;border-radius:2px;margin:2px}.line-scale>div:nth-child(1){animation:line-scale 1s -.5s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(2){animation:line-scale 1s -.4s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(3){animation:line-scale 1s -.3s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(4){animation:line-scale 1s -.2s infinite cubic-bezier(.2,.68,.18,1.08)}.line-scale>div:nth-child(5){animation:line-scale 1s -.1s infinite cubic-bezier(.2,.68,.18,1.08)}@keyframes line-scale{0%{transform:scaley(1)}50%{transform:scaley(.4)}100%{transform:scaley(1)}}.ball-scale-multiple{position:relative;-ms-transform:translateY(30px);transform:translateY(30px);display:inline-block}.ball-scale-multiple>div{border-radius:100%;animation-fill-mode:both;margin:2px;position:absolute;left:-30px;top:0;opacity:0;margin:0;width:50px;height:50px;animation:ball-scale-multiple 1s 0s linear infinite}.ball-scale-multiple>div:nth-child(2){animation-delay:-.2s}.ball-scale-multiple>div:nth-child(3){animation-delay:-.2s}@keyframes ball-scale-multiple{0%{transform:scale(0);opacity:0}5%{opacity:1}100%{transform:scale(1);opacity:0}}.ball-pulse-sync{display:inline-block}.ball-pulse-sync>div{width:15px;height:15px;border-radius:100%;margin:2px;animation-fill-mode:both;display:inline-block}.ball-pulse-sync>div:nth-child(1){animation:ball-pulse-sync .6s -.21s infinite ease-in-out}.ball-pulse-sync>div:nth-child(2){animation:ball-pulse-sync .6s -.14s infinite ease-in-out}.ball-pulse-sync>div:nth-child(3){animation:ball-pulse-sync .6s -70ms infinite ease-in-out}@keyframes ball-pulse-sync{33%{transform:translateY(10px)}66%{transform:translateY(-10px)}100%{transform:translateY(0)}}.transparent-circle{display:inline-block;border-top:.5em solid rgba(255,255,255,.2);border-right:.5em solid rgba(255,255,255,.2);border-bottom:.5em solid rgba(255,255,255,.2);border-left:.5em solid #fff;transform:translateZ(0);animation:transparent-circle 1.1s infinite linear;width:50px;height:50px;border-radius:50%}.transparent-circle:after{border-radius:50%;width:10em;height:10em}@keyframes transparent-circle{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}.ball-spin-fade-loader{position:relative;top:-10px;left:-10px;display:inline-block}.ball-spin-fade-loader>div{width:15px;height:15px;border-radius:100%;margin:2px;animation-fill-mode:both;position:absolute;animation:ball-spin-fade-loader 1s infinite linear}.ball-spin-fade-loader>div:nth-child(1){top:25px;left:0;animation-delay:-.84s;-webkit-animation-delay:-.84s}.ball-spin-fade-loader>div:nth-child(2){top:17.05px;left:17.05px;animation-delay:-.72s;-webkit-animation-delay:-.72s}.ball-spin-fade-loader>div:nth-child(3){top:0;left:25px;animation-delay:-.6s;-webkit-animation-delay:-.6s}.ball-spin-fade-loader>div:nth-child(4){top:-17.05px;left:17.05px;animation-delay:-.48s;-webkit-animation-delay:-.48s}.ball-spin-fade-loader>div:nth-child(5){top:-25px;left:0;animation-delay:-.36s;-webkit-animation-delay:-.36s}.ball-spin-fade-loader>div:nth-child(6){top:-17.05px;left:-17.05px;animation-delay:-.24s;-webkit-animation-delay:-.24s}.ball-spin-fade-loader>div:nth-child(7){top:0;left:-25px;animation-delay:-.12s;-webkit-animation-delay:-.12s}.ball-spin-fade-loader>div:nth-child(8){top:17.05px;left:-17.05px;animation-delay:0s;-webkit-animation-delay:0s}@keyframes ball-spin-fade-loader{50%{opacity:.3;transform:scale(.4)}100%{opacity:1;transform:scale(1)}}		</style>
    <link href="//www.google.com" rel="dns-prefetch"/>
    <link href="//s.w.org" rel="dns-prefetch"/>
    <link href="https://www.redrockcanyonlv.org/feed/" rel="alternate" title="Red Rock Canyon Las Vegas » Feed" type="application/rss+xml"/>
    <link href="https://www.redrockcanyonlv.org/comments/feed/" rel="alternate" title="Red Rock Canyon Las Vegas » Comments Feed" type="application/rss+xml"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/images/favicon.png" rel="shortcut icon"/>
    <link href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/feed/" rel="alternate" title="Red Rock Canyon Las Vegas » Hikes &amp; Trails - Round-Trip Distances &amp; Times Category Feed" type="application/rss+xml"/>
    <script type="text/javascript">window.abb = {};php = {};window.PHP = {};PHP.ajax = "https://www.redrockcanyonlv.org/wp-admin/admin-ajax.php";PHP.wp_p_id = "";var mk_header_parallax, mk_banner_parallax, mk_page_parallax, mk_footer_parallax, mk_body_parallax;var mk_images_dir = "https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/images",mk_theme_js_path = "https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js",mk_theme_dir = "https://www.redrockcanyonlv.org/wp-content/themes/jupiter",mk_captcha_placeholder = "Enter Captcha",mk_captcha_invalid_txt = "Invalid. Try again.",mk_captcha_correct_txt = "Captcha correct.",mk_responsive_nav_width = 1220,mk_vertical_header_back = "Back",mk_vertical_header_anim = "1",mk_check_rtl = true,mk_grid_width = 1200,mk_ajax_search_option = "fullscreen_search",mk_preloader_bg_color = "#fff",mk_accent_color = "#841617",mk_go_to_top =  "false",mk_smooth_scroll =  "true",mk_preloader_bar_color = "#841617",mk_preloader_logo = "https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png";mk_typekit_id   = "",mk_google_fonts = ["Cabin:100italic,200italic,300italic,400italic,500italic,600italic,700italic,800italic,900italic,100,200,300,400,500,600,700,800,900"],mk_global_lazyload = true;</script> <style type="text/css">
    	.wp-pagenavi{float:left !important; }
    	</style>
    <link href="https://www.redrockcanyonlv.org/wp-includes/css/dashicons.min.css" id="dashicons-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/wunderground/assets/css/wunderground.css" id="wunderground-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/jquery-colorbox/themes/theme6/colorbox.css" id="colorbox-theme6-css" media="screen" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-includes/css/dist/block-library/style.min.css" id="wp-block-library-css" media="all" rel="stylesheet" type="text/css"/>
    <style id="wp-block-library-theme-inline-css" type="text/css">
    #start-resizable-editor-section{display:none}.wp-block-audio figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-audio figcaption{color:hsla(0,0%,100%,.65)}.wp-block-code{font-family:Menlo,Consolas,monaco,monospace;color:#1e1e1e;padding:.8em 1em;border:1px solid #ddd;border-radius:4px}.wp-block-embed figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-embed figcaption{color:hsla(0,0%,100%,.65)}.blocks-gallery-caption{color:#555;font-size:13px;text-align:center}.is-dark-theme .blocks-gallery-caption{color:hsla(0,0%,100%,.65)}.wp-block-image figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-image figcaption{color:hsla(0,0%,100%,.65)}.wp-block-pullquote{border-top:4px solid;border-bottom:4px solid;margin-bottom:1.75em;color:currentColor}.wp-block-pullquote__citation,.wp-block-pullquote cite,.wp-block-pullquote footer{color:currentColor;text-transform:uppercase;font-size:.8125em;font-style:normal}.wp-block-quote{border-left:.25em solid;margin:0 0 1.75em;padding-left:1em}.wp-block-quote cite,.wp-block-quote footer{color:currentColor;font-size:.8125em;position:relative;font-style:normal}.wp-block-quote.has-text-align-right{border-left:none;border-right:.25em solid;padding-left:0;padding-right:1em}.wp-block-quote.has-text-align-center{border:none;padding-left:0}.wp-block-quote.is-large,.wp-block-quote.is-style-large{border:none}.wp-block-search .wp-block-search__label{font-weight:700}.wp-block-group.has-background{padding:1.25em 2.375em;margin-top:0;margin-bottom:0}.wp-block-separator{border:none;border-bottom:2px solid;margin-left:auto;margin-right:auto;opacity:.4}.wp-block-separator:not(.is-style-wide):not(.is-style-dots){width:100px}.wp-block-separator.has-background:not(.is-style-dots){border-bottom:none;height:1px}.wp-block-separator.has-background:not(.is-style-wide):not(.is-style-dots){height:2px}.wp-block-table thead{border-bottom:3px solid}.wp-block-table tfoot{border-top:3px solid}.wp-block-table td,.wp-block-table th{padding:.5em;border:1px solid;word-break:normal}.wp-block-table figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-table figcaption{color:hsla(0,0%,100%,.65)}.wp-block-video figcaption{color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-video figcaption{color:hsla(0,0%,100%,.65)}.wp-block-template-part.has-background{padding:1.25em 2.375em;margin-top:0;margin-bottom:0}#end-resizable-editor-section{display:none}
    </style>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/events-manager/includes/css/events_manager.css" id="events-manager-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/wp-fullcalendar/includes/css/main.css" id="wp-fullcalendar-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/min/full-styles.6.10.0.css" id="theme-styles-css" media="all" rel="stylesheet" type="text/css"/>
    <style id="theme-styles-inline-css" type="text/css">

    			#wpadminbar {
    				-webkit-backface-visibility: hidden;
    				backface-visibility: hidden;
    				-webkit-perspective: 1000;
    				-ms-perspective: 1000;
    				perspective: 1000;
    				-webkit-transform: translateZ(0px);
    				-ms-transform: translateZ(0px);
    				transform: translateZ(0px);
    			}
    			@media screen and (max-width: 600px) {
    				#wpadminbar {
    					position: fixed !important;
    				}
    			}

    body { background-color:#fff; } .hb-custom-header #mk-page-introduce, .mk-header { background-color:#2b6ca3;background-image:url(https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-header-bg.jpg);background-position:center center;background-size:cover;-webkit-background-size:cover;-moz-background-size:cover; } .hb-custom-header > div, .mk-header-bg { background:-webkit-linear-gradient(top,#ffffff 0%, #eeeeee 100%);background:linear-gradient(to bottom,#ffffff 0%, #eeeeee 100%) } .mk-classic-nav-bg { background:-webkit-linear-gradient(top,#ffffff 0%, #eeeeee 100%);background:linear-gradient(to bottom,#ffffff 0%, #eeeeee 100%) } .master-holder-bg { background-color:#fff; } #mk-footer { background-color:#7d909f; } #mk-boxed-layout { -webkit-box-shadow:0 0 px rgba(0, 0, 0, ); -moz-box-shadow:0 0 px rgba(0, 0, 0, ); box-shadow:0 0 px rgba(0, 0, 0, ); } .mk-news-tab .mk-tabs-tabs .is-active a, .mk-fancy-title.pattern-style span, .mk-fancy-title.pattern-style.color-gradient span:after, .page-bg-color { background-color:#fff; } .page-title { font-size:30px; color:#ffffff; text-transform:uppercase; font-weight:700; letter-spacing:2px; } .page-subtitle { font-size:16px; line-height:100%; color:#e5e5e5; font-size:16px; text-transform:none; } .mk-header { border-bottom:1px solid #ededed; } .header-style-1 .mk-header-padding-wrapper, .header-style-2 .mk-header-padding-wrapper, .header-style-3 .mk-header-padding-wrapper { padding-top:136px; } .mk-process-steps[max-width~="950px"] ul::before { display:none !important; } .mk-process-steps[max-width~="950px"] li { margin-bottom:30px !important; width:100% !important; text-align:center; } .mk-event-countdown-ul[max-width~="750px"] li { width:90%; display:block; margin:0 auto 15px; } body { font-family:Cabin } @font-face { font-family:'star'; src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.eot'); src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.eot?#iefix') format('embedded-opentype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.woff') format('woff'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.ttf') format('truetype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/star/font.svg#star') format('svg'); font-weight:normal; font-style:normal; } @font-face { font-family:'WooCommerce'; src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.eot'); src:url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.eot?#iefix') format('embedded-opentype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.woff') format('woff'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.ttf') format('truetype'), url('https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/stylesheet/fonts/woocommerce/font.svg#WooCommerce') format('svg'); font-weight:normal; font-style:normal; }
    </style>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/css/mkhb-render.css" id="mkhb-render-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/css/mkhb-row.css" id="mkhb-row-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/css/mkhb-column.css" id="mkhb-column-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/uploads/mk_assets/theme-options-production-1638917485.css" id="theme-options-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/jupiter-donut/assets/css/shortcodes-styles.min.css" id="jupiter-donut-shortcodes-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/themes/jupiter-child/style.css" id="mk-style-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="https://www.redrockcanyonlv.org/wp-content/plugins/wp-pagenavi-style/css/css3_gray_glossy.css" id="wp-pagenavi-style-css" media="all" rel="stylesheet" type="text/css"/>
    <script id="jquery-core-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/jquery.min.js" type="text/javascript"></script>
    <script id="jquery-migrate-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/jquery-migrate.min.js" type="text/javascript"></script>
    <script id="jquery-ui-core-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/core.min.js" type="text/javascript"></script>
    <script id="jquery-ui-menu-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/menu.min.js" type="text/javascript"></script>
    <script id="regenerator-runtime-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/vendor/regenerator-runtime.min.js" type="text/javascript"></script>
    <script id="wp-polyfill-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/vendor/wp-polyfill.min.js" type="text/javascript"></script>
    <script id="wp-dom-ready-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/dom-ready.min.js" type="text/javascript"></script>
    <script id="wp-hooks-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/hooks.min.js" type="text/javascript"></script>
    <script id="wp-i18n-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/i18n.min.js" type="text/javascript"></script>
    <script id="wp-i18n-js-after" type="text/javascript">
    wp.i18n.setLocaleData( { 'text direction\u0004ltr': [ 'ltr' ] } );
    </script>
    <script id="wp-a11y-js-translations" type="text/javascript">
    ( function( domain, translations ) {
    	var localeData = translations.locale_data[ domain ] || translations.locale_data.messages;
    	localeData[""].domain = domain;
    	wp.i18n.setLocaleData( localeData, domain );
    } )( "default", { "locale_data": { "messages": { "": {} } } } );
    </script>
    <script id="wp-a11y-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/a11y.min.js" type="text/javascript"></script>
    <script id="jquery-ui-autocomplete-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var uiAutocompleteL10n = {"noResults":"No results found.","oneResult":"1 result found. Use up and down arrow keys to navigate.","manyResults":"%d results found. Use up and down arrow keys to navigate.","itemSelected":"Item selected."};
    /* ]]> */
    </script>
    <script id="jquery-ui-autocomplete-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/autocomplete.min.js" type="text/javascript"></script>
    <script id="wunderground-widget-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var WuWidget = {"apiKey":"3ffab52910ec1a0e","_wpnonce":"e05fa5b9e4","ajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php","is_admin":"","subdomain":"www"};
    /* ]]> */
    </script>
    <script id="wunderground-widget-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/wunderground/assets/js/widget.min.js" type="text/javascript"></script>
    <script id="colorbox-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var jQueryColorboxSettingsArray = {"jQueryColorboxVersion":"4.6.2","colorboxInline":"false","colorboxIframe":"false","colorboxGroupId":"","colorboxTitle":"","colorboxWidth":"false","colorboxHeight":"false","colorboxMaxWidth":"false","colorboxMaxHeight":"false","colorboxSlideshow":"false","colorboxSlideshowAuto":"false","colorboxScalePhotos":"false","colorboxPreloading":"false","colorboxOverlayClose":"false","colorboxLoop":"true","colorboxEscKey":"true","colorboxArrowKey":"true","colorboxScrolling":"true","colorboxOpacity":"0.85","colorboxTransition":"elastic","colorboxSpeed":"350","colorboxSlideshowSpeed":"2500","colorboxClose":"close","colorboxNext":"next","colorboxPrevious":"previous","colorboxSlideshowStart":"start slideshow","colorboxSlideshowStop":"stop slideshow","colorboxCurrent":"{current} of {total} images","colorboxXhrError":"This content failed to load.","colorboxImgError":"This image failed to load.","colorboxImageMaxWidth":"false","colorboxImageMaxHeight":"false","colorboxImageHeight":"false","colorboxImageWidth":"false","colorboxLinkHeight":"false","colorboxLinkWidth":"false","colorboxInitialHeight":"100","colorboxInitialWidth":"300","autoColorboxJavaScript":"","autoHideFlash":"true","autoColorbox":"","autoColorboxGalleries":"true","addZoomOverlay":"","useGoogleJQuery":"","colorboxAddClassToLinks":""};
    /* ]]> */
    </script>
    <script id="colorbox-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/jquery-colorbox/js/jquery.colorbox-min.js" type="text/javascript"></script>
    <script id="colorbox-wrapper-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/jquery-colorbox/js/jquery-colorbox-wrapper-min.js" type="text/javascript"></script>
    <script id="jquery-ui-mouse-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/mouse.min.js" type="text/javascript"></script>
    <script id="jquery-ui-sortable-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/sortable.min.js" type="text/javascript"></script>
    <script data-no-minify="" data-noptimize="" id="mk-webfontloader-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js/plugins/wp-enqueue/min/webfontloader.js" type="text/javascript"></script>
    <script id="mk-webfontloader-js-after" type="text/javascript">
    WebFontConfig = {
    	timeout: 2000
    }

    if ( mk_typekit_id.length > 0 ) {
    	WebFontConfig.typekit = {
    		id: mk_typekit_id
    	}
    }

    if ( mk_google_fonts.length > 0 ) {
    	WebFontConfig.google = {
    		families:  mk_google_fonts
    	}
    }

    if ( (mk_google_fonts.length > 0 || mk_typekit_id.length > 0) && navigator.userAgent.indexOf("Speed Insights") == -1) {
    	WebFont.load( WebFontConfig );
    }

    </script>
    <script id="jquery-ui-datepicker-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/datepicker.min.js" type="text/javascript"></script>
    <script id="jquery-ui-datepicker-js-after" type="text/javascript">
    jQuery(document).ready(function(jQuery){jQuery.datepicker.setDefaults({"closeText":"Close","currentText":"Today","monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Previous","dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"dateFormat":"MM d, yy","firstDay":1,"isRTL":false});});
    </script>
    <script id="jquery-ui-resizable-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/resizable.min.js" type="text/javascript"></script>
    <script id="jquery-ui-draggable-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/draggable.min.js" type="text/javascript"></script>
    <script id="jquery-ui-controlgroup-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/controlgroup.min.js" type="text/javascript"></script>
    <script id="jquery-ui-checkboxradio-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/checkboxradio.min.js" type="text/javascript"></script>
    <script id="jquery-ui-button-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/button.min.js" type="text/javascript"></script>
    <script id="jquery-ui-dialog-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/dialog.min.js" type="text/javascript"></script>
    <script id="events-manager-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var EM = {"ajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php","locationajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php?action=locations_search","firstDay":"1","locale":"en","dateFormat":"mm\/dd\/yy","ui_css":"https:\/\/www.redrockcanyonlv.org\/wp-content\/plugins\/events-manager\/includes\/css\/jquery-ui.min.css","show24hours":"0","is_ssl":"1","txt_search":"Search","txt_searching":"Searching...","txt_loading":"Loading..."};
    /* ]]> */
    </script>
    <script id="events-manager-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/events-manager/includes/js/events-manager.js" type="text/javascript"></script>
    <script id="jquery-ui-selectmenu-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/selectmenu.min.js" type="text/javascript"></script>
    <script id="jquery-ui-tooltip-js" src="https://www.redrockcanyonlv.org/wp-includes/js/jquery/ui/tooltip.min.js" type="text/javascript"></script>
    <script id="moment-js" src="https://www.redrockcanyonlv.org/wp-includes/js/dist/vendor/moment.min.js" type="text/javascript"></script>
    <script id="moment-js-after" type="text/javascript">
    moment.updateLocale( 'en_US', {"months":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthsShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"weekdays":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"weekdaysShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"week":{"dow":1},"longDateFormat":{"LT":"g:i a","LTS":null,"L":null,"LL":"F j, Y","LLL":"F j, Y g:i a","LLLL":null}} );
    </script>
    <script id="wp-fullcalendar-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var WPFC = {"ajaxurl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php?action=WP_FullCalendar","firstDay":"1","wpfc_theme":"","wpfc_limit":"6","wpfc_limit_txt":"","timeFormat":"h(:mm)a","defaultView":"month","weekends":"true","header":{"left":"prev,next today","center":"title","right":"month,basicWeek,basicDay"},"wpfc_qtips":""};
    /* ]]> */
    </script>
    <script id="wp-fullcalendar-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/wp-fullcalendar/includes/js/main.js" type="text/javascript"></script>
    <link href="https://www.redrockcanyonlv.org/wp-json/" rel="https://api.w.org/"/><link href="https://www.redrockcanyonlv.org/wp-json/wp/v2/categories/7" rel="alternate" type="application/json"/><link href="https://www.redrockcanyonlv.org/xmlrpc.php?rsd" rel="EditURI" title="RSD" type="application/rsd+xml"/>
    <link href="https://www.redrockcanyonlv.org/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
    <style type="text/css">
    	 .wp-pagenavi
    	{
    		font-size:12px !important;
    	}
    	</style>
    <link href="/wp-content/uploads/fbrfg/apple-touch-icon.png" rel="apple-touch-icon" sizes="152x152"/>
    <link href="/wp-content/uploads/fbrfg/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
    <link href="/wp-content/uploads/fbrfg/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
    <link href="/wp-content/uploads/fbrfg/manifest.json" rel="manifest"/>
    <link color="#5bbad5" href="/wp-content/uploads/fbrfg/safari-pinned-tab.svg" rel="mask-icon"/>
    <link href="/wp-content/uploads/fbrfg/favicon.ico" rel="shortcut icon"/>
    <meta content="/wp-content/uploads/fbrfg/browserconfig.xml" name="msapplication-config"/>
    <meta content="#ffffff" name="theme-color"/><meta content="" itemprop="author"><meta content="March 21, 2020" itemprop="datePublished"><meta content="March 21, 2020" itemprop="dateModified"/><meta content="Red Rock Canyon Las Vegas" itemprop="publisher"/><script> var isTest = false; </script><meta content="Powered by WPBakery Page Builder - drag and drop page builder for WordPress." name="generator"/>
    <style type="text/css">.grecaptcha-badge {
        display: none !important;
    }</style><meta content="Jupiter Child Theme " name="generator"/><noscript><style> .wpb_animate_when_almost_visible { opacity: 1; }</style></noscript><script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-13102530-33', 'auto');
      ga('send', 'pageview');

    </script>
    </meta></meta></meta></head>
    <body class="archive paged category category-hikes-trails category-7 paged-2 category-paged-2 wpb-js-composer js-comp-ver-6.7.0 vc_responsive" data-adminbar="" data-rsssl="1" itemscope="itemscope" itemtype="https://schema.org/WebPage">
    <!-- Target for scroll anchors to achieve native browser bahaviour + possible enhancements like smooth scrolling -->
    <div id="top-of-page"></div>
    <div id="mk-boxed-layout">
    <div id="mk-theme-container">
    <header class="mk-header header-style-1 header-align-left toolbar-true menu-hover-2 sticky-style-slide mk-background-stretch full-header" data-header-style="1" data-height="100" data-responsive-height="100" data-sticky-height="55" data-sticky-offset="header" data-sticky-style="slide" data-transparent-skin="" id="mk-header-1" itemscope="itemscope" itemtype="https://schema.org/WPHeader" role="banner">
    <div class="mk-header-holder">
    <div class="mk-header-toolbar">
    <div class="mk-header-toolbar-holder">
    <span class="mk-header-tagline"><a class="button" href="https://goo.gl/maps/X8LKj9bXcMT2" target="_blank">Driving Directions</a> <a class="button" href="https://www.redrockcanyonlv.org/fees/">Fees &amp; Passes</a></span><div class="mk-header-social toolbar-section"><ul><li><a class="mk-simple-rounded facebook-hover" href="https://www.facebook.com/RedRockCanyonLV/" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e17aa" data-name="mk-jupiter-icon-simple-facebook" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192.191 92.743v60.485h-63.638v96.181h63.637v256.135h97.069v-256.135h84.168s6.674-51.322 9.885-96.508h-93.666v-42.921c0-8.807 11.565-20.661 23.01-20.661h71.791v-95.719h-83.57c-111.317 0-108.686 86.262-108.686 99.142z"></path></svg></a></li><li><a class="mk-simple-rounded instagram-hover" href="https://www.instagram.com/redrockcanyonlv/" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e1837" data-name="mk-jupiter-icon-simple-instagram" style=" height:16px; width: 16px; " viewbox="0 0 81.2 81.2" xmlns="http://www.w3.org/2000/svg"><path d="M81,23.9c-0.2-4.3-0.9-7.3-1.9-9.9c-1-2.7-2.4-4.9-4.7-7.2c-2.3-2.3-4.5-3.6-7.2-4.7c-2.6-1-5.5-1.7-9.9-1.9 C53,0,51.6,0,40.6,0c-11,0-12.4,0-16.7,0.2c-4.3,0.2-7.3,0.9-9.9,1.9c-2.7,1-4.9,2.4-7.2,4.7C4.6,9.1,3.2,11.3,2.1,14 c-1,2.6-1.7,5.5-1.9,9.9C0,28.2,0,29.6,0,40.6c0,11,0,12.4,0.2,16.7c0.2,4.3,0.9,7.3,1.9,9.9c1,2.7,2.4,4.9,4.7,7.2 c2.3,2.3,4.5,3.6,7.2,4.7c2.6,1,5.5,1.7,9.9,1.9c4.3,0.2,5.7,0.2,16.7,0.2c11,0,12.4,0,16.7-0.2c4.3-0.2,7.3-0.9,9.9-1.9 c2.7-1,4.9-2.4,7.2-4.7c2.3-2.3,3.6-4.5,4.7-7.2c1-2.6,1.7-5.5,1.9-9.9c0.2-4.3,0.2-5.7,0.2-16.7C81.2,29.6,81.2,28.2,81,23.9z  M73.6,57c-0.2,4-0.8,6.1-1.4,7.5c-0.7,1.9-1.6,3.2-3,4.7c-1.4,1.4-2.8,2.3-4.7,3c-1.4,0.6-3.6,1.2-7.5,1.4 c-4.3,0.2-5.6,0.2-16.4,0.2c-10.8,0-12.1,0-16.4-0.2c-4-0.2-6.1-0.8-7.5-1.4c-1.9-0.7-3.2-1.6-4.7-3c-1.4-1.4-2.3-2.8-3-4.7 C8.4,63.1,7.7,61,7.6,57c-0.2-4.3-0.2-5.6-0.2-16.4c0-10.8,0-12.1,0.2-16.4c0.2-4,0.8-6.1,1.4-7.5c0.7-1.9,1.6-3.2,3-4.7 c1.4-1.4,2.8-2.3,4.7-3c1.4-0.6,3.6-1.2,7.5-1.4c4.3-0.2,5.6-0.2,16.4-0.2c10.8,0,12.1,0,16.4,0.2c4,0.2,6.1,0.8,7.5,1.4 c1.9,0.7,3.2,1.6,4.7,3c1.4,1.4,2.3,2.8,3,4.7c0.6,1.4,1.2,3.6,1.4,7.5c0.2,4.3,0.2,5.6,0.2,16.4C73.9,51.4,73.8,52.7,73.6,57z"></path><path d="M40.6,19.8c-11.5,0-20.8,9.3-20.8,20.8c0,11.5,9.3,20.8,20.8,20.8c11.5,0,20.8-9.3,20.8-20.8 C61.4,29.1,52.1,19.8,40.6,19.8z M40.6,54.1c-7.5,0-13.5-6.1-13.5-13.5c0-7.5,6.1-13.5,13.5-13.5c7.5,0,13.5,6.1,13.5,13.5 C54.1,48.1,48.1,54.1,40.6,54.1z"></path><circle cx="62.3" cy="18.9" r="4.9"></circle></svg></a></li><li><a class="mk-simple-rounded google-hover" href="https://goo.gl/maps/X8LKj9bXcMT2" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e188b" data-name="mk-jupiter-icon-simple-google" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M431.474-6.4h-139.076c-36.469 0-82.376 5.372-120.846 36.925-29.069 24.875-43.219 59.114-43.219 90.04 0 52.392 40.522 105.507 112.082 105.507 6.749 0 14.135-.686 21.632-1.328-3.378 8.029-6.793 14.751-6.793 26.189 0 20.838 10.801 33.575 20.253 45.692-30.35 2.007-87.08 5.358-128.964 30.86-39.833 23.57-52.019 57.808-52.019 81.997 0 49.736 47.292 96.121 145.196 96.121 116.149 0 177.591-63.83 177.591-127.039 0-46.312-27.009-69.188-56.7-94.055l-24.327-18.787c-7.394-6.081-17.512-14.11-17.512-28.898 0-14.78 10.119-24.211 18.875-32.941 28.358-22.159 56.716-45.677 56.716-95.397 0-51.086-32.433-77.961-47.959-90.719h41.914l43.158-24.166zm-59.352 411.202c0 41.633-34.476 72.537-99.31 72.537-72.228 0-118.831-34.254-118.831-81.953 0-47.728 43.218-63.815 58.056-69.187 28.38-9.445 64.834-10.774 70.908-10.774 6.756 0 10.119 0 15.542.649 51.351 36.29 73.635 54.474 73.635 88.726zm-54.048-216.363c-10.815 10.737-29.07 18.795-45.945 18.795-58.048 0-84.376-74.589-84.376-119.587 0-17.481 3.378-35.597 14.838-49.72 10.808-13.445 29.706-22.182 47.27-22.182 56.049 0 85.102 75.26 85.102 123.623 0 12.116-1.378 33.59-16.889 49.072z"></path></svg></a></li><li><a class="mk-simple-rounded twitter-hover" href="https://twitter.com/RedRockCynLV" rel="noreferrer noopener" target="_blank"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e18df" data-name="mk-jupiter-icon-simple-twitter" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M454.058 213.822c28.724-2.382 48.193-15.423 55.683-33.132-10.365 6.373-42.524 13.301-60.269 6.681-.877-4.162-1.835-8.132-2.792-11.706-13.527-49.679-59.846-89.698-108.382-84.865 3.916-1.589 7.914-3.053 11.885-4.388 5.325-1.923 36.678-7.003 31.749-18.079-4.176-9.728-42.471 7.352-49.672 9.597 9.501-3.581 25.26-9.735 26.93-20.667-14.569 1.991-28.901 8.885-39.937 18.908 3.998-4.293 7.01-9.536 7.666-15.171-38.91 24.85-61.624 74.932-80.025 123.523-14.438-13.972-27.239-25.008-38.712-31.114-32.209-17.285-70.722-35.303-131.156-57.736-1.862 19.996 9.899 46.591 43.723 64.273-7.325-.986-20.736 1.219-31.462 3.773 4.382 22.912 18.627 41.805 57.251 50.918-17.642 1.163-26.767 5.182-35.036 13.841 8.043 15.923 27.656 34.709 62.931 30.82-39.225 16.935-15.998 48.234 15.93 43.565-54.444 56.244-140.294 52.123-189.596 5.08 128.712 175.385 408.493 103.724 450.21-65.225 31.23.261 49.605-10.823 60.994-23.05-17.99 3.053-44.072-.095-57.914-5.846z"></path></svg></a></li></ul><div class="clearboth"></div></div>
    </div>
    </div>
    <div class="mk-header-inner add-header-height">
    <div class="mk-header-bg"></div>
    <div class="mk-toolbar-resposnive-icon"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e19bc" data-name="mk-icon-chevron-down" viewbox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1683 808l-742 741q-19 19-45 19t-45-19l-742-741q-19-19-19-45.5t19-45.5l166-165q19-19 45-19t45 19l531 531 531-531q19-19 45-19t45 19l166 165q19 19 19 45.5t-19 45.5z"></path></svg></div>
    <div class="mk-header-nav-container one-row-style menu-hover-style-2" itemscope="itemscope" itemtype="https://schema.org/SiteNavigationElement" role="navigation">
    <nav class="mk-main-navigation js-main-nav"><ul class="main-navigation-ul" id="menu-main-menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home no-mega-menu" id="menu-item-9249"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e6536" data-name="mk-moon-home-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 304l-96-96v-144h-64v80l-96-96-256 256v16h64v160h160v-96h64v96h160v-160h64z"></path></svg>Home</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-ancestor current-menu-parent menu-item-has-children no-mega-menu" id="menu-item-472"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/redrockcanyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e6634" data-name="mk-icon-map-marker" style=" height:16px; width: 9.1428571428571px; " viewbox="0 0 1024 1792" xmlns="http://www.w3.org/2000/svg"><path d="M768 640q0-106-75-181t-181-75-181 75-75 181 75 181 181 75 181-75 75-181zm256 0q0 109-33 179l-364 774q-16 33-47.5 52t-67.5 19-67.5-19-46.5-52l-365-774q-33-70-33-179 0-212 150-362t362-150 362 150 150 362z"></path></svg>Plan A Visit</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-9251"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/fees/">Fees &amp; Passes</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-511"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/visitor-information/">Visitor Information</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item" id="menu-item-930"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/">Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-382"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/geology-highlights/">Geology Highlights</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-396"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/weather/">Weather Information</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item no-mega-menu" id="menu-item-862"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e68e9" data-name="mk-moon-direction" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M400 192l96-64-96-64h-112v-40c0-13.2-10.8-24-24-24h-16c-13.2 0-24 10.8-24 24v40h-160v128h160v32h-144l-64 48 64 48h144v192h64v-192h128v-96h-128v-32h112z"></path></svg>Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children no-mega-menu" id="menu-item-7306"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/events/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e69fe" data-name="mk-icon-calendar" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M128 1664h288v-288h-288v288zm352 0h320v-288h-320v288zm-352-352h288v-320h-288v320zm352 0h320v-320h-320v320zm-352-384h288v-288h-288v288zm736 736h320v-288h-320v288zm-384-736h320v-288h-320v288zm768 736h288v-288h-288v288zm-384-352h320v-320h-320v320zm-352-864v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm736 864h288v-320h-288v320zm-384-384h320v-288h-320v288zm384 0h288v-288h-288v288zm32-480v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm384-64v1280q0 52-38 90t-90 38h-1408q-52 0-90-38t-38-90v-1280q0-52 38-90t90-38h128v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h384v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h128q52 0 90 38t38 90z"></path></svg>Events</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-7311"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/event-calendar/">Event Calendar</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-7304"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/upcoming-events/">Upcoming Events List</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children no-mega-menu" id="menu-item-9453"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/programs/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e6bed" data-name="mk-moon-map-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M0 96l160-64v384l-160 64zm352 0v384l-160-53.333v-384zm160-64v384l-128 51.2v-384z"></path></svg>Programs</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9391"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/red-rock-canyon-a-to-z/">Red Rock Canyon A To Z</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9390"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/wildlife-wednesday/">Wildlife Wednesday</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9389"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/flower-friday/">Flower Friday</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-9417"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/jackson-the-burro/">Jackson the Red Rock Canyon Burro</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-1226"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/tortoise-habitat/">Tortoise Habitat</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="menu-item-9416"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/artist-in-residence/">Artist In Residence Program</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page no-mega-menu" id="menu-item-1184"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/shop/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e6def" data-name="mk-icon-shopping-cart" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M640 1536q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm896 0q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm128-1088v512q0 24-16 42.5t-41 21.5l-1044 122q1 7 4.5 21.5t6 26.5 2.5 22q0 16-24 64h920q26 0 45 19t19 45-19 45-45 19h-1024q-26 0-45-19t-19-45q0-14 11-39.5t29.5-59.5 20.5-38l-177-823h-204q-26 0-45-19t-19-45 19-45 45-19h256q16 0 28.5 6.5t20 15.5 13 24.5 7.5 26.5 5.5 29.5 4.5 25.5h1201q26 0 45 19t19 45z"></path></svg>Shop</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children no-mega-menu" id="menu-item-5076"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e6fa2" data-name="mk-moon-users" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M367.497 402.687c-9.476-1.494-9.692-27.327-9.692-27.327s27.844-27.328 33.912-64.076c16.326 0 26.407-39.069 10.082-52.814.681-14.47 20.984-113.588-81.799-113.588-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.816-144.503 54.658-144.503 109.313h384c0-54.655-113.979-104.497-144.503-109.313zm-195.47 8.718c22.047-13.575 48.813-26.154 70.769-33.712-7.876-11.216-16.647-26.468-22.165-44.531-7.703-6.283-13.972-15.266-17.999-26.301-4.033-11.052-5.561-23.426-4.304-34.842.902-8.196 3.239-15.833 6.825-22.544-2.175-23.293-3.707-69.017 26.224-102.366 11.607-12.933 26.278-22.23 43.85-27.843-3.137-32.38-19.58-70.385-83.227-70.385-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.817-144.503 54.659-144.503 109.314h164.798c2.355-1.537 4.753-3.07 7.229-4.595z"></path></svg>About</a>
    <ul class="sub-menu" style="">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-89"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/contact-us/">Contact Us</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="menu-item-9279"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/news/">News</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-5079"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/">Our Mission</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-5078"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/opportunities/">Opportunities</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="menu-item-1114"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/frequently-asked-questions/">FAQ</a></li>
    </ul>
    </li>
    </ul></nav>
    <div class="main-nav-side-search">
    <a class="mk-search-trigger add-header-height mk-fullscreen-trigger" href="#"><i class="mk-svg-icon-wrapper"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e7271" data-name="mk-icon-search" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1152 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></i></a>
    </div>
    </div>
    <div class="mk-nav-responsive-link">
    <div class="mk-css-icon-menu">
    <div class="mk-css-icon-menu-line-1"></div>
    <div class="mk-css-icon-menu-line-2"></div>
    <div class="mk-css-icon-menu-line-3"></div>
    </div>
    </div> <div class="header-logo fit-logo-img add-header-height logo-is-responsive logo-has-sticky">
    <a href="https://www.redrockcanyonlv.org/" title="Red Rock Canyon Las Vegas">
    <img alt="" class="mk-desktop-logo dark-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    <img alt="" class="mk-desktop-logo light-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    <img alt="" class="mk-resposnive-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    <img alt="" class="mk-sticky-logo" src="https://www.redrockcanyonlv.org/wp-content/uploads/red-rock-canyon-las-vegas.png" title=""/>
    </a>
    </div>
    <div class="mk-header-right">
    </div>
    </div>
    <div class="mk-responsive-wrap">
    <nav class="menu-main-menu-container"><ul class="mk-responsive-nav" id="menu-main-menu-1"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home" id="responsive-menu-item-9249"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e8861" data-name="mk-moon-home-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 304l-96-96v-144h-64v80l-96-96-256 256v16h64v160h160v-96h64v96h160v-160h64z"></path></svg>Home</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-ancestor current-menu-parent menu-item-has-children" id="responsive-menu-item-472"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/redrockcanyon/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e8972" data-name="mk-icon-map-marker" style=" height:16px; width: 9.1428571428571px; " viewbox="0 0 1024 1792" xmlns="http://www.w3.org/2000/svg"><path d="M768 640q0-106-75-181t-181-75-181 75-75 181 75 181 181 75 181-75 75-181zm256 0q0 109-33 179l-364 774q-16 33-47.5 52t-67.5 19-67.5-19-46.5-52l-365-774q-33-70-33-179 0-212 150-362t362-150 362 150 150 362z"></path></svg>Plan A Visit</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e8ac3" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-9251"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/fees/">Fees &amp; Passes</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-511"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/visitor-information/">Visitor Information</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item" id="responsive-menu-item-930"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/">Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-382"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/geology-highlights/">Geology Highlights</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-396"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/weather/">Weather Information</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item" id="responsive-menu-item-862"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e8da3" data-name="mk-moon-direction" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M400 192l96-64-96-64h-112v-40c0-13.2-10.8-24-24-24h-16c-13.2 0-24 10.8-24 24v40h-160v128h160v32h-144l-64 48 64 48h144v192h64v-192h128v-96h-128v-32h112z"></path></svg>Hikes &amp; Trails</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children" id="responsive-menu-item-7306"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/events/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e8ea1" data-name="mk-icon-calendar" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M128 1664h288v-288h-288v288zm352 0h320v-288h-320v288zm-352-352h288v-320h-288v320zm352 0h320v-320h-320v320zm-352-384h288v-288h-288v288zm736 736h320v-288h-320v288zm-384-736h320v-288h-320v288zm768 736h288v-288h-288v288zm-384-352h320v-320h-320v320zm-352-864v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm736 864h288v-320h-288v320zm-384-384h320v-288h-320v288zm384 0h288v-288h-288v288zm32-480v-288q0-13-9.5-22.5t-22.5-9.5h-64q-13 0-22.5 9.5t-9.5 22.5v288q0 13 9.5 22.5t22.5 9.5h64q13 0 22.5-9.5t9.5-22.5zm384-64v1280q0 52-38 90t-90 38h-1408q-52 0-90-38t-38-90v-1280q0-52 38-90t90-38h128v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h384v-96q0-66 47-113t113-47h64q66 0 113 47t47 113v96h128q52 0 90 38t38 90z"></path></svg>Events</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e8fe7" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-7311"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/event-calendar/">Event Calendar</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-7304"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/upcoming-events/">Upcoming Events List</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children" id="responsive-menu-item-9453"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/programs/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e91bd" data-name="mk-moon-map-3" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M0 96l160-64v384l-160 64zm352 0v384l-160-53.333v-384zm160-64v384l-128 51.2v-384z"></path></svg>Programs</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e9312" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9391"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/red-rock-canyon-a-to-z/">Red Rock Canyon A To Z</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9390"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/wildlife-wednesday/">Wildlife Wednesday</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9389"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/flower-friday/">Flower Friday</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-9417"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/jackson-the-burro/">Jackson the Red Rock Canyon Burro</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-1226"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/tortoise-habitat/">Tortoise Habitat</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post" id="responsive-menu-item-9416"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/artist-in-residence/">Artist In Residence Program</a></li>
    </ul>
    </li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-1184"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/shop/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e9615" data-name="mk-icon-shopping-cart" style=" height:16px; width: 14.857142857143px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M640 1536q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm896 0q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm128-1088v512q0 24-16 42.5t-41 21.5l-1044 122q1 7 4.5 21.5t6 26.5 2.5 22q0 16-24 64h920q26 0 45 19t19 45-19 45-45 19h-1024q-26 0-45-19t-19-45q0-14 11-39.5t29.5-59.5 20.5-38l-177-823h-204q-26 0-45-19t-19-45 19-45 45-19h256q16 0 28.5 6.5t20 15.5 13 24.5 7.5 26.5 5.5 29.5 4.5 25.5h1201q26 0 45 19t19 45z"></path></svg>Shop</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children" id="responsive-menu-item-5076"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e9792" data-name="mk-moon-users" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M367.497 402.687c-9.476-1.494-9.692-27.327-9.692-27.327s27.844-27.328 33.912-64.076c16.326 0 26.407-39.069 10.082-52.814.681-14.47 20.984-113.588-81.799-113.588-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.816-144.503 54.658-144.503 109.313h384c0-54.655-113.979-104.497-144.503-109.313zm-195.47 8.718c22.047-13.575 48.813-26.154 70.769-33.712-7.876-11.216-16.647-26.468-22.165-44.531-7.703-6.283-13.972-15.266-17.999-26.301-4.033-11.052-5.561-23.426-4.304-34.842.902-8.196 3.239-15.833 6.825-22.544-2.175-23.293-3.707-69.017 26.224-102.366 11.607-12.933 26.278-22.23 43.85-27.843-3.137-32.38-19.58-70.385-83.227-70.385-102.782 0-82.479 99.118-81.799 113.588-16.327 13.745-6.244 52.814 10.081 52.814 6.067 36.748 33.913 64.076 33.913 64.076s-.216 25.833-9.692 27.327c-30.524 4.817-144.503 54.659-144.503 109.314h164.798c2.355-1.537 4.753-3.07 7.229-4.595z"></path></svg>About</a><span class="mk-nav-arrow mk-nav-sub-closed"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e98c4" data-name="mk-moon-arrow-down" style=" height:16px; width: 16px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M512 192l-96-96-160 160-160-160-96 96 256 255.999z"></path></svg></span>
    <ul class="sub-menu">
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-89"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/contact-us/">Contact Us</a></li>
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category" id="responsive-menu-item-9279"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/lasvegas/news/">News</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-5079"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/our-mission/">Our Mission</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-5078"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/opportunities/">Opportunities</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page" id="responsive-menu-item-1114"><a class="menu-item-link js-smooth-scroll" href="https://www.redrockcanyonlv.org/frequently-asked-questions/">FAQ</a></li>
    </ul>
    </li>
    </ul></nav>
    <form action="https://www.redrockcanyonlv.org/" class="responsive-searchform" method="get">
    <input class="text-input" id="s" name="s" placeholder="Search.." type="text" value=""/>
    <i><input type="submit" value=""/><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7e9bfc" data-name="mk-icon-search" viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1152 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></i>
    </form>
    </div>
    </div>
    <div class="mk-header-padding-wrapper"></div>
    <section class="intro-left" id="mk-page-introduce"><div class="mk-grid"><h1 class="page-title mk-drop-shadow">Hikes &amp; Trails – Round-Trip Distances &amp; Times</h1><div class="page-subtitle">Hikes are numbered according to their location on the trail map. Georeferenced maps are also included with each trail and can be used with any georeferenced map mobile application.
    </div><div id="mk-breadcrumbs"><div class="mk-breadcrumbs-inner dark-skin"><span xmlns:v="http://rdf.data-vocabulary.org/#"><span typeof="v:Breadcrumb"><a href="https://www.redrockcanyonlv.org/" property="v:title" rel="v:url">Home</a> / <span rel="v:child" typeof="v:Breadcrumb"><span class="breadcrumb-categoris-holder"><a href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/">Hikes &amp; Trails - Round-Trip Distances &amp; Times</a> <span>/</span> </span> (Page 2)</span></span></span></div></div><div class="clearboth"></div></div></section>
    </header>
    <div class="master-holder clearfix" id="theme-page" itemprop="mainContentOfPage" role="main">
    <div class="master-holder-bg-holder">
    <div class="master-holder-bg js-el" id="theme-page-bg"></div>
    </div>
    <div class="mk-main-wrapper-holder">
    <div class="theme-page-wrapper mk-main-wrapper mk-grid right-layout">
    <div class="theme-content" itemprop="mainContentOfPage">
    <section "item":".mk-isotop-item"}"="" class="js-loop js-el clearfix mk-blog-container mk-newspaper-wrapper mag-one-column mk-blog-container-lazyload js-loop--loaded" container":"#loop-2",="" data-grid-config="{" data-loop-iterator="10" data-loop-posts="" data-max-pages="1" data-mk-component="Grid" data-pagination-style="1" id="loop-2" itemscope="itemscope" itemtype="https://schema.org/Blog">
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-12840 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-12840">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/genes-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-12840 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-300x300.jpg 300w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-768x768.jpg 768w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-1024x1024.jpg 1024w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2842-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/genes-trail/" rel="bookmark">Gene’s Trail</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/genes-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7eb2c5" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">N/A</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-12851 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-12851">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/calico-overlook/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-12851 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/img_2828-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/img_2828-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2828-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2828-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2828-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/calico-overlook/" rel="bookmark">Calico Overlook</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/calico-overlook/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7eb815" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">N/A</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-12854 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-12854">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/calico-basin-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-12854 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/img_2789-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/img_2789-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2789-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2789-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2789-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/calico-basin-trail/" rel="bookmark">Calico Basin Trail</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/calico-basin-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7ebcc6" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">N/A</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-12857 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-12857">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/girl-scout-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-12857 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/img_2814-500x500.jpg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/img_2814-500x500.jpg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2814-1000x1000.jpg 1000w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2814-266x266.jpg 266w, https://www.redrockcanyonlv.org/wp-content/uploads/img_2814-195x195.jpg 195w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/girl-scout-trail/" rel="bookmark">Girl Scout Trail</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/girl-scout-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7ec1cd" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">N/A</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    <article class="mk-blog-newspaper-item image-post-type mk-isotop-item three-column mk-blog-newspaper-item--loaded post-12860 post type-post status-publish format-standard has-post-thumbnail hentry category-hikes-trails" id="post-12860">
    <div class="featured-image">
    <a href="https://www.redrockcanyonlv.org/ash-spring-trail/">
    <img alt="" class="attachment-500x500 size-500x500 colorbox-12860 wp-post-image" height="500" itemprop="image" loading="lazy" sizes="(max-width: 500px) 100vw, 500px" src="https://www.redrockcanyonlv.org/wp-content/uploads/ash-spring-8004599-500x500.jpeg" srcset="https://www.redrockcanyonlv.org/wp-content/uploads/ash-spring-8004599-500x500.jpeg 500w, https://www.redrockcanyonlv.org/wp-content/uploads/ash-spring-8004599-266x266.jpeg 266w" width="500"/> </a>
    </div><!-- .post-thumbnail -->
    <div class="mk-blog-meta">
    <h2 class="the-title"><a href="https://www.redrockcanyonlv.org/ash-spring-trail/" rel="bookmark">Ash Spring Trail</a></h2> </div>
    <div class="newspaper-item-footer"><div class="newspaper-item-footer-holder"><a class="mk-readmore" href="https://www.redrockcanyonlv.org/ash-spring-trail/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a7ec6b8" data-name="mk-moon-arrow-right-2" style=" height:8px; width: 8px; " viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M192 0l-96 96 160 160-160 160 96 96 256-256z"></path></svg>Read More</a> <span class="trailnum">N/A</span>
    <div class="clearboth"></div></div> </div></article><!-- #post-## -->
    </section><div class="wp-pagenavi" role="navigation">
    <span class="pages">Page 2 of 2</span><a aria-label="Previous Page" class="previouspostslink" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/" rel="prev">«</a><a class="page smaller" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/" title="Page 1">1</a><span aria-current="page" class="current">2</span>
    </div> <div class="clearboth"></div>
    </div>
    <aside class="mk-builtin" id="mk-sidebar" itemscope="itemscope" itemtype="https://schema.org/WPSideBar" role="complementary">
    <div class="sidebar-wrapper">
    <section class="widget widget_text" id="text-21"><div class="widgettitle">Upcoming Events</div> <div class="textwidget"><div class="em-calendar-wrapper" id="em-calendar-166"><table class="em-calendar">
    <thead>
    <tr>
    <td><a class="em-calnav em-calnav-prev" href="/lasvegas/hikes-trails/page/2/?ajaxCalendar=1&amp;mo=1&amp;yr=2022" rel="nofollow">&lt;&lt;</a></td>
    <td class="month_name" colspan="5">Feb 2022</td>
    <td><a class="em-calnav em-calnav-next" href="/lasvegas/hikes-trails/page/2/?ajaxCalendar=1&amp;mo=3&amp;yr=2022" rel="nofollow">&gt;&gt;</a></td>
    </tr>
    </thead>
    <tbody>
    <tr class="days-names">
    <td>M</td><td>T</td><td>W</td><td>T</td><td>F</td><td>S</td><td>S</td>
    </tr>
    <tr>
    <td class="eventless-pre">
    										31									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/trail-talk-tuesday-pine-creek-8am-2-1-22/" title="Trail Talk Tuesday – Pine Creek">1</a>
    </td>
    <td class="eventless">
    										2									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-3-22/" title="Moenkopi Mornings Guided Hike">3</a>
    </td>
    <td class="eventless">
    										4									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-5-22/" title="Geology Tabletop at Calico I">5</a>
    </td>
    <td class="eventless">
    										6									</td>
    </tr><tr> <td class="eventless">
    										7									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/tabletop-tuesday-mountain-lion-9am-2-8-22/" title="Tabletop Tuesday – Mountain Lion">8</a>
    </td>
    <td class="eventless">
    										9									</td>
    <td class="eventful-today">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-10-22/" title="Moenkopi Mornings Guided Hike">10</a>
    </td>
    <td class="eventless">
    										11									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-12-22/" title="Geology Tabletop at Calico I">12</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/healthy-heart-hike-pine-creek-2-13-22/" title="Healthy Heart Hike – Pine Creek">13</a>
    </td>
    </tr><tr> <td class="eventless">
    										14									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/tabletop-tuesday-canines-of-red-rock-canyon-nca-9am-2-15-22/" title="Tabletop Tuesday – Canines of Red Rock Canyon NCA">15</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/campground-program-gila-monsters-6pm-2-16-22/" title="Campground Program – Gila Monsters">16</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-17-22/" title="Moenkopi Mornings Guided Hike">17</a>
    </td>
    <td class="eventless">
    										18									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-19-22/" title="Geology Tabletop at Calico I">19</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/fossil-ridge-hike-2-20-22/" title="Fossil Ridge Hike">20</a>
    </td>
    </tr><tr> <td class="eventless">
    										21									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/tabletop-tuesday-eagles-9am-2-22-22/" title="Tabletop Tuesday – Eagles">22</a>
    </td>
    <td class="eventless">
    										23									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/moenkopi-mornings-guided-hike-2-24-22/" title="Moenkopi Mornings Guided Hike">24</a>
    </td>
    <td class="eventless">
    										25									</td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/geology-tabletop-at-calico-i-930am-2-26-22/" title="Geology Tabletop at Calico I">26</a>
    </td>
    <td class="eventful">
    <a href="https://www.redrockcanyonlv.org/events/healthy-heart-hike-la-madre-spring-2-27-22/" title="Healthy Heart Hike – La Madre Spring">27</a>
    </td>
    </tr><tr> <td class="eventless">
    										28									</td>
    <td class="eventful-post">
    <a href="https://www.redrockcanyonlv.org/events/trail-talk-tuesday-calico-hills-8am-3-1-22/" title="Trail Talk Tuesday – Calico Hills">1</a>
    </td>
    <td class="eventless-post">
    										2									</td>
    <td class="eventless-post">
    										3									</td>
    <td class="eventless-post">
    										4									</td>
    <td class="eventless-post">
    										5									</td>
    <td class="eventful-post">
    <a href="https://www.redrockcanyonlv.org/events/nature-walks-red-spring-7am-3-6-22/" title="Nature Walks – Red Spring">6</a>
    </td>
    </tr>
    </tbody>
    </table></div>
    <a class="button" href="https://www.redrockcanyonlv.org/event-calendar/">View Full Calendar</a></div>
    </section> </div>
    </aside>
    <div class="clearboth"></div>
    </div>
    </div>
    </div>
    <section id="mk-footer-unfold-spacer"></section>
    <section class="" id="mk-footer" itemscope="itemscope" itemtype="https://schema.org/WPFooter" role="contentinfo">
    <div class="footer-wrapper fullwidth-footer">
    <div class="mk-padding-wrapper">
    <div class="mk-col-1-4"><section class="widget widget_text" id="text-26"><div class="widgettitle">Who We Are</div> <div class="textwidget"><p><a href="https://www.redrockcanyonlv.org/our-mission/">Southern Nevada Conservancy</a>, a 501c3 nonprofit organization based in Las Vegas, NV, serves Red Rock Canyon National Conservation Area under a formal agreement with the Bureau of Land Management (BLM) in many ways, including interpretive programming, fee-station management, retail operations, and this website.</p>
    <p><a class="button" href="https://www.redrockcanyonlv.org/redrockcanyon/fees/">Fees &amp; Passes</a></p>
    </div>
    </section></div>
    <div class="mk-col-1-4"><section class="widget widget_nav_menu" id="nav_menu-2"><div class="widgettitle">Visit Red Rock Canyon</div>
    <div class="menu-footer-menu-container"><ul class="menu" id="menu-footer-menu">
    <li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item menu-item-9245" id="menu-item-9245"><a aria-current="page" href="https://www.redrockcanyonlv.org/lasvegas/hikes-trails/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a8016b0" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Hikes &amp; Trails – Round-Trip Distances &amp; Times</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post menu-item-9247" id="menu-item-9247"><a href="https://www.redrockcanyonlv.org/fees/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a8016b0" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Fees &amp; Passes</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-post menu-item-9437" id="menu-item-9437"><a href="https://www.redrockcanyonlv.org/visitor-information/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a8016b0" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Visitor Information</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9246" id="menu-item-9246"><a href="https://www.redrockcanyonlv.org/shop/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a8016b0" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Shop</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9242" id="menu-item-9242"><a href="https://www.redrockcanyonlv.org/event-calendar/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a8016b0" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>Event Calendar</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1339" id="menu-item-1339"><a href="https://www.redrockcanyonlv.org/frequently-asked-questions/"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a8016b0" data-name="mk-icon-angle-right" style=" height:14px; width: 5px; " viewbox="0 0 640 1792" xmlns="http://www.w3.org/2000/svg"><path d="M595 960q0 13-10 23l-466 466q-10 10-23 10t-23-10l-50-50q-10-10-10-23t10-23l393-393-393-393q-10-10-10-23t10-23l50-50q10-10 23-10t23 10l466 466q10 10 10 23z"></path></svg>FAQ</a></li>
    </ul></div></section></div>
    <div class="mk-col-1-4"><section class="widget widget_text" id="text-24"><div class="widgettitle">Operating Hours</div> <div class="textwidget"><p><a href="https://www.redrockcanyonlv.org/red-rock-canyon-is-hot-hot-hot/" rel="noopener" target="_blank"><strong>PLEASE VISIT THIS PAGE FOR CURRENT OPERATING HOURS &amp; FACILITIES.</strong></a></p>
    <p>The Visitor Center is open daily from 9<strong>:00 AM – 4:30 pm</strong>.</p>
    <p>The Scenic Drive is open every day of the year with hours changing slightly according to the season:</p>
    <p><strong>Nov – Feb</strong> – 6:00 AM to 5:00 PM<br/>
    <strong>March</strong> – 6:00 AM to 7:00 PM<br/>
    <strong>Apr – Sep</strong> – 6:00 AM to 8:00 PM<br/>
    <strong>Oct</strong> – 6:00 AM to 7:00 PM</p>
    </div>
    </section></div>
    <div class="mk-col-1-4"><section class="widget widget_text" id="text-25"><div class="widgettitle">Get In Touch</div> <div class="textwidget"><p><strong>Red Rock Canyon</strong><br/>
    <strong>General Information &amp; Questions</strong><br/>
    Phone: <a href="tel:17025155350">+1 (702) 515-5350</a></p>
    <p><strong>Programs &amp; Guided Hikes</strong><br/>
    Phone: <a href="tel:17025155350">+1 (702) 515-5367</a></p>
    <p><strong>Elements Gift &amp; Book Store</strong><br/>
    Phone: <a href="tel:17025155379">+1 (702) 515-5379</a></p>
    <p><a class="button" href="https://goo.gl/maps/X8LKj9bXcMT2" rel="noopener" target="_blank">Driving Directions</a></p>
    </div>
    </section></div>
    <div class="clearboth"></div>
    </div>
    </div>
    <div id="sub-footer">
    <div class="fullwidth-footer">
    <span class="mk-footer-copyright">© Copyright 2017 - <a href="https://www.southernnevadaconservancy.org/" target="_blank">Southern Nevada Conservancy</a> |  All Rights Reserved.  | Website by: <a href="http://www.sitesmartmarketing.com" target="_blank">Site Smart Marketing</a></span>
    </div>
    <div class="clearboth"></div>
    </div>
    </section>
    </div>
    </div>
    <div class="bottom-corner-btns js-bottom-corner-btns">
    </div>
    <div class="mk-fullscreen-search-overlay">
    <a class="mk-fullscreen-close" href="#"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a802075" data-name="mk-moon-close-2" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M390.628 345.372l-45.256 45.256-89.372-89.373-89.373 89.372-45.255-45.255 89.373-89.372-89.372-89.373 45.254-45.254 89.373 89.372 89.372-89.373 45.256 45.255-89.373 89.373 89.373 89.372z"></path></svg></a>
    <div class="mk-fullscreen-search-wrapper">
    <p>Start typing and press Enter to search</p>
    <form action="https://www.redrockcanyonlv.org/" id="mk-fullscreen-searchform" method="get">
    <input id="mk-fullscreen-search-input" name="s" type="text" value=""/>
    <i class="fullscreen-search-icon"><svg class="mk-svg-icon" data-cacheid="icon-6205d3a80211e" data-name="mk-icon-search" style=" height:25px; width: 23.214285714286px; " viewbox="0 0 1664 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1152 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></i>
    </form>
    </div>
    </div>
    <style type="text/css"></style><script type="text/javascript">
        php = {
            hasAdminbar: false,
            json: (null != null) ? null : "",
            jsPath: 'https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js'
          };
        </script><script id="google-invisible-recaptcha-js-before" type="text/javascript">
    var renderInvisibleReCaptcha = function() {

        for (var i = 0; i < document.forms.length; ++i) {
            var form = document.forms[i];
            var holder = form.querySelector('.inv-recaptcha-holder');

            if (null === holder) continue;
    		holder.innerHTML = '';

             (function(frm){
    			var cf7SubmitElm = frm.querySelector('.wpcf7-submit');
                var holderId = grecaptcha.render(holder,{
                    'sitekey': '6Lc1tbsZAAAAAA2NJDh7vLq2eDoOGmA2jYsM6-_z', 'size': 'invisible', 'badge' : 'bottomright',
                    'callback' : function (recaptchaToken) {
    					if((null !== cf7SubmitElm) && (typeof jQuery != 'undefined')){jQuery(frm).submit();grecaptcha.reset(holderId);return;}
    					 HTMLFormElement.prototype.submit.call(frm);
                    },
                    'expired-callback' : function(){grecaptcha.reset(holderId);}
                });

    			if(null !== cf7SubmitElm && (typeof jQuery != 'undefined') ){
    				jQuery(cf7SubmitElm).off('click').on('click', function(clickEvt){
    					clickEvt.preventDefault();
    					grecaptcha.execute(holderId);
    				});
    			}
    			else
    			{
    				frm.onsubmit = function (evt){evt.preventDefault();grecaptcha.execute(holderId);};
    			}


            })(form);
        }
    };
    </script>
    <script async="" defer="" id="google-invisible-recaptcha-js" src="https://www.google.com/recaptcha/api.js?onload=renderInvisibleReCaptcha&amp;render=explicit" type="text/javascript"></script>
    <script id="smoothscroll-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js/plugins/wp-enqueue/min/smoothscroll.js" type="text/javascript"></script>
    <script id="theme-scripts-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/assets/js/min/full-scripts.6.10.0.js" type="text/javascript"></script>
    <script id="mkhb-render-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/js/mkhb-render.js" type="text/javascript"></script>
    <script id="mkhb-column-js" src="https://www.redrockcanyonlv.org/wp-content/themes/jupiter/header-builder/includes/assets/js/mkhb-column.js" type="text/javascript"></script>
    <script id="jupiter-donut-shortcodes-js-extra" type="text/javascript">
    /* <![CDATA[ */
    var jupiterDonutVars = {"themeDir":"https:\/\/www.redrockcanyonlv.org\/wp-content\/themes\/jupiter","assetsUrl":"https:\/\/www.redrockcanyonlv.org\/wp-content\/plugins\/jupiter-donut\/assets","gridWidth":"1200","ajaxUrl":"https:\/\/www.redrockcanyonlv.org\/wp-admin\/admin-ajax.php","nonce":"5dd3aa9f3e"};
    /* ]]> */
    </script>
    <script id="jupiter-donut-shortcodes-js" src="https://www.redrockcanyonlv.org/wp-content/plugins/jupiter-donut/assets/js/shortcodes-scripts.min.js" type="text/javascript"></script>
    <script id="wp-embed-js" src="https://www.redrockcanyonlv.org/wp-includes/js/wp-embed.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    		jQuery(document).ready(function () {
      equalHeight('article div.mk-blog-meta');
    	//equalHeight('article div.featured-image');

    	//jQuery(window).resize(function(){jQuery('article div.featured-image').removeAttr("style");equalHeight('article div.featured-image');});
    	jQuery(window).resize(function(){jQuery('article div.mk-blog-meta').removeAttr("style");equalHeight('article div.mk-blog-meta');});
    });
    function equalHeight(columnClass){
       var maxHeight = 0;

    jQuery(columnClass).each(function(){
       if (jQuery(this).height() > maxHeight) { maxHeight = jQuery(this).height(); }
    });
    jQuery(columnClass).height(maxHeight);
    }		</script>
    <script type="text/javascript">	window.get = {};	window.get.captcha = function(enteredCaptcha) {
                      return jQuery.get(ajaxurl, { action : "mk_validate_captcha_input", captcha: enteredCaptcha });
                  	};</script>
    </body>
    </html>
    <!--
    Performance optimized by W3 Total Cache. Learn more: https://www.boldgrid.com/w3-total-cache/

    Page Caching using disk: enhanced
    Database Caching using disk (Request-wide modification query)

    Served from: www.redrockcanyonlv.org @ 2022-02-10 19:10:32 by W3 Total Cache
    -->




```python
#Two List comprehension to create a list of "Trail Urls" from our trails_soup objects. Finds all h2 tags with the class 'the-title.
#Then uses the object created from find_all() to find all get 'href' from 'a' tags.

page1_list = [x.find("a").get('href') for x in trails_soup.find_all('h2',{'class':'the-title'})]
page2_list = [x.find("a").get('href') for x in trails_soup2.find_all('h2',{'class':'the-title'})]

#Concatanate the two lists together to make one list of Urls.

trail_urls = page1_list + page2_list
```


```python
trail_urls
```




    ['https://www.redrockcanyonlv.org/moenkopi-loop/',
     'https://www.redrockcanyonlv.org/calico-hills/',
     'https://www.redrockcanyonlv.org/calico-tanks/',
     'https://www.redrockcanyonlv.org/turtlehead-peak/',
     'https://www.redrockcanyonlv.org/keystone-thrust/',
     'https://www.redrockcanyonlv.org/white-rock-willow-springs/',
     'https://www.redrockcanyonlv.org/grand-circle-loop/',
     'https://www.redrockcanyonlv.org/white-rock-la-madre-spring-loop/',
     'https://www.redrockcanyonlv.org/willow-springs-loop/',
     'https://www.redrockcanyonlv.org/la-madre-spring/',
     'https://www.redrockcanyonlv.org/petroglyph-wall-trail/',
     'https://www.redrockcanyonlv.org/north-peak-trail/',
     'https://www.redrockcanyonlv.org/bridge-mountain-trail/',
     'https://www.redrockcanyonlv.org/lost-creek-childrens-discovery/',
     'https://www.redrockcanyonlv.org/smyc/',
     'https://www.redrockcanyonlv.org/ice-box-canyon/',
     'https://www.redrockcanyonlv.org/dales/',
     'https://www.redrockcanyonlv.org/pine-creek-canyon/',
     'https://www.redrockcanyonlv.org/fire-ecology/',
     'https://www.redrockcanyonlv.org/arnight/',
     'https://www.redrockcanyonlv.org/knoll/',
     'https://www.redrockcanyonlv.org/oak-creek-canyon/',
     'https://www.redrockcanyonlv.org/oak-creek-cutoff/',
     'https://www.redrockcanyonlv.org/south-oak-creek/',
     'https://www.redrockcanyonlv.org/first-creek-canyon/',
     'https://www.redrockcanyonlv.org/kraft-boulders/',
     'https://www.redrockcanyonlv.org/genes-trail/',
     'https://www.redrockcanyonlv.org/calico-overlook/',
     'https://www.redrockcanyonlv.org/calico-basin-trail/',
     'https://www.redrockcanyonlv.org/girl-scout-trail/',
     'https://www.redrockcanyonlv.org/ash-spring-trail/']




```python

```


```python

```


```python
#With our list of URLs we will now be scraping each trail url to scrape the neccesary information from them.
# First we create a list of html pages with list comprehension.

trail_htmls = [BeautifulSoup(requests.get(url = link ,headers = user_agent).text, 'html.parser') for link in trail_urls]

#Then we scrape each list and
```


```python

```


```python

```


```python

```


```python

```


```python
#Creating DataFrame

df = pd.DataFrame({'Name': [],
                   'Distance (miles)': [],
                   'Average Time (hours)':[],
                   'Difficulty':[],
                  })
#For loop to grab needed data from htmls created above.

for x in trail_htmls:
    #This grabs some metrics from the web pages and then turns those metrics into a list.
    scraped_metrics = x.find_all('div',{'class':'mk-single-content clearfix'})[0].find('p').text.split(';')


    #This grabs <title> of the webpage in order to get the name of the trail.
    scraped_name = x.find_all('title')[0].get_text().split('|')[0].strip()

    #This adds the trail name to the beggining of the metrics list.
    scraped_metrics.insert(0, scraped_name)



    #This adds the list of information to the dataframe as row.
    df.loc[len(df.index)] = scraped_metrics

```


```python

```


```python

```


```python

```


```python
# Cleaning data.

# Grabbing only the numeric value from distance column.
for x,y in df.iterrows():
    y[1] = y[1].split(' ')[1]
    y[1]


```


```python
#Cleaning Average Time data.

#Stripping excess information from strings and turning values into numerics.

for x,y in df.iterrows():
    y[2] = y[2].strip().split(':')[1].split('h')[0].strip()
    y[2]=y[2].split('-')[0]


#Petroglyph Wall had it's value as '30 minutes'.

df.loc[10,'Average Time (hours)'] = .5

#Ash Spring trail had it's value as '1/2'
df.loc[30,'Average Time (hours)'] = .5

```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Distance (miles)</th>
      <th>Average Time (hours)</th>
      <th>Difficulty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Moenkopi Loop</td>
      <td>2</td>
      <td>1.5</td>
      <td>Difficulty: EASY</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Calico Hills</td>
      <td>2-6</td>
      <td>1.5 – 3.5</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Calico Tanks</td>
      <td>2.2</td>
      <td>2</td>
      <td>Difficulty: MODERATE – STRENUOUS</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Turtlehead Peak</td>
      <td>4.6</td>
      <td>3.5</td>
      <td>Difficulty: STRENUOUS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Keystone Thrust</td>
      <td>2.4</td>
      <td>1.5</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>5</th>
      <td>White Rock – Willow Springs</td>
      <td>4</td>
      <td>2.5</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Grand Circle Loop</td>
      <td>11.4</td>
      <td>6</td>
      <td>Difficulty: Strenuous</td>
    </tr>
    <tr>
      <th>7</th>
      <td>White Rock Mountain Loop</td>
      <td>6.2</td>
      <td>3.5</td>
      <td>Difficulty: STRENUOUS</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Willow Spring Loop</td>
      <td>1.1</td>
      <td>1.25</td>
      <td>Difficulty: EASY</td>
    </tr>
    <tr>
      <th>9</th>
      <td>La Madre Spring</td>
      <td>3.6</td>
      <td>2</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Petroglyph Wall</td>
      <td>0.20</td>
      <td>0.5</td>
      <td>Difficulty: Easy</td>
    </tr>
    <tr>
      <th>11</th>
      <td>North Peak</td>
      <td>11.8</td>
      <td>5</td>
      <td>Difficulty: Strenuous</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Bridge Mountain</td>
      <td>15.8</td>
      <td>6</td>
      <td>Difficulty: Strenuous</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Lost Creek – Children’s Discovery</td>
      <td>0.80</td>
      <td>1</td>
      <td>Difficulty: EASY-MODERATE</td>
    </tr>
    <tr>
      <th>14</th>
      <td>SMYC</td>
      <td>2</td>
      <td>2</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Ice Box Canyon</td>
      <td>2.2</td>
      <td>2</td>
      <td>Difficulty: STRENUOUS</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Dale’s</td>
      <td>4</td>
      <td>2.5</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Pine Creek Canyon</td>
      <td>2.4</td>
      <td>2</td>
      <td>Difficulty: EASY-MODERATE</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Fire Ecology</td>
      <td>0.4</td>
      <td>1</td>
      <td>Difficulty: EASY</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Arnight</td>
      <td>2.2</td>
      <td>1.5</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Knoll</td>
      <td>3.6</td>
      <td>2.5</td>
      <td>Difficulty: MODERATE</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Oak Creek Canyon</td>
      <td>2</td>
      <td>1.5</td>
      <td>Difficulty: EASY-MODERATE</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Middle Oak Creek</td>
      <td>3</td>
      <td>3</td>
      <td>Difficulty: Moderate</td>
    </tr>
    <tr>
      <th>23</th>
      <td>South Oak Creek</td>
      <td>4.8</td>
      <td>3.5</td>
      <td>Difficulty: Moderate</td>
    </tr>
    <tr>
      <th>24</th>
      <td>First Creek Canyon</td>
      <td>4</td>
      <td>2</td>
      <td>Difficulty: EASY-MODERATE</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Kraft Mountain Loop Hike</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>Difficulty: STRENUOUS</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Gene’s Trail</td>
      <td>2.6</td>
      <td>1.5</td>
      <td>Difficulty: Moderate</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Calico Overlook</td>
      <td>1.5</td>
      <td>1</td>
      <td>Difficulty: Easy to Moderate</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Calico Basin Trail</td>
      <td>1.5</td>
      <td>1</td>
      <td>Difficulty: Easy</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Girl Scout Trail</td>
      <td>1.3</td>
      <td>1</td>
      <td>Difficulty: Easy</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ash Spring Trail</td>
      <td>1</td>
      <td>0.5</td>
      <td>Difficulty: Easy</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Difficulty'].unique()
```




    array([' Difficulty: EASY', '\xa0Difficulty: MODERATE',
           '\xa0Difficulty: MODERATE – STRENUOUS\xa0',
           '\xa0Difficulty: STRENUOUS', ' Difficulty: MODERATE',
           ' Difficulty: Strenuous', ' Difficulty:\xa0STRENUOUS',
           ' Difficulty: Easy', ' Difficulty: EASY-MODERATE',
           '\xa0Difficulty: EASY-MODERATE', '\xa0Difficulty: EASY',
           ' Difficulty: Moderate', ' Difficulty: STRENUOUS',
           ' Difficulty: Easy to Moderate'], dtype=object)




```python
for x,y in df.iterrows():
    y[3]=y[3].split(':')[1].strip().lower()
```


```python
df['Difficulty'].unique()
```




    array(['easy', 'moderate', 'moderate – strenuous', 'strenuous',
           'easy-moderate', 'easy to moderate'], dtype=object)




```python
for x,y in df.iterrows():   

    if df.loc[x,'Difficulty'] == 'easy':
        df.loc[x,'Difficulty'] = 1
    elif df.loc[x,'Difficulty'] == 'easy-moderate':
        df.loc[x,'Difficulty'] = 1.5
    elif df.loc[x,'Difficulty'] == 'easy to moderate':
        df.loc[x,'Difficulty'] = 1.5
    elif df.loc[x,'Difficulty'] == 'moderate':
        df.loc[x,'Difficulty'] = 2
    elif df.loc[x,'Difficulty'] == 'moderate - strenuous':
        df.loc[x,'Difficulty'] = 2.5
    elif df.loc[x,'Difficulty'] == 'strenuous':
        df.loc[x,'Difficulty'] = 3

df.loc[2,'Difficulty'] = 2.5
```


```python
#Calico hills had it's value as '1.5 – 3.5'. According to it's description on the website, this is because
#There are two differen't "vesions" of the trial. It's Distance is also set to '2-6'. However it is only given
#One difficulty rating. Based on the the fact that I'm trying to find the correleation between distance,
# average time and Difficult, it kind of making it a guessing game which of these pairs, average time 1.5 and
# distance 2, or average time 3.5 and distance 6, are considered to be moderate. After some thought I decided
# to simply remove the row rather than choosing to guess. We already have a small amount of total rows, however
# one small lie means a lot more to a small set of data than it would mean to large set of data.

df.drop(1, inplace = True)
```


```python
#Lastly we make sure all of our string values are turned to numerics.


df['Average Time (hours)'] = pd.to_numeric(df['Average Time (hours)'])
df['Distance (miles)'] = pd.to_numeric(df['Distance (miles)'])
df['Difficulty'] = pd.to_numeric(df['Difficulty'])

```


```python

```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 30 entries, 0 to 30
    Data columns (total 4 columns):
     #   Column                Non-Null Count  Dtype  
    ---  ------                --------------  -----  
     0   Name                  30 non-null     object
     1   Distance (miles)      30 non-null     float64
     2   Average Time (hours)  30 non-null     float64
     3   Difficulty            30 non-null     float64
    dtypes: float64(3), object(1)
    memory usage: 1.2+ KB



```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Distance (miles)</th>
      <th>Average Time (hours)</th>
      <th>Difficulty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>30.000000</td>
      <td>30.000000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.603333</td>
      <td>2.241667</td>
      <td>1.933333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.529040</td>
      <td>1.430100</td>
      <td>0.727932</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.200000</td>
      <td>0.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.625000</td>
      <td>1.312500</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.400000</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.000000</td>
      <td>2.500000</td>
      <td>2.375000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>15.800000</td>
      <td>6.000000</td>
      <td>3.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Distance (miles)</th>
      <th>Average Time (hours)</th>
      <th>Difficulty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Distance (miles)</th>
      <td>1.000000</td>
      <td>0.944939</td>
      <td>0.683999</td>
    </tr>
    <tr>
      <th>Average Time (hours)</th>
      <td>0.944939</td>
      <td>1.000000</td>
      <td>0.777865</td>
    </tr>
    <tr>
      <th>Difficulty</th>
      <td>0.683999</td>
      <td>0.777865</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
px.histogram(df, x = "Distance (miles)",color_discrete_sequence=['indianred'], template = "plotly_dark" )
```


<div>                            <div id="66455b9b-5ad8-4cc6-8b06-e20a6ebad0c9" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("66455b9b-5ad8-4cc6-8b06-e20a6ebad0c9")) {                    Plotly.newPlot(                        "66455b9b-5ad8-4cc6-8b06-e20a6ebad0c9",                        [{"alignmentgroup":"True","bingroup":"x","hovertemplate":"Distance (miles)=%{x}<br>count=%{y}<extra></extra>","legendgroup":"","marker":{"color":"indianred","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"type":"histogram","x":[2.0,2.2,4.6,2.4,4.0,11.4,6.2,1.1,3.6,0.2,11.8,15.8,0.8,2.0,2.2,4.0,2.4,0.4,2.2,3.6,2.0,3.0,4.8,4.0,3.5,2.6,1.5,1.5,1.3,1.0],"xaxis":"x","yaxis":"y"}],                        {"barmode":"relative","legend":{"tracegroupgap":0},"margin":{"t":60},"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Distance (miles)"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"count"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('66455b9b-5ad8-4cc6-8b06-e20a6ebad0c9');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
px.histogram(df, x = "Average Time (hours)", color_discrete_sequence=['indianred'], template = "plotly_dark")
```


<div>                            <div id="839ef6ff-ebfa-4a84-88c1-52273387d54d" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("839ef6ff-ebfa-4a84-88c1-52273387d54d")) {                    Plotly.newPlot(                        "839ef6ff-ebfa-4a84-88c1-52273387d54d",                        [{"alignmentgroup":"True","bingroup":"x","hovertemplate":"Average Time (hours)=%{x}<br>count=%{y}<extra></extra>","legendgroup":"","marker":{"color":"indianred","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"type":"histogram","x":[1.5,2.0,3.5,1.5,2.5,6.0,3.5,1.25,2.0,0.5,5.0,6.0,1.0,2.0,2.0,2.5,2.0,1.0,1.5,2.5,1.5,3.0,3.5,2.0,2.5,1.5,1.0,1.0,1.0,0.5],"xaxis":"x","yaxis":"y"}],                        {"barmode":"relative","legend":{"tracegroupgap":0},"margin":{"t":60},"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Average Time (hours)"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"count"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('839ef6ff-ebfa-4a84-88c1-52273387d54d');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
px.histogram(df , x = "Difficulty", color_discrete_sequence=['indianred'], template = "plotly_dark")
```


<div>                            <div id="470c7b33-5dd9-41f8-ad5e-970a46f5b39b" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("470c7b33-5dd9-41f8-ad5e-970a46f5b39b")) {                    Plotly.newPlot(                        "470c7b33-5dd9-41f8-ad5e-970a46f5b39b",                        [{"alignmentgroup":"True","bingroup":"x","hovertemplate":"Difficulty=%{x}<br>count=%{y}<extra></extra>","legendgroup":"","marker":{"color":"indianred","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"type":"histogram","x":[1.0,2.5,3.0,2.0,2.0,3.0,3.0,1.0,2.0,1.0,3.0,3.0,1.5,2.0,3.0,2.0,1.5,1.0,2.0,2.0,1.5,2.0,2.0,1.5,3.0,2.0,1.5,1.0,1.0,1.0],"xaxis":"x","yaxis":"y"}],                        {"barmode":"relative","legend":{"tracegroupgap":0},"margin":{"t":60},"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Difficulty"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"count"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('470c7b33-5dd9-41f8-ad5e-970a46f5b39b');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
px.scatter(df, x = "Distance (miles)", y = "Average Time (hours)",
           color = "Difficulty", color_continuous_scale = "reds", template = "plotly_dark")
```


<div>                            <div id="89dfa448-71c3-4e57-bf40-33298d53f483" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("89dfa448-71c3-4e57-bf40-33298d53f483")) {                    Plotly.newPlot(                        "89dfa448-71c3-4e57-bf40-33298d53f483",                        [{"hovertemplate":"Distance (miles)=%{x}<br>Average Time (hours)=%{y}<br>Difficulty=%{marker.color}<extra></extra>","legendgroup":"","marker":{"color":[1.0,2.5,3.0,2.0,2.0,3.0,3.0,1.0,2.0,1.0,3.0,3.0,1.5,2.0,3.0,2.0,1.5,1.0,2.0,2.0,1.5,2.0,2.0,1.5,3.0,2.0,1.5,1.0,1.0,1.0],"coloraxis":"coloraxis","symbol":"circle"},"mode":"markers","name":"","orientation":"v","showlegend":false,"type":"scatter","x":[2.0,2.2,4.6,2.4,4.0,11.4,6.2,1.1,3.6,0.2,11.8,15.8,0.8,2.0,2.2,4.0,2.4,0.4,2.2,3.6,2.0,3.0,4.8,4.0,3.5,2.6,1.5,1.5,1.3,1.0],"xaxis":"x","y":[1.5,2.0,3.5,1.5,2.5,6.0,3.5,1.25,2.0,0.5,5.0,6.0,1.0,2.0,2.0,2.5,2.0,1.0,1.5,2.5,1.5,3.0,3.5,2.0,2.5,1.5,1.0,1.0,1.0,0.5],"yaxis":"y"}],                        {"coloraxis":{"colorbar":{"title":{"text":"Difficulty"}},"colorscale":[[0.0,"rgb(255,245,240)"],[0.125,"rgb(254,224,210)"],[0.25,"rgb(252,187,161)"],[0.375,"rgb(252,146,114)"],[0.5,"rgb(251,106,74)"],[0.625,"rgb(239,59,44)"],[0.75,"rgb(203,24,29)"],[0.875,"rgb(165,15,21)"],[1.0,"rgb(103,0,13)"]]},"legend":{"tracegroupgap":0},"margin":{"t":60},"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Distance (miles)"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Average Time (hours)"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('89dfa448-71c3-4e57-bf40-33298d53f483');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
#change the theme for all the other plotes. Thanks.
```
