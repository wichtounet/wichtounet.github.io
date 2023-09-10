I am happy to announce the release of budgetwarrior 1.1.0.

The last release of budgetwarrior was more than 5 years ago. So, once I finished my C++20/C++23 refresh of the code,
I decided it was a good time to generate a new release. There has been many improvements in this new version:
* Many new graphs on the web interface
* Add support for tracking stock values
* Significant speed improvements if you have a lot of data in the tool
* Assets can be set as inactive to be hidden
* Introduction of the FI Net Worth
* Better support of asset classes
* Many small bug fixes

If you want to use the latest version, you can now use the docker image that I am publishing frequently. This docker
image is what I use, so it should be fairly up-to-date.
* `budgetwarrior on docker hub <https://hub.docker.com/r/wichtounet/budgetwarrior>`

Otherwise, you can of course compile it from the sources (another docker image is available as a build image). For this,
you will need a very recent GCC (13+) or Clang (16+) compiler.

Most of the new features have been implemented a while ago, for my personal usage. The main recent changes are
improvements in the code, related to using C++20 and C++23. I plan for all my projects to be compiled with C++23 by
default. The reason is mostly so I can really learn about these features, since I cannot use them all at work. On that
note, I was a bit disappointed by the support in clang, especially in libc++. I had to work around a few limitations in
order to support clang.

The main C++20 feature that I am using in budgetwarrior is ranges. I have been able to improve many pieces of code from
using loops and multiple ifs, to using a range. I have implemented many transforms and filters for budgetwarrior. And
I am quite happy about the result. For instance:

.. code:: cpp

	bool budget::account_exists(const std::string& name){
		for(auto& account : all_accounts()){
			if(account.name == name){
				return true;
			}
		}

		return false;
	}

became:

.. code:: cpp

	bool budget::account_exists(const std::string& name){
		return !ranges::empty(all_accounts() | filter_by_name(name));
	}

or here is another example of using ranges:

.. code:: cpp

   if (accounts.data() | not_id(id) | active_today | filter_by_name(account.name)) {
       throw budget_exception("There is already an account with the name " + account.name);
   }

This is likely the biggest change, but I have made other improvements based on recent versions of C++:
* Use of std::format
* Use of the spaceship operator
* Use of template lambdas
* Use of std::string_view
* Use of std::filesystem
* Use of std::map::contains (and other such functions)

Overall, it was a lot of fun and I could significantly improve the code by using these new features (and more).

I am also taking advantage of clang-tidy now. I have added a clang-tidy configuration to my projects so that I can
quickly check everything. I have also integrated clang-tidy in neovim (yes, I switched from vim to neovim, more on that
later maybe) and this shows in real time where I could improve the code.

Finally, another change is that I am now taking advantage of Github Workflows. Every time I push to the repo, everything is
compiled with the two compilers I support. This allows me to keep compatibility between both. In the future, I plan to
add a few more tools to the workflows for code analysis. This is also an opportunity for me to learn about these
workflows, which I never used before.

I am quite glad to be working on these projects again eve though I do not have much time. It was really fun to use all
these new features in budgetwarrior. Next, I plan to refresh the code of ETL. And since I want to refresh my GPU skills
as well, I will also work on etl_gpu_blas.
