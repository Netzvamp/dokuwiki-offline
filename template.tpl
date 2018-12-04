<!DOCTYPE html>
<html>
<head>
    <title>{{title}} [{{hostname}}]</title>
    <link rel="stylesheet" type="text/css" href="{{root_link}}style.css"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>
<body>
<div id="dokuwiki__site">
    <div id="dokuwiki__top" class="site dokuwiki mode_show tpl_dokuwiki loggedIn  home  ">
        <div id="dokuwiki__header">
            <div class="headings group">
                <h1><a href="{{root_link}}start.html"><img src="{{root_link}}wiki/dokuwiki-128.png" width="64" height="64" alt=""><span>{{hostname}}</span></a></h1>
            </div>
            <div class="breadcrumbs">
                <div class="youarehere"><span class="home"> {{path}}</span></div>
            </div>

        </div>
        <div class="wrapper group">
            <div id="dokuwiki__content">
                <div class="page group">
                    {{body_content}}
                </div>
            </div>
        </div>
    </div>
</body>
</html>