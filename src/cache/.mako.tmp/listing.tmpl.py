# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394992176.008077
_enable_loop = True
_template_filename = '/usr/lib64/python3.3/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 19
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def content():
            return render_content(context)
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        # SOURCE LINE 6
        if folders or files:
            # SOURCE LINE 7
            __M_writer('<ul class="list-unstyled">\n')
            # SOURCE LINE 8
            for name in folders:
                # SOURCE LINE 9
                __M_writer('    <li><a href="')
                __M_writer(str(name))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i> ')
                __M_writer(str(name))
                __M_writer('</a>\n')
            # SOURCE LINE 11
            for name in files:
                # SOURCE LINE 12
                __M_writer('    <li><a href="')
                __M_writer(str(name))
                __M_writer('.html"><i class="glyphicon glyphicon-file"></i> ')
                __M_writer(str(name))
                __M_writer('</a>\n')
            # SOURCE LINE 14
            __M_writer('</ul>\n')
        # SOURCE LINE 16
        if code:
            # SOURCE LINE 17
            __M_writer('    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


