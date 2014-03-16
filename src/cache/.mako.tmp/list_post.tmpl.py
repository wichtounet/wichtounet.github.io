# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394986051.0914426
_enable_loop = True
_template_filename = '/usr/lib64/python3.3/site-packages/nikola/data/themes/bootstrap3/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


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
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 18
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n        <!--Body content-->\n        <div class="postbox">\n        <h1>')
        # SOURCE LINE 6
        __M_writer(str(title))
        __M_writer('</h1>\n')
        # SOURCE LINE 7
        if posts:
            # SOURCE LINE 8
            __M_writer('        <ul class="list-unstyled">\n')
            # SOURCE LINE 9
            for post in posts:
                # SOURCE LINE 10
                __M_writer('            <li><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('">[')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('] ')
                __M_writer(str(post.title()))
                __M_writer('</a>\n')
            # SOURCE LINE 12
            __M_writer('        </ul>\n')
            # SOURCE LINE 13
        else:
            # SOURCE LINE 14
            __M_writer('        <p>')
            __M_writer(str(messages("No posts found.")))
            __M_writer('</p>\n')
        # SOURCE LINE 16
        __M_writer('        </div>\n        <!--End of body content-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


