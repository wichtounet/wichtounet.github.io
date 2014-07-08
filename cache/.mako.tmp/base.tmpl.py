# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1404851692.951122
_enable_loop = True
_template_filename = u'themes/wicht/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'extra_js', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        notes = _mako_get_namespace(context, 'notes')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        base = _mako_get_namespace(context, 'base')
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        IOError = _import_ns.get('IOError', context.get('IOError', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        hide_sourcelink = _import_ns.get('hide_sourcelink', context.get('hide_sourcelink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n<link href="/favicon.ico" rel="icon" type="image/x-icon">\n</head>\n<body>\n\n<div class="social_container">\n    <div class="social_container_gplus">\n        <a target="_blank" title="Share on Google+" href="https://plusone.google.com/_/+1/confirm?hl=en&url=')
        # SOURCE LINE 16
        __M_writer(unicode(abs_link(permalink)))
        __M_writer(u'"><img src="/assets/img/google_plus.png" /></a>\n    </div>\n    <div class="social_container_facebook">\n        <a target="_blank" title="Share on Facebook" href="http://www.facebook.com/sharer/sharer.php?u=#url"><img src="/assets/img/facebook.png" /></a>\n    </div>\n    <div class="social_container_twitter">\n        <a target="_blank" title="Tweet on Twitter" href="http://twitter.com/home?status=#url"><img src="/assets/img/twitter.svg" /></a>\n    </div>\n</div>\n\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="container-fluid"><!-- This keeps the margins nice -->\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="')
        # SOURCE LINE 37
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n                <span id="blog-title">')
        # SOURCE LINE 38
        __M_writer(unicode(blog_title))
        __M_writer(u'</span>\n            </a>\n        </div><!-- /.navbar-header -->\n        \n        <div class="collapse navbar-collapse navbar-ex1-collapse">\n            <ul class="nav navbar-nav">\n                ')
        # SOURCE LINE 44
        __M_writer(unicode(base.html_navigation_links()))
        __M_writer(u'\n            </ul>\n\n            <span class="navbar-form pull-left">\n                <form action="/stories/search.html">\n                    <input type="text" name="q" id="tipue_search_input">\n                </form>\n            </span>\n            \n            <ul class="nav navbar-nav navbar-right">\n                <li>\n                    <a target="_blank" title="Follow @wichtounet on Twitter" href="https://twitter.com/wichtounet">\n                        <img src="/assets/img/twitter.svg" alt="Follow @wichtounet on Twitter" />\n                    </a>\n                </li>\n                <li>\n                    <a target="_blank" title="Follow +BaptisteWicht on Google+" href="https://plus.google.com/+BaptisteWicht">\n                        <img src="/assets/img/google_plus.svg" alt="Follow +BaptisteWicht on Google+" />\n                    </a>\n                </li>\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container-fluid -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="body-container">\n\n    <!-- Sidebar -->\n\n    <div class="left-sidebar">\n')
        # SOURCE LINE 76
        if not post:
            # SOURCE LINE 77
            __M_writer(u'            <div class="left-sidebar-widget">\n                <h3>Welcome to my blog</h3>\n                <div class="left-sidebar-widget-content">\n                    <div class="g-person" data-width="275" data-href="//plus.google.com/u/0/103113673902796202116" data-theme="dark" data-layout="landscape" data-rel="author"></div>\n                </div>\n            </div>\n\n            <div class="left-sidebar-widget">\n                <h3>Tags</h3>\n                <div class="left-sidebar-widget-content">\n                    <div id="tags_container">\n                        <canvas width="275" height="250" id="tags_canvas">\n                            <p>Anything in here will be replaced on browsers that support the canvas element</p>\n                        </canvas>\n                    </div>\n                </div>\n            </div>\n')
            # SOURCE LINE 94
        elif post:
            # SOURCE LINE 95
            __M_writer(u'            <div class="left-sidebar-widget">\n                <div class="left-sidebar-widget-content">\n                    <div class="g-person" data-width="275" data-href="//plus.google.com/u/0/103113673902796202116" data-theme="dark" data-layout="landscape" data-rel="author"></div>\n                </div>\n            </div>\n')
        # SOURCE LINE 101
        __M_writer(u'\n')
        # SOURCE LINE 102
        if post and not post.source_link().startswith('/stories/'):
            # SOURCE LINE 103
            __M_writer(u'            <div class="left-sidebar-widget">\n                <h3>Related posts</h3>\n                <div class="left-sidebar-widget-content">\n                    ')
            # SOURCE LINE 106

            related_path = post.source_path + ".related.html"
            import codecs
            
            try:
                with codecs.open(related_path, 'r', 'utf8') as f:
                    related_text = f.read()
                    f.close()
            except IOError as e:
                related_text = "Not generated"
                                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['e','f','related_text','related_path','codecs'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 116
            __M_writer(u'\n                    ')
            # SOURCE LINE 117
            __M_writer(unicode(related_text))
            __M_writer(u'\n                </div>\n            </div>\n')
        # SOURCE LINE 121
        __M_writer(u'        \n        <div class="left-sidebar-widget">\n            <h3>Recent comments</h3>\n            <div class="left-sidebar-widget-content">\n                <div id="recentcomments" class="dsq-widget">\n                    <script type="text/javascript" src="http://blogwichtounet.disqus.com/recent_comments_widget.js?num_items=5&hide_avatars=0&avatar_size=28&excerpt_length=50"></script> \n                </div>\n            </div>\n        </div>\n\n        <div class="left-sidebar-widget">\n            <h3>Blogroll</h3>\n            <div class="left-sidebar-widget-content">\n                <ul>\n                    <li><a target="_blank" href="http://www.asjava.com/">AsJava.com : Java Tutorial</a></li>\n                    <li><a target="_blank" href="http://www.mkyong.com/">Mkyong : Java Tutorials</a></li>\n                </ul>\n            </div>\n        </div>\n    </div>\n\n')
        # SOURCE LINE 142
        if post and post.source_link() == '/stories/search.md':
            # SOURCE LINE 143
            __M_writer(u'        ')
            __M_writer(unicode(base.late_load_js()))
            __M_writer(u'\n')
        # SOURCE LINE 145
        __M_writer(u'\n    <!-- Content -->\n\n    <div class="container">\n        <div class="body-content">\n            <div class="row">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 151
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n</div>\n\n<!-- Footer -->\n\n<footer>\n    ')
        # SOURCE LINE 160
        __M_writer(unicode(content_footer))
        __M_writer(u'\n')
        # SOURCE LINE 161
        if not hide_sourcelink:
            # SOURCE LINE 162
            __M_writer(u'        <ul class="footer_inline_ul">\n            ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            # SOURCE LINE 163
            __M_writer(u'\n        </ul>\n')
        # SOURCE LINE 166
        __M_writer(u'</footer>\n\n<!-- Late loading stuff  -->\n\n')
        # SOURCE LINE 170
        if not post or not post.source_link() == '/stories/search.md':
            # SOURCE LINE 171
            __M_writer(u'    ')
            __M_writer(unicode(base.late_load_js()))
            __M_writer(u'\n')
        # SOURCE LINE 173
        __M_writer(u'\n')
        # SOURCE LINE 174
        if not post:
            # SOURCE LINE 175
            __M_writer(u'    <script type="text/javascript">\n      $(document).ready(function() {\n        jQuery.getJSON(\'/assets/js/tag_cloud_data.json\', function(data) {\n            var items = [];\n\n            $.each(data, function(key, val) {\n                items.push(\'<li><a href="\' + val[1] +\'" \'+\'data-weight="\'+val[0]+\'"\'+\'>\' + key + \'</a></li>\');\n            });\n\n            $(\'<div/>\', {\n                \'id\': \'tags\',\n                html: \'<ul>\' + items.join(\'\') + \'</ul>\'\n            }).appendTo(\'body\');\n\n            if(!$(\'#tags_canvas\').tagcanvas({\n                textColour: \'#FFFFFF\',\n                outlineColour: \'#ff00ff\',\n                reverse: true,\n                depth: 0.8,\n                maxSpeed: 0.05,\n                weight: true,\n                weightFrom: "data-weight",\n                weightSizeMin: 8,\n                weightSizeMax: 24\n            },\'tags\')) {\n                //something went wrong, hide the canvas container\n                $(\'#tags_container\').hide();\n            }});\n        });\n    </script>\n')
        # SOURCE LINE 206
        __M_writer(u'\n<!-- Google platform JS -->\n    \n<script type="text/javascript" src="https://apis.google.com/js/platform.js"></script>\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        # SOURCE LINE 212
        __M_writer(u'\n\n')
        # SOURCE LINE 214
        if annotations and post and not post.meta('noannotations'):
            # SOURCE LINE 215
            __M_writer(u'    ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
            # SOURCE LINE 216
        elif not annotations and post and post.meta('annotations'):
            # SOURCE LINE 217
            __M_writer(u'    ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
        # SOURCE LINE 219
        __M_writer(u'\n')
        # SOURCE LINE 220
        __M_writer(unicode(body_end))
        __M_writer(u'\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


