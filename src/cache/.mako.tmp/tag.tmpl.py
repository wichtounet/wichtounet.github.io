# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394992920.3319335
_enable_loop = True
_template_filename = '/usr/lib64/python3.3/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


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
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        tag = context.get('tag', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 11
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 34
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        def content():
            return render_content(context)
        tag = context.get('tag', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer('\n        <!--Body content-->\n        <div class="postbox">\n        <h1>')
        # SOURCE LINE 16
        __M_writer(str(title))
        __M_writer('</h1>\n')
        # SOURCE LINE 17
        if len(translations) > 1:
            # SOURCE LINE 18
            for language in translations:
                # SOURCE LINE 19
                __M_writer('                <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">RSS (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n')
            # SOURCE LINE 21
        else:
            # SOURCE LINE 22
            __M_writer('            <a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">RSS</a>\n')
        # SOURCE LINE 24
        __M_writer('        <br>\n')
        # SOURCE LINE 25
        if posts:
            # SOURCE LINE 26
            __M_writer('        <ul class="unstyled">\n')
            # SOURCE LINE 27
            for post in posts:
                # SOURCE LINE 28
                __M_writer('            <li><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('">[')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('] ')
                __M_writer(str(post.title()))
                __M_writer('</a>\n')
            # SOURCE LINE 30
            __M_writer('        </ul>\n')
        # SOURCE LINE 32
        __M_writer('        </div>\n        <!--End of body content-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        tag = context.get('tag', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
        if len(translations) > 1:
            # SOURCE LINE 5
            for language in translations:
                # SOURCE LINE 6
                __M_writer('            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(str(tag))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
            # SOURCE LINE 8
        else:
            # SOURCE LINE 9
            __M_writer('        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(str(tag))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


