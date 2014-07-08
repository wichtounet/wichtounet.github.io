# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1404851692.997028
_enable_loop = True
_template_filename = u'/home/wichtounet/.virtualenvs/blog/lib/python2.7/site-packages/nikola/data/themes/bootstrap/templates/tags.tmpl'
_template_uri = u'tags.tmpl'
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
        cat_items = context.get('cat_items', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 26
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        cat_items = context.get('cat_items', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<h1>')
        # SOURCE LINE 5
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        # SOURCE LINE 6
        if cat_items:
            # SOURCE LINE 7
            __M_writer(u'    <h2>')
            __M_writer(unicode(messages("Categories")))
            __M_writer(u'</h2>\n    <ul class="unstyled">\n')
            # SOURCE LINE 9
            for text, link in cat_items:
                # SOURCE LINE 10
                if text:
                    # SOURCE LINE 11
                    __M_writer(u'            <li><a class="reference badge" href="')
                    __M_writer(unicode(link))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
            # SOURCE LINE 14
            __M_writer(u'    </ul>\n')
            # SOURCE LINE 15
            if items:
                # SOURCE LINE 16
                __M_writer(u'        <h2>')
                __M_writer(unicode(messages("Tags")))
                __M_writer(u'</h2>\n')
        # SOURCE LINE 19
        if items:
            # SOURCE LINE 20
            __M_writer(u'    <ul class="list-inline">\n')
            # SOURCE LINE 21
            for text, link in items:
                # SOURCE LINE 22
                __M_writer(u'        <li><a class="reference badge" href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a></li>\n')
            # SOURCE LINE 24
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


