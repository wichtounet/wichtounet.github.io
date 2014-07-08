# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1404851693.14648
_enable_loop = True
_template_filename = u'/home/wichtounet/.virtualenvs/blog/lib/python2.7/site-packages/nikola/data/themes/base/templates/post_header.tmpl'
_template_uri = u'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_post_header', 'html_title', 'html_translations', 'html_sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        def html_title():
            return render_html_title(context)
        messages = context.get('messages', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        comments = _mako_get_namespace(context, 'comments')
        def html_translations(post):
            return render_html_translations(context,post)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    <header>\n        ')
        # SOURCE LINE 32
        __M_writer(unicode(html_title()))
        __M_writer(u'\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
        # SOURCE LINE 34
        __M_writer(unicode(post.author()))
        __M_writer(u'</span></p>\n            <p class="dateline"><a href="')
        # SOURCE LINE 35
        __M_writer(unicode(post.permalink()))
        __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(unicode(post.date.isoformat()))
        __M_writer(u'" itemprop="datePublished" title="')
        __M_writer(unicode(messages("Publication date")))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time></a></p>\n')
        # SOURCE LINE 36
        if not post.meta('nocomments') and site_has_comments:
            # SOURCE LINE 37
            __M_writer(u'                <p class="commentline">')
            __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer(u'\n')
        # SOURCE LINE 39
        __M_writer(u'            ')
        __M_writer(unicode(html_sourcelink()))
        __M_writer(u'\n')
        # SOURCE LINE 40
        if post.meta('link'):
            # SOURCE LINE 41
            __M_writer(u"                    <p><a href='")
            __M_writer(unicode(post.meta('link')))
            __M_writer(u"'>")
            __M_writer(unicode(messages("Original site")))
            __M_writer(u'</a></p>\n')
        # SOURCE LINE 43
        if post.description():
            # SOURCE LINE 44
            __M_writer(u'                <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        # SOURCE LINE 46
        __M_writer(u'        </div>\n        ')
        # SOURCE LINE 47
        __M_writer(unicode(html_translations(post)))
        __M_writer(u'\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        if title and not post.meta('hidetitle'):
            # SOURCE LINE 7
            __M_writer(u'    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(filters.html_escape(unicode(title)))
            __M_writer(u'</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        if len(translations) > 1:
            # SOURCE LINE 13
            __M_writer(u'        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            # SOURCE LINE 14
            __M_writer(unicode(messages("Also available in:")))
            __M_writer(u'</h3>\n')
            # SOURCE LINE 15
            for langname in translations.keys():
                # SOURCE LINE 16
                if langname != lang and post.is_translation_available(langname):
                    # SOURCE LINE 17
                    __M_writer(u'                <p><a href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'" rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'">')
                    __M_writer(unicode(messages("LANGUAGE", langname)))
                    __M_writer(u'</a></p>\n')
            # SOURCE LINE 20
            __M_writer(u'        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        if show_sourcelink:
            # SOURCE LINE 26
            __M_writer(u'        <p class="sourceline"><a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


