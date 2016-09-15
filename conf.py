# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

#!! This is the configuration of Nikola. !!#
#!!  You should edit it to your liking.  !!#

GITHUB_SOURCE_BRANCH = 'sources'
GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_REMOTE_NAME = 'origin'

# Data about this site
BLOG_AUTHOR = "Baptiste Wicht"
BLOG_TITLE = "@Blog(\"Baptiste Wicht\")"
SITE_URL = "http://baptiste-wicht.com/"
BLOG_EMAIL = "baptistewicht@gmail.com"
BLOG_DESCRIPTION = "Tutorials and short posts about programming, C++, Java, Assembly, Operating Systems Development, Compilers, ..."

WRITE_TAG_CLOUD = True

DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.rst.pl will be considered
# its Polish translation.
#     (in the above example: path == "something", lang == "pl", ext == "rst")
# this pattern is also used for metadata:
#     something.meta -> something.meta.pl

TRANSLATIONS_PATTERN = "{path}.{ext}.{lang}"

# If you don't want your Polish files to be considered Perl code, use this:
# TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"
#     Note that this pattern will become the default in v7.0.0.

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/stories/about.html', 'About'),
        ('/stories/publications.html', 'Publications'),
        ('/stories/donate.html', 'Donate'),
        ('/stories/contact.html', 'Contact'),
        ('/stories/faq.html', 'FAQ'),
        ('/stories/legal.html', 'Legal'),
        ('/categories/index.html', 'Tags'),
        ('/archive.html', 'Archives'),
        ('http://feeds.feedburner.com/BaptisteWicht', 'RSS'),
    ),
}

# Below this point, everything is optional

# While nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can ommit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
            ("posts/*.rst", "posts", "post.tmpl"),
            ("posts/*.md", "posts", "post.tmpl"),
            ("posts/*.wp", "posts", "post.tmpl"),
        )
PAGES = (
            ("stories/*.rst", "stories", "story.tmpl"),
            ("stories/*.md", "stories", "story.tmpl"),
            ("stories/*.wp", "stories", "story.tmpl"),
        )

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
        "rest": ('.rst',),
        "markdown": ('.md', '.mdown', '.markdown', '.wp',),
        "html": ('.html', '.htm',)
        }


# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
ONE_FILE_POSTS = False

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# HIDE_UNTRANSLATED_POSTS = False

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
FEED_LENGTH = 25

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [["posts/update-thor-thesis-and-publications.html", "/posts/2016/08/update-thor-thesis-and-publications.html"], ["2011/06/eddi-0-2-1-integer-operations-and-optimizations/index.html", "/posts/2011/06/eddi-0-2-1-integer-operations-and-optimizations.html"], ["2012/12/eddic-1-2-1-string-concatenation-and-vector/index.html", "/posts/2012/12/eddic-1-2-1-string-concatenation-and-vector.html"], ["2011/09/packt-open-source-awards-2011/index.html", "/posts/2011/09/packt-open-source-awards-2011.html"], ["2010/09/jtheque-utils-1-1-5/index.html", "/posts/2010/09/jtheque-utils-1-1-5.html"], ["2012/09/eddi-compiler-1-1-3-templates/index.html", "/posts/2012/09/eddi-compiler-1-1-3-templates.html"], ["2012/01/install-insight-debugger-linux-mint-ubuntu/index.html", "/posts/2012/01/install-insight-debugger-linux-mint-ubuntu.html"], ["2011/09/book-review-effective-c/index.html", "/posts/2011/09/book-review-effective-c.html"], ["2012/03/eddic-0-9-floating-point-support/index.html", "/posts/2012/03/eddic-0-9-floating-point-support.html"], ["2010/01/new-design-jtheque-website/index.html", "/posts/2010/01/new-design-jtheque-website.html"], ["2011/12/merry-christmas/index.html", "/posts/2011/12/merry-christmas.html"], ["2010/05/ubuntu-lucid-lynx-buttons-right/index.html", "/posts/2010/05/ubuntu-lucid-lynx-buttons-right.html"], ["2010/05/modular-application-loading-modules/index.html", "/posts/2010/05/modular-application-loading-modules.html"], ["2010/08/java-file-copy-benchmarks-update/index.html", "/posts/2010/08/java-file-copy-benchmarks-update.html"], ["2011/07/eddi-0-4-native-compilation-swap/index.html", "/posts/2011/07/eddi-0-4-native-compilation-swap.html"], ["2010/08/tip-launch-java-applications-from-java-applications-with-ant/index.html", "/posts/2010/08/tip-launch-java-applications-from-java-applications-with-ant.html"], ["2010/03/java-swing-focus/index.html", "/posts/2010/03/java-swing-focus.html"], ["2010/08/file-copy-in-java-benchmark/index.html", "/posts/2010/08/file-copy-in-java-benchmark.html"], ["2010/03/4-reasons-not-using-osmorc-anymore/index.html", "/posts/2010/03/4-reasons-not-using-osmorc-anymore.html"], ["2010/05/switch-kubuntu-to-ubuntu/index.html", "/posts/2010/05/switch-kubuntu-to-ubuntu.html"], ["2012/03/1726/index.html", "/stories/2012/03/1726.html"], ["2010/04/jetbrains-released-intellij-idea-9-0-2/index.html", "/posts/2010/04/jetbrains-released-intellij-idea-9-0-2.html"], ["2011/11/new-theme-site/index.html", "/posts/2011/11/new-theme-site.html"], ["2010/05/jtheque-licensed-under-apache-license-2-0/index.html", "/posts/2010/05/jtheque-licensed-under-apache-license-2-0.html"], ["2012/09/packt-publishing-thousandth-book-celebration/index.html", "/posts/2012/09/packt-publishing-thousandth-book-celebration.html"], ["2010/04/10-most-useful-google-tools/index.html", "/posts/2010/04/10-most-useful-google-tools.html"], ["2010/04/using-substance-look-and-feel-in-osgi/index.html", "/posts/2010/04/using-substance-look-and-feel-in-osgi.html"], ["2012/03/1730/index.html", "/stories/2012/03/1730.html"], ["2010/05/modular-application-modules/index.html", "/posts/2010/05/modular-application-modules.html"], ["2010/04/java-7-updates-project-coin/index.html", "/posts/2010/04/java-7-updates-project-coin.html"], ["2011/05/now-writing-from-berkeley-california/index.html", "/posts/2011/05/now-writing-from-berkeley-california.html"], ["2010/03/sonar-2-0-released/index.html", "/posts/2010/03/sonar-2-0-released.html"], ["2011/11/dynamic-memory-allocation-intel-assembly-linux/index.html", "/posts/2011/11/dynamic-memory-allocation-intel-assembly-linux.html"], ["2010/06/how-to-choose-a-monitor/index.html", "/posts/2010/06/how-to-choose-a-monitor.html"], ["2010/09/java-synchronization-mutual-exclusion-benchmark/index.html", "/posts/2010/09/java-synchronization-mutual-exclusion-benchmark.html"], ["2010/09/java-concurrency-atomic-variables/index.html", "/posts/2010/09/java-concurrency-atomic-variables.html"], ["2013/12/thor-os-boot-process/index.html", "/posts/2013/12/thor-os-boot-process.html"], ["2010/02/logging-with-slf4j/index.html", "/posts/2010/02/logging-with-slf4j.html"], ["2010/04/drag-and-drop-files-to-gmail/index.html", "/posts/2010/04/drag-and-drop-files-to-gmail.html"], ["2010/01/dont-use-shorts-in-loop/index.html", "/posts/2010/01/dont-use-shorts-in-loop.html"], ["2011/06/solve-file-param-is-missing-problem-of-w3-total-cache/index.html", "/posts/2011/06/solve-file-param-is-missing-problem-of-w3-total-cache.html"], ["2013/12/gentoo-tips-avoid-gnome-3-8-emerged-automatically/index.html", "/posts/2013/12/gentoo-tips-avoid-gnome-3-8-emerged-automatically.html"], ["2010/04/maven-3-0-beta-1-is-here/index.html", "/posts/2010/04/maven-3-0-beta-1-is-here.html"], ["2013/07/home-server-adventure-step-1/index.html", "/posts/2013/07/home-server-adventure-step-1.html"], ["2011/07/eddi-0-4-1-loops-and-better-assembly-generation/index.html", "/posts/2011/07/eddi-0-4-1-loops-and-better-assembly-generation.html"], ["2012/03/a-new-theme-for-the-site/index.html", "/posts/2012/03/a-new-theme-for-the-site.html"], ["faq/index.html", "/stories/faq.html"], ["2012/03/1716/index.html", "/stories/2012/03/1716.html"], ["2012/12/cpp-benchmark-vector-list-deque/index.html", "/posts/2012/12/cpp-benchmark-vector-list-deque.html"], ["2010/07/modular-java-book-review/index.html", "/posts/2010/07/modular-java-book-review.html"], ["2012/11/eddic-compiles-with-clang-3-1/index.html", "/posts/2012/11/eddic-compiles-with-clang-3-1.html"], ["2012/01/eddic-0-7-compiler-model-optimizations/index.html", "/posts/2012/01/eddic-0-7-compiler-model-optimizations.html"], ["2013/01/eddic-1-2-2-performances-optimization-library/index.html", "/posts/2013/01/eddic-1-2-2-performances-optimization-library.html"], ["2012/03/1727/index.html", "/stories/2012/03/1727.html"], ["2010/08/presentation-usage-h2-database-engine/index.html", "/posts/2010/08/presentation-usage-h2-database-engine.html"], ["2010/07/profile-applications-java-visualvm/index.html", "/posts/2010/07/profile-applications-java-visualvm.html"], ["2011/12/wordpress-3-3-sonny-released/index.html", "/posts/2011/12/wordpress-3-3-sonny-released.html"], ["2010/09/save-time-with-the-gmail-priority-inbox/index.html", "/posts/2010/09/save-time-with-the-gmail-priority-inbox.html"], ["2010/07/play-framework-template-engine/index.html", "/posts/2010/07/play-framework-template-engine.html"], ["2012/06/the-site-now-running-wordpress-3-4/index.html", "/posts/2012/06/the-site-now-running-wordpress-3-4.html"], ["2012/08/architexa-free-understand-code-base/index.html", "/posts/2012/08/architexa-free-understand-code-base.html"], ["2011/01/export-a-sharepoint-2010-site-as-solution-package/index.html", "/posts/2011/01/export-a-sharepoint-2010-site-as-solution-package.html"], ["2010/09/hardware-guide-the-power-supply/index.html", "/posts/2010/09/hardware-guide-the-power-supply.html"], ["2010/07/intellij-idea-9-0-3-is-here/index.html", "/posts/2010/07/intellij-idea-9-0-3-is-here.html"], ["2012/01/compilers-principles-techniques-tools/index.html", "/posts/2012/01/compilers-principles-techniques-tools.html"], ["2012/04/switching-gentoo-linux/index.html", "/posts/2012/04/switching-gentoo-linux.html"], ["2010/09/solve-einsteins-riddle-using-prolog/index.html", "/posts/2010/09/solve-einsteins-riddle-using-prolog.html"], ["2012/05/compiler-architecture-refinements-eddic/index.html", "/posts/2012/05/compiler-architecture-refinements-eddic.html"], ["2012/03/cp11-concurrency-tutorial-part-2-protect-shared-data/index.html", "/posts/2012/03/cp11-concurrency-tutorial-part-2-protect-shared-data.html"], ["2012/03/introduction-64-bit-intel-assembly-language-programming-linux-book-review/index.html", "/posts/2012/03/introduction-64-bit-intel-assembly-language-programming-linux-book-review.html"], ["2013/06/improving-eddic-boost-spirit-parser-performances/index.html", "/posts/2013/06/improving-eddic-boost-spirit-parser-performances.html"], ["2010/07/version-control-with-git-book-review/index.html", "/posts/2010/07/version-control-with-git-book-review.html"], ["2010/05/java-concurrency-part-2-manipulate-threads/index.html", "/posts/2010/05/java-concurrency-part-2-manipulate-threads.html"], ["2010/07/osgi-hello-world-services/index.html", "/posts/2010/07/osgi-hello-world-services.html"], ["2012/03/1729/index.html", "/stories/2012/03/1729.html"], ["2013/03/eddic-1-2-3-better-data-flow-analysis/index.html", "/posts/2013/03/eddic-1-2-3-better-data-flow-analysis.html"], ["2010/07/top-15-best-wordpress-plugins/index.html", "/posts/2010/07/top-15-best-wordpress-plugins.html"], ["2013/06/some-news/index.html", "/posts/2013/06/some-news.html"], ["2010/03/osgi-enterprise-4-2-available/index.html", "/posts/2010/03/osgi-enterprise-4-2-available.html"], ["2012/11/gcc-4-7-clang-3-1-eddic/index.html", "/posts/2012/11/gcc-4-7-clang-3-1-eddic.html"], ["2010/02/modular-application-jtheque-core-2-0-3/index.html", "/posts/2010/02/modular-application-jtheque-core-2-0-3.html"], ["2012/03/1724/index.html", "/stories/2012/03/1724.html"], ["2011/09/google-is-open-to-all/index.html", "/posts/2011/09/google-is-open-to-all.html"], ["2010/09/java-concurrency-part-5-monitors-locks-and-conditions/index.html", "/posts/2010/09/java-concurrency-part-5-monitors-locks-and-conditions.html"], ["2010/10/jtheque-core-2-1-0-released/index.html", "/posts/2010/10/jtheque-core-2-1-0-released.html"], ["2010/08/holidays/index.html", "/posts/2010/08/holidays.html"], ["2012/02/cojac-a-numerical-problem-sniffer/index.html", "/posts/2012/02/cojac-a-numerical-problem-sniffer.html"], ["2012/08/memory-manager-intel-assembly-64-linux/index.html", "/posts/2012/08/memory-manager-intel-assembly-64-linux.html"], ["2013/07/zyxel-gs1910-managed-gigabit-switch-review/index.html", "/posts/2013/07/zyxel-gs1910-managed-gigabit-switch-review.html"], ["2011/06/eddi-new-programming-language/index.html", "/posts/2011/06/eddi-new-programming-language.html"], ["2010/07/state-of-the-lambda/index.html", "/posts/2010/07/state-of-the-lambda.html"], ["2010/08/java-concurrrency-synchronization-locks/index.html", "/posts/2010/08/java-concurrrency-synchronization-locks.html"], ["2011/10/eddic-0-5-functions-foreach/index.html", "/posts/2011/10/eddic-0-5-functions-foreach.html"], ["2014/01/budgetwarrior-0-2-1-minor-changes-gentoo-ebuild/index.html", "/posts/2014/01/budgetwarrior-0-2-1-minor-changes-gentoo-ebuild.html"], ["2010/07/tip-profile-osgi-application-visualvm/index.html", "/posts/2010/07/tip-profile-osgi-application-visualvm.html"], ["2010/07/integrate-play-framework-intellij-idea/index.html", "/posts/2010/07/integrate-play-framework-intellij-idea.html"], ["2010/03/mock-objects-easymock/index.html", "/posts/2010/03/mock-objects-easymock.html"], ["2010/07/intellij-idea-10-eap-is-here/index.html", "/posts/2010/07/intellij-idea-10-eap-is-here.html"], ["2012/05/advanced-compiler-design-and-implementation-book-review/index.html", "/posts/2012/05/advanced-compiler-design-and-implementation-book-review.html"], ["2010/04/jtheque-problems-migrating-osgi/index.html", "/posts/2010/04/jtheque-problems-migrating-osgi.html"], ["2014/02/budgetwarrior-0-3-0-objective-wish-management/index.html", "/posts/2014/02/budgetwarrior-0-3-0-objective-wish-management.html"], ["2010/09/jdk-7-features-updated-plan-b-is-apparently-here/index.html", "/posts/2010/09/jdk-7-features-updated-plan-b-is-apparently-here.html"], ["2010/04/java-7-new-io-features-asynchronous-operations-multicasting-random-access-with-jsr-203-nio-2/index.html", "/posts/2010/04/java-7-new-io-features-asynchronous-operations-multicasting-random-access-with-jsr-203-nio-2.html"], ["2010/05/oracle-pushes-a-first-version-of-closures/index.html", "/posts/2010/05/oracle-pushes-a-first-version-of-closures.html"], ["2012/11/integer-linear-time-sorting-algorithms/index.html", "/posts/2012/11/integer-linear-time-sorting-algorithms.html"], ["2009/12/google-analytics-asynchronous/index.html", "/posts/2009/12/google-analytics-asynchronous.html"], ["2010/07/asynchronous-message-passing-jr/index.html", "/posts/2010/07/asynchronous-message-passing-jr.html"], ["2014/01/home-server-adventure-step-3/index.html", "/posts/2014/01/home-server-adventure-step-3.html"], ["2010/06/jr-operations-and-capabilities/index.html", "/posts/2010/06/jr-operations-and-capabilities.html"], ["2010/06/monitor-programming-in-jr/index.html", "/posts/2010/06/monitor-programming-in-jr.html"], ["2012/03/1717/index.html", "/stories/2012/03/1717.html"], ["publications/index.html", "/stories/publications.html"], ["2010/07/rendezvous-concurrency-jr/index.html", "/posts/2010/07/rendezvous-concurrency-jr.html"], ["2012/09/linux-symbolic-links-hard-links/index.html", "/posts/2012/09/linux-symbolic-links-hard-links.html"], ["2011/11/print-strings-integers-intel-assembly/index.html", "/posts/2011/11/print-strings-integers-intel-assembly.html"], ["2011/05/avoid-scrolling-problems-in-kile-when-using-gnome/index.html", "/posts/2011/05/avoid-scrolling-problems-in-kile-when-using-gnome.html"], ["2012/03/1725/index.html", "/stories/2012/03/1725.html"], ["2010/10/compute-command-line-arguments-with-apache-commons-cli/index.html", "/posts/2010/10/compute-command-line-arguments-with-apache-commons-cli.html"], ["2012/12/wordpress-plugin-google-visualization-charts/index.html", "/posts/2012/12/wordpress-plugin-google-visualization-charts.html"], ["2010/05/evernote-a-very-smart-note-book/index.html", "/posts/2010/05/evernote-a-very-smart-note-book.html"], ["2012/09/cmake-compile-latex-documents/index.html", "/posts/2012/09/cmake-compile-latex-documents.html"], ["2010/08/generate-graphs-benchmarks-easily/index.html", "/posts/2010/08/generate-graphs-benchmarks-easily.html"], ["2012/06/eddi-compiler-1-0-1-pointers-better-struct-support/index.html", "/posts/2012/06/eddi-compiler-1-0-1-pointers-better-struct-support.html"], ["2010/01/install-jr-windows/index.html", "/posts/2010/01/install-jr-windows.html"], ["2011/09/profile-c-application-with-callgrind-kcachegrind/index.html", "/posts/2011/09/profile-c-application-with-callgrind-kcachegrind.html"], ["2012/03/cpp11-concurrency-part1-start-threads/index.html", "/posts/2012/03/cpp11-concurrency-part1-start-threads.html"], ["2010/04/closest-pair-of-point-plane-sweep-algorithm/index.html", "/posts/2010/04/closest-pair-of-point-plane-sweep-algorithm.html"], ["2012/11/eddic-compiler-1-1-4-graph-coloring-register-allocation/index.html", "/posts/2012/11/eddic-compiler-1-1-4-graph-coloring-register-allocation.html"], ["2011/06/write-and-read-binary-files-in-c/index.html", "/posts/2011/06/write-and-read-binary-files-in-c.html"], ["2010/04/links-of-the-week-3/index.html", "/posts/2010/04/links-of-the-week-3.html"], ["2012/03/1718/index.html", "/stories/2012/03/1718.html"], ["2012/07/eddi-compiler-1-1-0-member-functions/index.html", "/posts/2012/07/eddi-compiler-1-1-0-member-functions.html"], ["2012/07/manage-command-line-boost-program-options/index.html", "/posts/2012/07/manage-command-line-boost-program-options.html"], ["2010/03/nio-2-path-api-java-7/index.html", "/posts/2010/03/nio-2-path-api-java-7.html"], ["2012/09/back-in-berkeley-california/index.html", "/posts/2012/09/back-in-berkeley-california.html"], ["2010/05/java-7-add-public-defender-methods-to-java-interfaces/index.html", "/posts/2010/05/java-7-add-public-defender-methods-to-java-interfaces.html"], ["2012/02/eddic-0-8-1-do-while-loop-and-better-optimization/index.html", "/posts/2012/02/eddic-0-8-1-do-while-loop-and-better-optimization.html"], ["2011/07/profile-applications-linux-perf-tools/index.html", "/posts/2011/07/profile-applications-linux-perf-tools.html"], ["2011/11/eddic-0-5-1-better-assembly-generation-and-faster-parsing/index.html", "/posts/2011/11/eddic-0-5-1-better-assembly-generation-and-faster-parsing.html"], ["2012/08/algorithms-books-reviews/index.html", "/posts/2012/08/algorithms-books-reviews.html"], ["2010/07/tip-how-to-solve-agent-admitted-failure-to-sign-using-the-key-error/index.html", "/posts/2010/07/tip-how-to-solve-agent-admitted-failure-to-sign-using-the-key-error.html"], ["2010/01/jr-introduction/index.html", "/posts/2010/01/jr-introduction.html"], ["2010/02/java-keywords/index.html", "/posts/2010/02/java-keywords.html"], ["2011/07/java-7-has-been-released/index.html", "/posts/2011/07/java-7-has-been-released.html"], ["2012/06/eddic-1-0-structures-global-optimizations/index.html", "/posts/2012/06/eddic-1-0-structures-global-optimizations.html"], ["2010/09/the-pragmatic-programmer-book-review/index.html", "/posts/2010/09/the-pragmatic-programmer-book-review.html"], ["2010/07/effective-java-second-edition-book-review/index.html", "/posts/2010/07/effective-java-second-edition-book-review.html"], ["2010/05/15-years-birthday-of-java-a-bit-late/index.html", "/posts/2010/05/15-years-birthday-of-java-a-bit-late.html"], ["2010/07/jr-virtual-machines/index.html", "/posts/2010/07/jr-virtual-machines.html"], ["2011/10/diploma-thesis-inlining-assistance-for-large-scale-object-oriented-applications/index.html", "/posts/2011/10/diploma-thesis-inlining-assistance-for-large-scale-object-oriented-applications.html"], ["2011/11/boost-intrusive_ptr/index.html", "/posts/2011/11/boost-intrusive_ptr.html"], ["2010/05/java-concurrency-part-1-threads/index.html", "/posts/2010/05/java-concurrency-part-1-threads.html"], ["2010/09/java-concurrency-part-7-executors-and-thread-pools/index.html", "/posts/2010/09/java-concurrency-part-7-executors-and-thread-pools.html"], ["2011/06/no-more-ads-on-the-site/index.html", "/posts/2011/06/no-more-ads-on-the-site.html"], ["2011/06/eddi-0-2-types-and-variables/index.html", "/posts/2011/06/eddi-0-2-types-and-variables.html"], ["2012/01/boost-enable_if-handle-ambiguous-function-overload-void/index.html", "/posts/2012/01/boost-enable_if-handle-ambiguous-function-overload-void.html"], ["2013/12/new-hobby-project-thor-os-64bit-operating-system-c/index.html", "/posts/2013/12/new-hobby-project-thor-os-64bit-operating-system-c.html"], ["2012/03/1722/index.html", "/stories/2012/03/1722.html"], ["2012/07/eddi-compiler-1-0-3-inlining-register-allocation/index.html", "/posts/2012/07/eddi-compiler-1-0-3-inlining-register-allocation.html"], ["2011/06/book-review-accelerated-cpp/index.html", "/posts/2011/06/book-review-accelerated-cpp.html"], ["2010/08/a-website-for-jtheque/index.html", "/posts/2010/08/a-website-for-jtheque.html"], ["2010/07/java-se-6-update-21-released/index.html", "/posts/2010/07/java-se-6-update-21-released.html"], ["2012/08/eddi-compiler-1-1-2-read-command-line/index.html", "/posts/2012/08/eddi-compiler-1-1-2-read-command-line.html"], ["2009/12/swing-user-interface-jtable/index.html", "/posts/2009/12/swing-user-interface-jtable.html"], ["2010/05/develop-a-modular-application-implementation/index.html", "/posts/2010/05/develop-a-modular-application-implementation.html"], ["2011/06/upload-files-to-ftp-using-bash/index.html", "/posts/2011/06/upload-files-to-ftp-using-bash.html"], ["2010/07/discover-java-visualvm-1-3/index.html", "/posts/2010/07/discover-java-visualvm-1-3.html"], ["2010/03/hardware-guide-memory/index.html", "/posts/2010/03/hardware-guide-memory.html"], ["2012/07/eddi-compiler-1-0-2-better-pointer-support-new-optimizations/index.html", "/posts/2012/07/eddi-compiler-1-0-2-better-pointer-support-new-optimizations.html"], ["2012/12/cmake-rerun-last-failed-tests-ctest/index.html", "/posts/2012/12/cmake-rerun-last-failed-tests-ctest.html"], ["2010/05/better-exception-handling-in-java-7-multicatch-and-final-rethrow/index.html", "/posts/2010/05/better-exception-handling-in-java-7-multicatch-and-final-rethrow.html"], ["2012/02/eddic-0-8-64bit-generation/index.html", "/posts/2012/02/eddic-0-8-64bit-generation.html"], ["2012/11/cmakelatex-1-0-2-nomenclature-filters/index.html", "/posts/2012/11/cmakelatex-1-0-2-nomenclature-filters.html"], ["2010/03/welcome-to-my-new-website/index.html", "/posts/2010/03/welcome-to-my-new-website.html"], ["2010/04/java-7-more-concurrency/index.html", "/posts/2010/04/java-7-more-concurrency.html"], ["2010/07/osgi-spring-dynamic-modules-hello-world/index.html", "/posts/2010/07/osgi-spring-dynamic-modules-hello-world.html"], ["2012/07/c11-concurrency-tutorial-part-4-atomic-type/index.html", "/posts/2012/07/c11-concurrency-tutorial-part-4-atomic-type.html"], ["2010/07/getting-started-play-framework/index.html", "/posts/2010/07/getting-started-play-framework.html"], ["2011/09/book-review-more-effective-c/index.html", "/posts/2011/09/book-review-more-effective-c.html"], ["2011/11/eddi-compiler-0-6-1/index.html", "/posts/2011/11/eddi-compiler-0-6-1.html"], ["2012/02/assembly-language-step-by-step-book-review/index.html", "/posts/2012/02/assembly-language-step-by-step-book-review.html"], ["2011/11/cpp-templates-complete-guide-book/index.html", "/posts/2011/11/cpp-templates-complete-guide-book.html"], ["2010/04/ubuntu-lucid-lynx-10-04/index.html", "/posts/2010/04/ubuntu-lucid-lynx-10-04.html"], ["2010/06/jtheque-is-migrating-to-git/index.html", "/posts/2010/06/jtheque-is-migrating-to-git.html"], ["donate/index.html", "/stories/donate.html"], ["2010/05/improve-performance-builds-maven-cli-plugin/index.html", "/posts/2010/05/improve-performance-builds-maven-cli-plugin.html"], ["2010/04/java-7-the-new-java-util-objects-class/index.html", "/posts/2010/04/java-7-the-new-java-util-objects-class.html"], ["2010/04/passed-scjp-exam/index.html", "/posts/2010/04/passed-scjp-exam.html"], ["2012/07/taskwarrior-php-frontend-0-1/index.html", "/posts/2012/07/taskwarrior-php-frontend-0-1.html"], ["2013/07/why-how-left-windows-for-linux/index.html", "/posts/2013/07/why-how-left-windows-for-linux.html"], ["legal/index.html", "/stories/legal.html"], ["2012/03/1723/index.html", "/stories/2012/03/1723.html"], ["2010/05/improve-performances-wordpress-w3-total-cache/index.html", "/posts/2010/05/improve-performances-wordpress-w3-total-cache.html"], ["2009/12/jtheque-movies-1-0/index.html", "/posts/2009/12/jtheque-movies-1-0.html"], ["2010/08/java-concurrency-in-practice-book-review/index.html", "/posts/2010/08/java-concurrency-in-practice-book-review.html"], ["contact/index.html", "/stories/contact.html"], ["2010/03/osgi-and-cyclic-dependencies/index.html", "/posts/2010/03/osgi-and-cyclic-dependencies.html"], ["2011/06/introduce-variables-on-eddi/index.html", "/posts/2011/06/introduce-variables-on-eddi.html"], ["2012/04/c11-concurrency-tutorial-advanced-locking-and-condition-variables/index.html", "/posts/2012/04/c11-concurrency-tutorial-advanced-locking-and-condition-variables.html"], ["2013/12/zabbix-low-level-discovery-cores-cpus-hard-disk/index.html", "/posts/2013/12/zabbix-low-level-discovery-cores-cpus-hard-disk.html"], ["2010/09/tip-batch-resize-images-on-ubuntu-linux/index.html", "/posts/2010/09/tip-batch-resize-images-on-ubuntu-linux.html"], ["2012/12/cpp-benchmark-std-list-boost-intrusive-list/index.html", "/posts/2012/12/cpp-benchmark-std-list-boost-intrusive-list.html"], ["2010/05/first-build-jtheque-sonar-2-0/index.html", "/posts/2010/05/first-build-jtheque-sonar-2-0.html"], ["2012/07/c11-synchronization-benchmark/index.html", "/posts/2012/07/c11-synchronization-benchmark.html"], ["about/index.html", "/stories/about.html"], ["2012/11/cpp-benchmark-vector-vs-list/index.html", "/posts/2012/11/cpp-benchmark-vector-vs-list.html"], ["2012/02/eddic-0-7-1-boolean-operators/index.html", "/posts/2012/02/eddic-0-7-1-boolean-operators.html"], ["2010/05/tip-add-resources-dynamically-to-a-classloader/index.html", "/posts/2010/05/tip-add-resources-dynamically-to-a-classloader.html"], ["2010/08/java-concurrency-part-4-semaphores/index.html", "/posts/2010/08/java-concurrency-part-4-semaphores.html"], ["2012/02/local-optimization-on-three-address-code/index.html", "/posts/2012/02/local-optimization-on-three-address-code.html"], ["2012/03/1728/index.html", "/stories/2012/03/1728.html"], ["2011/10/install-git-flow-linux/index.html", "/posts/2011/10/install-git-flow-linux.html"], ["2009/12/improve-performance-web-site/index.html", "/posts/2009/12/improve-performance-web-site.html"], ["2010/08/file-copy-benchmark-updates-once-again/index.html", "/posts/2010/08/file-copy-benchmark-updates-once-again.html"], ["2012/12/eddic-1-2-0-single-inheritance-copy-constructor/index.html", "/posts/2012/12/eddic-1-2-0-single-inheritance-copy-constructor.html"], ["2011/07/eddi-0-3-branches-conditions/index.html", "/posts/2011/07/eddi-0-3-branches-conditions.html"], ["2012/08/jelastic-java-host-recommended-james-gosling/index.html", "/posts/2012/08/jelastic-java-host-recommended-james-gosling.html"], ["2012/03/eddic-0-9-1-enhanced-floating-point-support/index.html", "/posts/2012/03/eddic-0-9-1-enhanced-floating-point-support.html"], ["2011/06/git-tip-restore-a-deleted-tag/index.html", "/posts/2011/06/git-tip-restore-a-deleted-tag.html"], ["2010/07/replace-an-old-copyright-by-a-new-one/index.html", "/posts/2010/07/replace-an-old-copyright-by-a-new-one.html"], ["2010/04/write-corrects-benchmarks/index.html", "/posts/2010/04/write-corrects-benchmarks.html"], ["2012/03/enhanced-code-snippets-syntaxhighlighter-evolved/index.html", "/posts/2012/03/enhanced-code-snippets-syntaxhighlighter-evolved.html"], ["2013/08/norco-rpc-230-case-review/index.html", "/posts/2013/08/norco-rpc-230-case-review.html"], ["2010/04/substance-6-0-is-out/index.html", "/posts/2010/04/substance-6-0-is-out.html"], ["2011/10/effective-stl-book-review/index.html", "/posts/2011/10/effective-stl-book-review.html"], ["2010/09/my-java-benchmarks-on-github/index.html", "/posts/2010/09/my-java-benchmarks-on-github.html"], ["2012/03/1720/index.html", "/stories/2012/03/1720.html"], ["2010/03/bookmarks-bar-disappears-google-chrome/index.html", "/posts/2010/03/bookmarks-bar-disappears-google-chrome.html"], ["2012/07/eddi-compiler-1-1-1-dynamic-memory-allocation-constructors-destructors/index.html", "/posts/2012/07/eddi-compiler-1-1-1-dynamic-memory-allocation-constructors-destructors.html"], ["2009/12/intellij-idea-9-review/index.html", "/posts/2009/12/intellij-idea-9-review.html"], ["2011/11/eddi-compiler-0-6-0-arrays/index.html", "/posts/2011/11/eddi-compiler-0-6-0-arrays.html"], ["2012/03/1721/index.html", "/stories/2012/03/1721.html"], ["2010/08/java-7-try-with-resources-statement/index.html", "/posts/2010/08/java-7-try-with-resources-statement.html"], ["2010/03/jtheque-is-going-to-osgi/index.html", "/posts/2010/03/jtheque-is-going-to-osgi.html"], ["2013/08/home-server-adventure-step-2/index.html", "/posts/2013/08/home-server-adventure-step-2.html"], ["2012/03/1719/index.html", "/stories/2012/03/1719.html"], ["2010/04/links-of-the-week-2/index.html", "/posts/2010/04/links-of-the-week-2.html"], ["2011/08/compute-metrics-of-c-project-using-cccc/index.html", "/posts/2011/08/compute-metrics-of-c-project-using-cccc.html"], ["2012/12/christmas-offer-buy-packt-publishing-ebooks/index.html", "/posts/2012/12/christmas-offer-buy-packt-publishing-ebooks.html"], ["2011/01/using-linq-to-query-sharepoint-lists/index.html", "/posts/2011/01/using-linq-to-query-sharepoint-lists.html"], ["2010/04/java-links-of-the-week/index.html", "/posts/2010/04/java-links-of-the-week.html"], ["2010/04/java-7-more-dynamics/index.html", "/posts/2010/04/java-7-more-dynamics.html"], ["2012/04/install-valgrind-on-gentoo-linux/index.html", "/posts/2012/04/install-valgrind-on-gentoo-linux.html"], ["2011/11/boost-1-48-0-has-been-released/index.html", "/posts/2011/11/boost-1-48-0-has-been-released.html"], ["2011/12/moodle-promotion-on-packt-publishing-books/index.html", "/posts/2011/12/moodle-promotion-on-packt-publishing-books.html"], ["2011/11/linux-mint-12-lisa-released/index.html", "/posts/2011/11/linux-mint-12-lisa-released.html"], ["2010/02/hardware-guide-hard-disks/index.html", "/posts/2010/02/hardware-guide-hard-disks.html"], ["2011/06/install-specific-version-gcc-ubuntu/index.html", "/posts/2011/06/install-specific-version-gcc-ubuntu.html"], ["2010/03/bundle-non-osgi-dependencies-maven/index.html", "/posts/2010/03/bundle-non-osgi-dependencies-maven.html"], ["2010/09/a-better-swingworker/index.html", "/posts/2010/09/a-better-swingworker.html"], ["2012/01/install-cinnamon-linux-mint/index.html", "/posts/2012/01/install-cinnamon-linux-mint.html"], ["2010/09/java-7-delays-and-plan-b/index.html", "/posts/2010/09/java-7-delays-and-plan-b.html"], ["2011/06/this-website-is-now-running-wordpress-3-1-3/index.html", "/posts/2011/06/this-website-is-now-running-wordpress-3-1-3.html"], ["2013/10/budgetwarrior-0-2-visual-reports-fortune-status-expenses-aggregates/index.html", "/posts/2013/10/budgetwarrior-0-2-visual-reports-fortune-status-expenses-aggregates.html"], ["2010/05/develop-a-modular-application-bases/index.html", "/posts/2010/05/develop-a-modular-application-bases.html"], ["2012/04/linux-kernel-tip-do-not-disable-system-v-ipc-for-x-org-and-chrome/index.html", "/posts/2012/04/linux-kernel-tip-do-not-disable-system-v-ipc-for-x-org-and-chrome.html"], ["eddi-compiler-eddic/index.html", "/stories/eddi-compiler-eddic.html"], ["2010/08/do-not-use-relative-path-with-logback/index.html", "/posts/2010/08/do-not-use-relative-path-with-logback.html"], ["2013/08/budgetwarrior-command-line-personal-budgeting/index.html", "/posts/2013/08/budgetwarrior-command-line-personal-budgeting.html"], ["2010/06/wordpress-3-0-installed/index.html", "/posts/2010/06/wordpress-3-0-installed.html"], ["2010/06/java-7-translucency-shaped-windows/index.html", "/posts/2010/06/java-7-translucency-shaped-windows.html"], ["2010/05/sonar-2-1-has-been-released/index.html", "/posts/2010/05/sonar-2-1-has-been-released.html"], ["2012/10/run-boost-test-parallel-cmake/index.html", "/posts/2012/10/run-boost-test-parallel-cmake.html"], ["2010/07/tip-optimize-images-on-ubuntu-linux/index.html", "/posts/2010/07/tip-optimize-images-on-ubuntu-linux.html"], ["jtheque-project/index.html", "/stories/jtheque-project.html"],["tag/algorithm/index.html", "/categories/algorithm.html"],["tag/apache/index.html", "/categories/apache.html"],["tag/assembly/index.html", "/categories/assembly.html"],["tag/benchmark/index.html", "/categories/benchmark.html"],["tag/benchmarks/index.html", "/categories/benchmarks.html"],["tag/books/index.html", "/categories/books.html"],["tag/boost/index.html", "/categories/boost.html"],["tag/budgetwarrior/index.html", "/categories/budgetwarrior.html"],["tag/cpp/index.html", "/categories/cpp.html"],["tag/cpp11/index.html", "/categories/cpp11.html"],["tag/clang/index.html", "/categories/clang.html"],["tag/closures/index.html", "/categories/closures.html"],["tag/cmake/index.html", "/categories/cmake.html"],["tag/compilers/index.html", "/categories/compilers.html"],["tag/conception/index.html", "/categories/conception.html"],["tag/concurrency/index.html", "/categories/concurrency.html"],["tag/eddi/index.html", "/categories/eddi.html"],["tag/gcc/index.html", "/categories/gcc.html"],["tag/gentoo/index.html", "/categories/gentoo.html"],["tag/git/index.html", "/categories/git.html"],["tag/google/index.html", "/categories/google.html"],["tag/hardware/index.html", "/categories/hardware.html"],["tag/io/index.html", "/categories/io.html"],["tag/intel/index.html", "/categories/intel.html"],["tag/intellij-idea/index.html", "/categories/intellij-idea.html"],["tag/java/index.html", "/categories/java.html"],["tag/java-7/index.html", "/categories/java-7.html"],["tag/jr/index.html", "/categories/jr.html"],["tag/jtheque/index.html", "/categories/jtheque.html"],["tag/latex/index.html", "/categories/latex.html"],["tag/libraries/index.html", "/categories/libraries.html"],["tag/links/index.html", "/categories/links.html"],["tag/linux/index.html", "/categories/linux.html"],["tag/machine-learning/index.html", "/categories/machine-learning.html"],["tag/maven/index.html", "/categories/maven.html"],["tag/mint/index.html", "/categories/mint.html"],["tag/modular/index.html", "/categories/modular.html"],["tag/network/index.html", "/categories/network.html"],["tag/optimization/index.html", "/categories/performances.html"],["tag/osdev/index.html", "/categories/osdev.html"],["tag/osgi/index.html", "/categories/osgi.html"],["tag/performances/index.html", "/categories/performances.html"],["tag/personal/index.html", "/categories/personal.html"],["tag/php/index.html", "/categories/php.html"],["tag/play/index.html", "/categories/play.html"],["tag/projects/index.html", "/categories/projects.html"],["tag/prolog/index.html", "/categories/prolog.html"],["tag/promotion/index.html", "/categories/promotion.html"],["tag/releases/index.html", "/categories/releases.html"],["tag/review/index.html", "/categories/review.html"],["tag/seo/index.html", "/categories/seo.html"],["tag/server/index.html", "/categories/server.html"],["tag/sharepoint-2010/index.html", "/categories/sharepoint.html"],["tag/sonar/index.html", "/categories/sonar.html"],["tag/spring/index.html", "/categories/spring.html"],["tag/swing/index.html", "/categories/swing.html"],["tag/templates/index.html", "/categories/templates.html"],["tag/tests/index.html", "/categories/tests.html"],["tag/the-site/index.html", "/categories/the-site.html"],["tag/thor/index.html", "/categories/thor.html"],["tag/tips/index.html", "/categories/tips.html"],["tag/tools/index.html", "/categories/tools.html"],["tag/ubuntu/index.html", "/categories/linux.html"],["tag/visual-studio-2010/index.html", "/categories/visual-studio.html"],["tag/web/index.html", "/categories/web.html"],["tag/windows/index.html", "/categories/windows.html"],["tag/wordpress/index.html", "/categories/wordpress.html"],["tag/zabbix/index.html", "/categories/zabbix.html"], ["series/cpp11-concurrency-tutorial/index.html", "/categories/concurrency.html"],["series/develop-modular-application/index.html", "/categories/modular.html"],["series/java-concurrency-tutorial/index.html", "/categories/concurrency.html"],["hardware/index.html", "/categories/hardware.html"], ["linux/index.html","/categories/linux.html"], ["linux/gentoo/index.html","/categories/gentoo.html"], ["linux/mint/index.html","/categories/linux.html"], ["linux/ubuntu/index.html","/categories/linux.html"], ["others.html","/categories/others.html"], ["others/home-server/index.html","/categories/home-server.html"], ["programming/index.html","/categories/programming.html"], ["programming/assembly/index.html","/categories/assembly.html"], ["programming/c-cpp/index.html","/categories/cpp.html"], ["programming/c-cpp/eddi/index.html", "/categories/eddi.html"], ["programming/compilers/index.html", "/categories/compilers.html"],["programming/java/index.html", "categories/java.html"],["programming/java/jtheque/index.html","/categories/jtheque.html"],["programming/java/swing/index.html","/categories/swing.html"],["programming/operating-systems/index.html","/categories/osdev.html"],["programming/web/index.html","/categories/web.html"],["programming/web/sharepoint/index.html","/categories/sharepoint.html"],["feed/index.html", "/rss.xml"]]






# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola install_plugin ping`).
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
OUTPUT_FOLDER = 'target'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'


# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
# GALLERY_PATH = "galleries"
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to 'old posts, page %d' or 'page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
# INDEXES_TITLE = ""         # If this is empty, defaults to BLOG_TITLE
# INDEXES_PAGES = ""         # If this is empty, defaults to '[old posts,] page %d' (see above)
# INDEXES_PAGES_MAIN = False # If True, INDEXES_PAGES is also displayed on
                             # the main (the newest) index page (index.html)

# Name of the theme to use.
THEME = "wicht"

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

INDEX_TEASERS = True
FEED_TEASERS = True
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
FEED_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="padding-left:5px;border-width:0" src="/assets/img/cc.png" /></a>"""

# A small copyright notice for the page footer (in HTML).
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year,
                                       license=LICENSE)

# Disqus comments

COMMENT_SYSTEM = "disqus"
COMMENT_SYSTEM_ID = "blogwichtounet"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
# STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
# PRETTY_URLS = False

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False
# If True, schedules post to today if possible, even if scheduled hour is over
# SCHEDULE_FORCE_TODAY = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuracion you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What MarkDown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
SOCIAL_BUTTONS_CODE = ""

# Hide link to source for the posts?
# HIDE_SOURCELINK = False
# Copy the source files for your pages?
# Setting it to False implies HIDE_SOURCELINK = True
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# Local Search with tipue

ENABLED_EXTRAS = ['local_search']

# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
EXTRA_HEAD_DATA = """
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-2175227-7']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
"""

# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (eg. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use W3C-DTF Format (ex. 2012-03-30T23:00:00+02:00)
#
TIMEZONE = 'Europe/Zurich'

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Experimental plugins - use at your own risk.
# They probably need some manual adjustments - please see their respective
# readme.
# ENABLED_EXTRAS = [
#     'planetoid',
#     'ipynb',
#     'local_search',
#     'render_mustache',
# ]

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# You can configure the logging handlers installed as plugins or change the
# log level of the default stdout handler.
LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'WARNING', 'bubble': True},
    #'smtp': {
    #    'from_addr': 'test-errors@example.com',
    #    'recipients': ('test@example.com'),
    #    'credentials':('testusername', 'password'),
    #    'server_addr': ('127.0.0.1', 25),
    #    'secure': (),
    #    'level': 'DEBUG',
    #    'bubble': True
    #}
}

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}
