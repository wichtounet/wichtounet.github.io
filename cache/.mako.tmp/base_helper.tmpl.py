# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1405539471.671815
_enable_loop = True
_template_filename = u'/home/wichtounet/.virtualenvs/blog/lib/python2.7/site-packages/nikola/data/themes/bootstrap/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_headstart', 'html_navigation_links', 'html_stylesheets', 'html_translations', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'\n\n\n')
        # SOURCE LINE 84
        __M_writer(u'\n\n\n')
        # SOURCE LINE 115
        __M_writer(u'\n\n\n')
        # SOURCE LINE 139
        __M_writer(u'\n\n')
        # SOURCE LINE 153
        __M_writer(u'\n\n')
        # SOURCE LINE 161
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        colorbox_locales = context.get('colorbox_locales', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 62
        if use_bundles:
            # SOURCE LINE 63
            if use_cdn:
                # SOURCE LINE 64
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>\n            <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
                # SOURCE LINE 67
            else:
                # SOURCE LINE 68
                __M_writer(u'            <script src="/assets/js/all-nocdn.js"></script>\n')
            # SOURCE LINE 70
        else:
            # SOURCE LINE 71
            if use_cdn:
                # SOURCE LINE 72
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>\n            <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>\n')
                # SOURCE LINE 74
            else:
                # SOURCE LINE 75
                __M_writer(u'            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n')
            # SOURCE LINE 78
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        # SOURCE LINE 80
        if colorbox_locales[lang]:
            # SOURCE LINE 81
            __M_writer(u'        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(unicode(colorbox_locales[lang]))
            __M_writer(u'.js"></script>\n')
        # SOURCE LINE 83
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        # SOURCE LINE 7
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            # SOURCE LINE 8
            __M_writer(u"prefix='")
            # SOURCE LINE 9
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                # SOURCE LINE 10
                __M_writer(u'og: http://ogp.me/ns# ')
            # SOURCE LINE 12
            if use_open_graph:
                # SOURCE LINE 13
                __M_writer(u'article: http://ogp.me/ns/article# ')
            # SOURCE LINE 15
            if comment_system == 'facebook':
                # SOURCE LINE 16
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            # SOURCE LINE 18
            __M_writer(u"'")
        # SOURCE LINE 21
        if is_rtl:
            # SOURCE LINE 22
            __M_writer(u'dir="rtl" ')
        # SOURCE LINE 25
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n')
        # SOURCE LINE 28
        if description:
            # SOURCE LINE 29
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        # SOURCE LINE 31
        __M_writer(u'    <meta name="viewport" content="width=device-width">\n    <title>')
        # SOURCE LINE 32
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n\n    ')
        # SOURCE LINE 34
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 35
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n')
        # SOURCE LINE 36
        if permalink:
            # SOURCE LINE 37
            __M_writer(u'      <link rel="canonical" href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        if favicons:
            # SOURCE LINE 41
            for name, file, size in favicons:
                # SOURCE LINE 42
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        # SOURCE LINE 45
        __M_writer(u'\n')
        # SOURCE LINE 46
        if comment_system == 'facebook':
            # SOURCE LINE 47
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        # SOURCE LINE 49
        __M_writer(u'\n    ')
        # SOURCE LINE 50
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        # SOURCE LINE 51
        if use_cdn:
            # SOURCE LINE 52
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
            # SOURCE LINE 53
        else:
            # SOURCE LINE 54
            __M_writer(u'        <!--[if lt IE 9]><script src="/assets/js/html5.js"></script><![endif]-->\n')
        # SOURCE LINE 56
        __M_writer(u'\n    ')
        # SOURCE LINE 57
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 118
        __M_writer(u'\n')
        # SOURCE LINE 119
        for url, text in navigation_links[lang]:
            # SOURCE LINE 120
            if isinstance(url, tuple):
                # SOURCE LINE 121
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(unicode(text))
                __M_writer(u'<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                # SOURCE LINE 123
                for suburl, text in url:
                    # SOURCE LINE 124
                    if rel_link(permalink, suburl) == "#":
                        # SOURCE LINE 125
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 126
                    else:
                        # SOURCE LINE 127
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                # SOURCE LINE 130
                __M_writer(u'            </ul>\n')
                # SOURCE LINE 131
            else:
                # SOURCE LINE 132
                if rel_link(permalink, url) == "#":
                    # SOURCE LINE 133
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 134
                else:
                    # SOURCE LINE 135
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        notes = context.get('notes', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        post = context.get('post', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n')
        # SOURCE LINE 88
        if use_bundles:
            # SOURCE LINE 89
            if use_cdn:
                # SOURCE LINE 90
                __M_writer(u'            <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
                # SOURCE LINE 92
            else:
                # SOURCE LINE 93
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 95
        else:
            # SOURCE LINE 96
            if use_cdn:
                # SOURCE LINE 97
                __M_writer(u'            <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">\n')
                # SOURCE LINE 98
            else:
                # SOURCE LINE 99
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 102
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 106
            if has_custom_css:
                # SOURCE LINE 107
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 110
        if annotations and post and not post.meta('noannotations'):
            # SOURCE LINE 111
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
            # SOURCE LINE 112
        elif not annotations and post and post.meta('annotations'):
            # SOURCE LINE 113
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 155
        __M_writer(u'\n')
        # SOURCE LINE 156
        for langname in translations.keys():
            # SOURCE LINE 157
            if langname != lang:
                # SOURCE LINE 158
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(_link("index", None, langname)))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 141
        __M_writer(u'\n')
        # SOURCE LINE 142
        if rss_link:
            # SOURCE LINE 143
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 144
        elif generate_rss:
            # SOURCE LINE 145
            if len(translations) > 1:
                # SOURCE LINE 146
                for language in translations:
                    # SOURCE LINE 147
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
                # SOURCE LINE 149
            else:
                # SOURCE LINE 150
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


