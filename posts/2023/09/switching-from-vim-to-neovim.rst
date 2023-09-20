As mentioned in my last article, I am now using neovim instead of vim. I just wanted to comment shortly on this change.

I have been using vim as my IDE for many years now (more than 10 years at least). But at the beginning of the year,
I switched to neovim instead.

neovim is a fork of vim, so it is quite similar, but it has some very important differences. It started in 2015, after
a multithreading patch was rejected from vim. 

Here are some of the advantages:

* Very powerful Builtin Langauge Server Protocol (LSP)
* Faster startup
* Builtin LUA support (the configuration can be written entirely in LUA)
* Asynchronous tasks (was later added to vim)

A lot of things are compatible between both editors. When I started with neovim, I simply copied over my vim
configuration and started using neovim with only very minor changes.

But what really convinced me to keep using neovim was the LSP. This feature and the great plugins that make use of it
greatly simplify how to deeply integrate C++ into neovim. I am now taking advantage of the clang tooling to analyze C++
code on the fly. And I get great autocompletion as well. 

All of this is doable with vim as well, but the last time I tried with vim, it was a nightmware to configure. With the
help of (quite a few) plugins, I could setup automcompletion in a great way. This allows me to jump to declarations and
definitions very easily.

I am far from being a neovim expert, but I am very happy with this tool. It definitely makes my life easier for
configuring complex features, compared to vim.

If you are interested, you can find my neovim configuration in my `dotfiles repository<https://github.com/wichtounet/dotfiles>`. It's very fresh because it was previously saved on another place and was recently copied there. I plan to improve it and little by little rewrite it in LUA. There are still some experimental stuff and it could be improved significantly. But I am really happy with the features configured. 

What about you? What do you think of neovim?
