# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1404851693.007584
_enable_loop = True
_template_filename = u'/home/wichtounet/.virtualenvs/blog/lib/python2.7/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = u'tag.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 13
        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 40
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        posts = context.get('posts', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n<article class="tagpage">\n    <header>\n        <h1>')
        # SOURCE LINE 19
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n        <div class="metadata">\n')
        # SOURCE LINE 21
        if len(translations) > 1 and generate_rss:
            # SOURCE LINE 22
            for language in translations:
                # SOURCE LINE 23
                __M_writer(u'                <p class="feedlink">\n                    <a href="')
                # SOURCE LINE 24
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'" hreflang="')
                __M_writer(unicode(language))
                __M_writer(u'" type="application/rss+xml">')
                __M_writer(unicode(messages('RSS feed', language)))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')</a>&nbsp;\n                </p>\n')
            # SOURCE LINE 27
        elif generate_rss:
            # SOURCE LINE 28
            __M_writer(u'                <p class="feedlink"><a href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'" type="application/rss+xml">')
            __M_writer(unicode(messages('RSS feed')))
            __M_writer(u'</a></p>\n')
        # SOURCE LINE 30
        __M_writer(u'        </div>\n    </header>\n')
        # SOURCE LINE 32
        if posts:
            # SOURCE LINE 33
            __M_writer(u'    <ul class="postlist">\n')
            # SOURCE LINE 34
            for post in posts:
                # SOURCE LINE 35
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(post.permalink()))
                __M_writer(u'" class="listtitle">')
                __M_writer(unicode(post.title()))
                __M_writer(u'</a> <time class="listdate" datetime="')
                __M_writer(unicode(post.date.isoformat()))
                __M_writer(u'" title="')
                __M_writer(unicode(messages("Publication date")))
                __M_writer(u'">')
                __M_writer(unicode(post.formatted_date(date_format)))
                __M_writer(u'</time></li>\n')
            # SOURCE LINE 37
            __M_writer(u'    </ul>\n')
        # SOURCE LINE 39
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        # SOURCE LINE 6
        if len(translations) > 1 and generate_rss:
            # SOURCE LINE 7
            for language in translations:
                # SOURCE LINE 8
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(unicode(kind))
                __M_writer(u' ')
                __M_writer(unicode(tag))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">\n')
            # SOURCE LINE 10
        elif generate_rss:
            # SOURCE LINE 11
            __M_writer(u'        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(unicode(kind))
            __M_writer(u' ')
            __M_writer(unicode(tag))
            __M_writer(u'" href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


