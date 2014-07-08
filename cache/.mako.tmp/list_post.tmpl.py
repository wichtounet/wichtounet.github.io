# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1404851693.019014
_enable_loop = True
_template_filename = u'/home/wichtounet/.virtualenvs/blog/lib/python2.7/site-packages/nikola/data/themes/base/templates/list_post.tmpl'
_template_uri = u'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


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
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 19
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<article class="listpage">\n    <header>\n        <h1>')
        # SOURCE LINE 7
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n    </header>\n')
        # SOURCE LINE 9
        if posts:
            # SOURCE LINE 10
            __M_writer(u'    <ul class="postlist">\n')
            # SOURCE LINE 11
            for post in posts:
                # SOURCE LINE 12
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
            # SOURCE LINE 14
            __M_writer(u'    </ul>\n')
            # SOURCE LINE 15
        else:
            # SOURCE LINE 16
            __M_writer(u'    <p>')
            __M_writer(unicode(messages("No posts found.")))
            __M_writer(u'</p>\n')
        # SOURCE LINE 18
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


