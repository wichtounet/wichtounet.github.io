# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394996475.2532482
_enable_loop = True
_template_filename = '/usr/lib64/python3.3/site-packages/nikola/data/themes/bootstrap3/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 11
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 36
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 44
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer('\n')
        # SOURCE LINE 39
        if not post.meta('password'):
            # SOURCE LINE 40
            __M_writer('    <li>\n    <a href="')
            # SOURCE LINE 41
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer('\n    <article class="postbox post-')
        # SOURCE LINE 13
        __M_writer(str(post.meta('type')))
        __M_writer('">\n    <div class="h-entry" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        # SOURCE LINE 15
        __M_writer(str(helper.html_title()))
        __M_writer('\n    <hr>\n    <small>\n        ')
        # SOURCE LINE 18
        __M_writer(str(messages("Posted:")))
        __M_writer(' <time class="published dt-published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('" itemprop="datePublished">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n        ')
        # SOURCE LINE 19
        __M_writer(str(helper.html_translations(post)))
        __M_writer('\n        ')
        # SOURCE LINE 20
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    </small>\n    <hr>\n    <div class="e-content" itemprop="articleBody text">\n    ')
        # SOURCE LINE 24
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n')
        # SOURCE LINE 26
        if post.description():
            # SOURCE LINE 27
            __M_writer('        <meta content="')
            __M_writer(str(post.description()))
            __M_writer('" itemprop="description">\n')
        # SOURCE LINE 29
        __M_writer('    </div>\n    ')
        # SOURCE LINE 30
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        # SOURCE LINE 31
        if not post.meta('nocomments'):
            # SOURCE LINE 32
            __M_writer('        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        # SOURCE LINE 34
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    </article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n')
        # SOURCE LINE 7
        if post.meta('keywords'):
            # SOURCE LINE 8
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        # SOURCE LINE 10
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


