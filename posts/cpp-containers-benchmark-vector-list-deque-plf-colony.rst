Write your post here.


All the examples are compiled with g++-4.9.4 and run on a Gentoo Linux machine
with an Intel Core i7-4770 at 3.4GHz.


Here are direct links to all benchmarks:

* `Fill`_ Benchmark
* `Emplace`_ Benchmark
* `Fill Front`_ Benchmark
* `Linear Search`_ Benchmark
* `Iterate and modify`_ Benchmark
* `Number Crunching`_ Benchmark
* `Sort`_ Benchmark
* `Destruction`_ Benchmark

Fill
****

Let's start with the most obvious benchmark, insertion. A series of elements
will be inserted at the back of the container. Vector and colony both have
a reserve function that is able to preallocate memory for the necessary
elements. For both containers, both the standard version without reserve and the
version with reserve are benchmarked.

Since colony is unordered, this test is using insert in place of push_back.

.. raw:: html

    <div id="graph_fill_back___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_fill_back___Trivial_8_" type="button" value="Logarithmic scale">

For a very small data type, the results are very clear, the vector with reserve
is the winner, directly followed by the deque. After this, almost three times
slower is the colony and vector without pre-allocation. Interestingly, reserve
on the colony container does not help at all. And finally, the list is the
slowest container. The fact that the deque is faster than the vector (without
reserve) is logical since the deque will not have to move all its elements after
a reallocation.

With a type of 32bytes, the results are almost the same with less margin, let's
see with something bigger:

.. raw:: html

    <div id="graph_fill_back___Trivial_128_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_fill_back___Trivial_128_" type="button" value="Logarithmic scale">

This time, the vector without reserve() is clearly the slowest and we can two
plateaus which are corresponding to the levels of cache. The fastest is now the
deque almost on par with the vector preallocated. The colony and the list are
now at the same speed.

.. raw:: html

    <div id="graph_fill_back___Trivial_4096_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_fill_back___Trivial_4096_" type="button" value="Logarithmic scale">

With a large data type (4096 bytes), the list becomes the fastest, followed by
the deque and a bit slower the colony versions and vector_reserve.

Let's see with a non-trivial type that is costly to copy but fast to move:

.. raw:: html

    <div id="graph_fill_back___NonTrivialStringMovable" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_fill_back___NonTrivialStringMovable" type="button" value="Logarithmic scale">

The vector and the deque are able to take good advantage of the move and are the
fastest here. Even the vector without pre allocations is faring quite well here.

Let's see if there is a difference with noexcept on the move operation:

.. raw:: html

    <div id="graph_fill_back___NonTrivialStringMovableNoExcept" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_fill_back___NonTrivialStringMovableNoExcept" type="button" value="Logarithmic scale">

There is in fact a significant difference for the vector with pre allocation,
that is 20% faster than with the previous version.  Indeed, since it knows that
the operation cannot throw it can use a faster path for reallocation and still
guarantees it's exception safety.

Overall, for insertions, the vector and deque are the fastest for small types
and the list is the fastest for the very large types. colony offers a medium
performance on this bencmark but is quite stable for different data types. When
you know the size of the collection, you should always use reserve() on vectors.
Moreover, if you can use noexcept operations, you should always do it since it
can significantly speedup the vector performance.

Emplace
*******

The next operation is very similar to the first except that we use emplace
insertions instead of pushes.

.. raw:: html

    <div id="graph_emplace_back___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_emplace_back___Trivial_8_" type="button" value="Logarithmic scale">

As expected, there is no difference between push_back and emplace_back for
trivial types. The preallocated vector is the fastest container, followed by the
deque and then significantly slower are the colony and vector without
preallocation.

.. raw:: html

    <div id="graph_emplace_back___NonTrivialStringMovable" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_emplace_back___NonTrivialStringMovable" type="button" value="Logarithmic scale">

However, here is a very large difference between the push version and the
emplace version. Indeed, it is much slower. This may seem hard to believe that
emplace is slower than normal insert since it should at least as fast, and
sometimes faster. This in fact due to the version of GCC that is still using
Copy-On-Write for string. Therefore, the previous version was much faster
because the copies were not done since the string was not modified and this
saved a lot of time in that case. However, this is an artificial case since
a collection filled of all the same string is not highly likely in practice.
Generally, I think it's better to use Small-String-Optimization than
Copy-On-Write and now COW is not allowed by the standard anymore in C++11.

Overall, for the tested types, emplace should have exactly the same performance
as normal push_back. Except for the special case of COW for GCC that should not
happen anymore if you use a recent compiler and C++11.

Fill Front
**********

The next benchmark is again a fill benchmark but elements are inserted at the
front of the container. Since colony is unordered, it's removed from the
benchmark. This benchmark is mostly used because this is the worst case for
vector.

.. raw:: html

    <div id="graph_fill_front___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_fill_front___Trivial_8_" type="button" value="Logarithmic scale">

As expected, the vector is terribly slower than the deque and list containers,
by almost three orders of magnitude. As before, the deque is much faster than
the list.

If you really need a collection that offers performance for front and back
insertions, you should definitely prefer the deque over the vector. The list
should only be preferred for very large data types.

Linear Search
*************

The next operation is that is tested is the search. The container is filled with
all the numbers in [0, N] and shuffled. Then, each number in [0,N] is searched
in the container with std::find that performs a simple linear search.  In
theory, all the data structures should perform the same if we only consider
their complexity.

.. raw:: html

    <div id="graph_linear_search___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_linear_search___Trivial_8_" type="button" value="Logarithmic scale">

The differences between the different data structures are very important. The
list is about 8 times slower than the vector container. The deque is slightly
slower than the vector. Interestingly, the colony container is even 50% slower
than the list container.

This is simply due to the much better data locality of the vector and deque
compared to the list. The list is in fact a terrible data structure for data
locality. Every time the next element needs to be accessed, it is necessary to
jump from memory positions to memory positions. Since the processor will always
load a full cache line, several elements of the vector will be loaded in memory
at once and the next few loads will directly reading from the cache rather than
from the main memory. In the case of the list, this does not help since elements
are not contiguous. It means that all the time will be wasted with cache misses.
The vector is even faster than the deque because all elements are contiguous
whereas in a deque, only packs of elements are contiguous.

.. raw:: html

    <div id="graph_linear_search___Trivial_128_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_linear_search___Trivial_128_" type="button" value="Logarithmic scale">

For a bigger data type (128 bytes), the differences are smaller. The list is
only three times slower than the vector and deque which are about at the same
speed. The colony is now significantly faster than the list, but still much
slower than vector and deque.

.. raw:: html

    <div id="graph_linear_search___Trivial_4096_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_linear_search___Trivial_4096_" type="button" value="Logarithmic scale">

For a large data type (4KB), the list is still twice slower than the other
containers. For such big data, the colony is now the fastest data type, followed
by the deque and vector.

Overall, the speed of linear searching through a data structure is mostly
limited by the data locality of the container. For this reason, the deque and
vector containers are significantly faster than the list. Interestingly, the
colony container becomes faster than the other containers for large data types.
Overall, a list should never be used if the container is to be searched a lot.

Iterate and modify
******************

The next test iterates over the entire collection and increment each number
contained inside it. It uses the begin and end iterators for each container. The
time should be mostly dominated by the iteration time.

.. raw:: html

    <div id="graph_write___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_write___Trivial_8_" type="button" value="Logarithmic scale">

As expected, the list is the slowest of the container for that sort of
operations and the vector is the fastest. The deque is slightly slower than the
vector and the colony slightly faster than the list. There is a 6 times
difference between the best result, which is pretty significant.

.. raw:: html

    <div id="graph_write___Trivial_32_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_write___Trivial_32_" type="button" value="Logarithmic scale">

As the data type size augments, the deque starts to gets slightly better than
the vector and the colony starts to get much better than the list, but still not
on par with the other containers.

.. raw:: html

    <div id="graph_write___Trivial_128_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_write___Trivial_128_" type="button" value="Logarithmic scale">

Once increased to 128B, the colony really starts to get interesting being the
fastest with the deque depending on the number of elements.

.. raw:: html

    <div id="graph_write___Trivial_4096_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_write___Trivial_4096_" type="button" value="Logarithmic scale">

Interestingly, with very large data types (4KB), the vector takes the lead
again, very close to the colony and the deque a bit behind.

Overall, one thing is clear, the list is really bad for iteration. The colony
container starts to shine when the size of the data type is around 128B, but
does not provide a very significant speedup. The vector is generally the fastest
for this kind of workload.

Number Crunching
****************

The next test is about numbers. Random numbers are inserted into the container
so that it is kept sorted. That means that a linear search will be performed to
find the insertion point. Since colony is unordered, it is excluded from this
benchmark. In practice, vector and deque could use binary search contrary to the
list.

Let's see the result with a number of 8 bytes:

.. raw:: html

    <div id="graph_number_crunching___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_number_crunching___Trivial_8_" type="button" value="Logarithmic scale">

The results are quite clear. The list is more than 20 times slower and than the
vector and the deque. This is because this benchmark is driven more by iterations than
by modifications of the structure and therefore the vector and deque are much
faster at this. Vector is still faster than the deque for its slightly better
locality.

If we take elements of 32 bytes:

.. raw:: html

    <div id="graph_number_crunching___Trivial_32_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_number_crunching___Trivial_32_" type="button" value="Logarithmic scale">

The list is *only* 8 times slower than the vector and deque. There is no doubt
that the difference would be even slower as the size of the elements grows.
Nevertheless, since we are talking about number crunching, this is rarely with
bigger numbers.

Overall, for such a load, the vector and deque structures are shining because of
their excellent iteration performance compared to the poor performance of the
list. Moreover, keep into account that in practice this would be done using
binary search for the vector and deque, probably meaning faster time for them
(even though binary search is not cache-efficient).

Sort
****

Let's see how the different collections are efficient at being sorted. For
list and colony, the sort member function is used while the other are using
std::sort directly. Moreover, since the colony offers two different sort
methods, both where tested. The first is using std::sort internally and the
second is using a timsort algorithm.

Let's start with a very small type:

.. raw:: html

    <div id="graph_sort___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_sort___Trivial_8_" type="button" value="Logarithmic scale">

The vector is the fastest container here, closely followed by the deque. colony
is about twice slower, with the timsort being slightly slowest. The list is
about 8 times slower than the vector.

.. raw:: html

    <div id="graph_sort___Trivial_128_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_sort___Trivial_128_" type="button" value="Logarithmic scale">

For a bigger data type, the differences are smaller between the containers. The
vector is still the fastest, but only 2.3 times faster than the list.
Interestingly, the timsort is now faster than the standard sort algorithm.

.. raw:: html

    <div id="graph_sort___Trivial_4096_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_sort___Trivial_4096_" type="button" value="Logarithmic scale">

For a really big data type, the list becomes the fastest container. The vector
and deque containers now the slowest containers. The colony is significantly
faster than the vector on this data type but still twice slower than the list.

Overall, sorting a vector and deque is generally faster than a list unless the
data type gets too big (>1KB). Again, the colony container is in a sort of
middle ground with very stable performance for both large and small data types
but is never the fastest on this benchmark.

Destruction
***********

The last test that is done is used to measure the time necessary to delete
a container. The containers are dynamically allocated, filled with n numbers,
and then their destruction time (via delete) is computed. This is probably never
a bottleneck in practice, but this is still interesting to benchmark in my
opinion.

.. raw:: html

    <div id="graph_destruction___Trivial_8_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_destruction___Trivial_8_" type="button" value="Logarithmic scale">

As you can see, the differences between the benchmarks are very significant. The
list is 10'000 times slower than the vector, the colony is 2000 slower than it
and even the deque is 200 times slower than the vector. The deallocation of
a vector, for trivial type, is simply a memory deallocation so its speed purely
depends on the speed on deallocating memory which is very fast on modern
systems.  The other containers need to deallocate all the small pieces they have
allocated. Not only does that mean more deallocations but especially means
walking through most of the elements.

.. raw:: html

    <div id="graph_destruction___Trivial_128_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_destruction___Trivial_128_" type="button" value="Logarithmic scale">

For a larger data type, the results are changing significantly. The overhead of
the deque is going up very quickly. This is actually normal each of the blocks
of the deque are actually very few elements and therefore it becomes very close
to a list in terms of deallocation and memory walks. What is very interesting
here is that colony actually is going on par with the vector and sometimes
slower than it. This shows that very deallocations are not necessary slower than
several smaller deallocations. Moreover, this also shows that colony is
especially good when the data type starts to become important.

.. raw:: html

    <div id="graph_destruction___Trivial_4096_" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_destruction___Trivial_4096_" type="button" value="Logarithmic scale">

For a very large data type, the vector and the colony are the fastest
collection, followed by the deque and list, only 1.8 times slower. This shows
that at this point, the deque makes as much allocations than the list.

.. raw:: html

    <div id="graph_destruction___NonTrivialStringMovable" style="width: 700px; height: 400px;"></div>
    <input id="graph_button_destruction___NonTrivialStringMovable" type="button" value="Logarithmic scale">

For a non-trivial type, every collection has to go through each element and
calls the necessary destructor. Therefore, the time is mostly related to the
iteration time. This puts the list on the bottom and the three other containers
at almost the same time.

Overall, the destruction of a vector for trivial types is significantly faster
than the other collections, unless the data type becomes very big. Colony has
a large overhead for small types but becomes interesting for large data types.
The list is always a poor contender since it needs to walk through all elements
in order to deallocate each node. Interestingly, the deque has more and more
overhead as the data type grows since each block will be able to hold less and
elements and therefore resembles a list. When types are non-trivial, the time
for destruction is generally tied to the time necessary to walk through the
entire collection and calls each of the destructor.

Conclusion
**********

TODO





.. raw:: html

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">google.load('visualization', '1.0', {'packages':['corechart']});</script>

    <script type="text/javascript">
    function draw_destruction___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['100000', 240, 22, 988, 0],
    ['200000', 485, 45, 1963, 0],
    ['300000', 707, 96, 2996, 0],
    ['400000', 962, 100, 4004, 0],
    ['500000', 1197, 114, 4989, 0],
    ['600000', 1425, 138, 5986, 0],
    ['700000', 1683, 214, 6967, 0],
    ['800000', 1902, 189, 7985, 0],
    ['900000', 2138, 263, 9532, 0],
    ['1000000', 2409, 244, 10874, 0],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_destruction___Trivial_8_'));
    var options = {curveType: "function",title: "destruction - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_destruction___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_destruction___Trivial_128_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['100000', 251, 798, 2504, 0],
    ['200000', 499, 1952, 5396, 0],
    ['300000', 740, 3088, 8595, 1361],
    ['400000', 1003, 4120, 12363, 1850],
    ['500000', 1240, 5138, 15873, 2151],
    ['600000', 1513, 6857, 19100, 2798],
    ['700000', 4926, 7974, 22711, 4032],
    ['800000', 5581, 9172, 28014, 4692],
    ['900000', 6750, 10813, 32839, 5626],
    ['1000000', 7523, 16168, 38987, 6070],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_destruction___Trivial_128_'));
    var options = {curveType: "function",title: "destruction - Trivial<128>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_destruction___Trivial_128_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_destruction___Trivial_4096_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['100000', 23042, 27594, 26377, 20120],
    ['200000', 41537, 56241, 55568, 40759],
    ['300000', 56177, 82809, 79245, 53583],
    ['400000', 70974, 101075, 102419, 68183],
    ['500000', 85402, 125446, 124540, 83074],
    ['600000', 105598, 149797, 153420, 98360],
    ['700000', 114786, 169089, 171255, 111156],
    ['800000', 125951, 189993, 193192, 125769],
    ['900000', 134245, 211323, 212633, 137547],
    ['1000000', 146530, 227040, 228934, 145069],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_destruction___Trivial_4096_'));
    var options = {curveType: "function",title: "destruction - Trivial<4096>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_destruction___Trivial_4096_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_destruction___NonTrivialStringMovable(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['100000', 251, 230, 1129, 247],
    ['200000', 503, 452, 2682, 453],
    ['300000', 755, 684, 3699, 685],
    ['400000', 1018, 930, 5477, 910],
    ['500000', 1281, 1208, 6278, 1157],
    ['600000', 1551, 1502, 7664, 1411],
    ['700000', 1813, 1789, 8733, 1799],
    ['800000', 2089, 2126, 9732, 1821],
    ['900000', 2347, 2442, 11301, 2053],
    ['1000000', 2672, 2786, 12209, 2369],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_destruction___NonTrivialStringMovable'));
    var options = {curveType: "function",title: "destruction - NonTrivialStringMovable",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_destruction___NonTrivialStringMovable');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_fill_back___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 535, 201, 538, 984, 1649, 576],
    ['200000', 1088, 403, 1070, 478, 3160, 1163],
    ['300000', 1636, 603, 1607, 723, 4683, 2136],
    ['400000', 2188, 805, 2146, 956, 6220, 2397],
    ['500000', 2729, 1005, 2705, 1204, 7713, 2879],
    ['600000', 3226, 1207, 3219, 1440, 9317, 4423],
    ['700000', 3773, 1410, 3755, 1685, 10740, 4689],
    ['800000', 4316, 1615, 4310, 1925, 12251, 4941],
    ['900000', 4875, 1990, 4944, 2169, 13778, 5277],
    ['1000000', 5375, 2038, 5448, 2399, 15261, 5709],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_fill_back___Trivial_8_'));
    var options = {curveType: "function",title: "fill_back - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_fill_back___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_fill_back___Trivial_128_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 2041, 1527, 2081, 1860, 2884, 3210],
    ['200000', 4047, 3027, 4264, 3981, 5731, 10844],
    ['300000', 6199, 8223, 6373, 6101, 8796, 25019],
    ['400000', 8535, 10836, 8330, 8189, 11999, 27840],
    ['500000', 10407, 13427, 10295, 10384, 14704, 30540],
    ['600000', 22272, 16100, 22151, 12553, 17410, 56066],
    ['700000', 27628, 18803, 27632, 14555, 20499, 58845],
    ['800000', 32652, 21560, 31797, 16561, 31093, 61622],
    ['900000', 36216, 24302, 35956, 18872, 37265, 64702],
    ['1000000', 40885, 27145, 40172, 27008, 42010, 67174],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_fill_back___Trivial_128_'));
    var options = {curveType: "function",title: "fill_back - Trivial<128>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_fill_back___Trivial_128_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_fill_back___Trivial_4096_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 99291, 99165, 93745, 78083, 71280, 275150],
    ['200000', 189371, 195877, 191438, 161087, 151216, 555444],
    ['300000', 295924, 292906, 289069, 244678, 230150, 1015704],
    ['400000', 383938, 390134, 386876, 326803, 309189, 1114123],
    ['500000', 491567, 487224, 484430, 411020, 388064, 1211597],
    ['600000', 582054, 584361, 583918, 494356, 467153, 2029733],
    ['700000', 691463, 680920, 680137, 577437, 546012, 2128923],
    ['800000', 779796, 779300, 779129, 660831, 625425, 2225308],
    ['900000', 885591, 875187, 877538, 745724, 704473, 2323835],
    ['1000000', 980793, 974700, 976187, 829563, 783075, 2421730],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_fill_back___Trivial_4096_'));
    var options = {curveType: "function",title: "fill_back - Trivial<4096>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_fill_back___Trivial_4096_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_fill_back___NonTrivialStringMovable(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 792, 389, 793, 1385, 1882, 1101],
    ['200000', 1593, 778, 1578, 1008, 3726, 2209],
    ['300000', 2376, 1169, 2378, 1514, 5552, 4153],
    ['400000', 3235, 1561, 3174, 2018, 7423, 4577],
    ['500000', 4001, 1957, 3983, 2541, 9248, 4981],
    ['600000', 4783, 2343, 5100, 3059, 11121, 9013],
    ['700000', 5594, 2735, 5589, 3575, 12977, 9101],
    ['800000', 6413, 3130, 6589, 4103, 15169, 9422],
    ['900000', 7218, 3520, 7258, 4654, 16637, 9815],
    ['1000000', 8007, 3920, 8027, 5175, 18506, 10240],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_fill_back___NonTrivialStringMovable'));
    var options = {curveType: "function",title: "fill_back - NonTrivialStringMovable",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_fill_back___NonTrivialStringMovable');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_fill_back___NonTrivialStringMovableNoExcept(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 809, 388, 795, 1388, 1879, 798],
    ['200000', 1596, 781, 1601, 1021, 3733, 1633],
    ['300000', 2439, 1169, 2412, 1535, 5547, 3454],
    ['400000', 3185, 1556, 3248, 2065, 7394, 3612],
    ['500000', 4005, 1959, 4423, 2569, 9256, 4066],
    ['600000', 4784, 2342, 4825, 3109, 11113, 7052],
    ['700000', 5604, 2737, 5630, 3664, 13293, 7477],
    ['800000', 6373, 3133, 6434, 4176, 14889, 7910],
    ['900000', 7185, 3519, 7236, 4736, 16730, 8259],
    ['1000000', 7972, 3921, 8027, 5294, 18622, 8633],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_fill_back___NonTrivialStringMovableNoExcept'));
    var options = {curveType: "function",title: "fill_back - NonTrivialStringMovableNoExcept",animation: {duration:1200, easing:"in"},width: 600, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_fill_back___NonTrivialStringMovableNoExcept');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_emplace_back___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 536, 178, 540, 971, 1670, 552],
    ['200000', 1070, 355, 1137, 456, 3213, 1115],
    ['300000', 1604, 533, 1610, 687, 4821, 1992],
    ['400000', 2137, 714, 2141, 912, 6341, 2272],
    ['500000', 2679, 890, 2723, 1147, 7819, 2595],
    ['600000', 3211, 1068, 3275, 1379, 9335, 4353],
    ['700000', 3750, 1246, 3757, 1602, 10897, 4636],
    ['800000', 4311, 1434, 4295, 1830, 12424, 4889],
    ['900000', 4837, 1790, 4843, 2068, 13971, 5280],
    ['1000000', 5374, 1809, 5379, 2287, 15502, 5512],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_emplace_back___Trivial_8_'));
    var options = {curveType: "function",title: "emplace_back - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_emplace_back___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_emplace_back___NonTrivialStringMovable(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_reserve', 'vector_reserve', 'colony', 'deque', 'list', 'vector'],
    ['100000', 4159, 3570, 4086, 10340, 4814, 5123],
    ['200000', 8186, 7225, 8178, 7738, 9608, 11510],
    ['300000', 12298, 10813, 12332, 11211, 14397, 21432],
    ['400000', 16407, 14445, 16422, 14961, 19540, 25450],
    ['500000', 20514, 18773, 20546, 18721, 24529, 28862],
    ['600000', 25404, 21683, 24669, 24438, 29634, 47174],
    ['700000', 28747, 25332, 28905, 26207, 34165, 49175],
    ['800000', 32832, 30607, 32917, 29952, 39691, 52576],
    ['900000', 36932, 32551, 38905, 33771, 43919, 57070],
    ['1000000', 41068, 36322, 41128, 37491, 48958, 69685],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_emplace_back___NonTrivialStringMovable'));
    var options = {curveType: "function",title: "emplace_back - NonTrivialStringMovable",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_emplace_back___NonTrivialStringMovable');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_sort___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_timsort', 'colony', 'deque', 'list', 'vector'],
    ['100000', 11, 8, 6, 15, 5],
    ['200000', 24, 17, 13, 39, 11],
    ['300000', 38, 28, 21, 81, 18],
    ['400000', 52, 38, 28, 129, 24],
    ['500000', 67, 50, 36, 175, 32],
    ['600000', 83, 62, 43, 252, 37],
    ['700000', 102, 78, 51, 302, 45],
    ['800000', 120, 95, 60, 367, 52],
    ['900000', 139, 114, 68, 418, 59],
    ['1000000', 159, 132, 76, 473, 67],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_sort___Trivial_8_'));
    var options = {curveType: "function",title: "sort - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"ms"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_sort___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_sort___Trivial_128_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_timsort', 'colony', 'deque', 'list', 'vector'],
    ['100000', 21, 20, 17, 21, 14],
    ['200000', 48, 48, 38, 58, 31],
    ['300000', 77, 80, 61, 108, 50],
    ['400000', 108, 112, 84, 150, 69],
    ['500000', 146, 153, 107, 183, 88],
    ['600000', 181, 197, 137, 262, 114],
    ['700000', 215, 231, 161, 306, 134],
    ['800000', 248, 269, 183, 364, 153],
    ['900000', 283, 309, 212, 398, 177],
    ['1000000', 320, 347, 235, 447, 195],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_sort___Trivial_128_'));
    var options = {curveType: "function",title: "sort - Trivial<128>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"ms"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_sort___Trivial_128_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_sort___Trivial_4096_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony_timsort', 'colony', 'deque', 'list', 'vector'],
    ['100000', 172, 167, 380, 37, 368],
    ['200000', 345, 342, 812, 94, 792],
    ['300000', 519, 518, 1269, 172, 1237],
    ['400000', 697, 695, 1749, 238, 1696],
    ['500000', 879, 883, 2221, 297, 2175],
    ['600000', 1058, 1099, 2680, 419, 2616],
    ['700000', 1239, 1287, 3182, 489, 3128],
    ['800000', 1424, 1485, 3687, 569, 3610],
    ['900000', 1611, 1706, 4182, 637, 4089],
    ['1000000', 1795, 1834, 4712, 718, 4616],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_sort___Trivial_4096_'));
    var options = {curveType: "function",title: "sort - Trivial<4096>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"ms"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_sort___Trivial_4096_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_fill_front___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'deque', 'list', 'vector'],
    ['10000', 103, 164, 10808],
    ['20000', 45, 317, 47462],
    ['30000', 68, 468, 112331],
    ['40000', 91, 671, 208569],
    ['50000', 113, 864, 337059],
    ['60000', 138, 1056, 505252],
    ['70000', 161, 1067, 705592],
    ['80000', 184, 1370, 930767],
    ['90000', 207, 1374, 1192495],
    ['100000', 230, 1531, 1482277],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_fill_front___Trivial_8_'));
    var options = {curveType: "function",title: "fill_front - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_fill_front___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_linear_search___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['1000', 1225, 194, 594, 115],
    ['2000', 4837, 808, 2963, 417],
    ['3000', 10802, 1706, 7022, 923],
    ['4000', 19162, 3009, 12493, 1641],
    ['5000', 29970, 4812, 19916, 2681],
    ['6000', 42972, 6694, 28622, 4024],
    ['7000', 58487, 9108, 38993, 5602],
    ['8000', 76267, 11886, 51254, 7461],
    ['9000', 96459, 15073, 64857, 9535],
    ['10000', 118988, 18544, 80483, 11880],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_linear_search___Trivial_8_'));
    var options = {curveType: "function",title: "linear_search - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_linear_search___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_linear_search___Trivial_128_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['1000', 1290, 314, 1699, 316],
    ['2000', 5223, 1578, 7973, 1640],
    ['3000', 11864, 4445, 19918, 5136],
    ['4000', 21161, 9900, 37173, 10354],
    ['5000', 33118, 17371, 59245, 17496],
    ['6000', 47625, 26720, 85888, 26406],
    ['7000', 64734, 37500, 118073, 36900],
    ['8000', 84493, 50223, 153380, 49153],
    ['9000', 106670, 64512, 197568, 62828],
    ['10000', 131667, 80432, 244541, 78244],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_linear_search___Trivial_128_'));
    var options = {curveType: "function",title: "linear_search - Trivial<128>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_linear_search___Trivial_128_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_linear_search___Trivial_4096_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['1000', 1388, 486, 4104, 773],
    ['2000', 11302, 9886, 18768, 10841],
    ['3000', 28771, 27352, 50864, 29040],
    ['4000', 53444, 52677, 103377, 55008],
    ['5000', 86680, 86373, 211490, 88483],
    ['6000', 126078, 128374, 266281, 130910],
    ['7000', 174497, 178375, 374968, 182652],
    ['8000', 235061, 236228, 570192, 244255],
    ['9000', 288774, 300379, 642628, 313213],
    ['10000', 358575, 373799, 801212, 389737],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_linear_search___Trivial_4096_'));
    var options = {curveType: "function",title: "linear_search - Trivial<4096>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_linear_search___Trivial_4096_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_write___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['10000', 23, 5, 24, 2],
    ['20000', 47, 11, 49, 5],
    ['30000', 71, 16, 73, 8],
    ['40000', 94, 22, 99, 13],
    ['50000', 118, 27, 123, 14],
    ['60000', 146, 33, 148, 17],
    ['70000', 165, 39, 173, 23],
    ['80000', 189, 45, 197, 23],
    ['90000', 214, 78, 223, 27],
    ['100000', 236, 56, 247, 38],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_write___Trivial_8_'));
    var options = {curveType: "function",title: "write - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_write___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_write___Trivial_32_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['10000', 24, 12, 38, 11],
    ['20000', 49, 25, 76, 23],
    ['30000', 74, 37, 113, 35],
    ['40000', 99, 51, 153, 57],
    ['50000', 124, 64, 191, 65],
    ['60000', 148, 76, 234, 75],
    ['70000', 173, 89, 271, 92],
    ['80000', 198, 102, 320, 104],
    ['90000', 223, 119, 384, 125],
    ['100000', 252, 136, 432, 146],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_write___Trivial_32_'));
    var options = {curveType: "function",title: "write - Trivial<32>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_write___Trivial_32_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_write___Trivial_128_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['10000', 28, 34, 58, 26],
    ['20000', 57, 59, 122, 59],
    ['30000', 100, 93, 240, 123],
    ['40000', 199, 170, 536, 329],
    ['50000', 314, 250, 797, 414],
    ['60000', 450, 319, 858, 509],
    ['70000', 585, 533, 1076, 565],
    ['80000', 577, 567, 1294, 664],
    ['90000', 668, 615, 1539, 781],
    ['100000', 780, 893, 1666, 971],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_write___Trivial_128_'));
    var options = {curveType: "function",title: "write - Trivial<128>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_write___Trivial_128_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_write___Trivial_4096_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'colony', 'deque', 'list', 'vector'],
    ['10000', 173, 197, 788, 163],
    ['20000', 345, 401, 1579, 338],
    ['30000', 523, 615, 2355, 506],
    ['40000', 705, 828, 3091, 686],
    ['50000', 876, 1026, 3967, 851],
    ['60000', 1054, 1218, 4764, 1027],
    ['70000', 1234, 1432, 5446, 1174],
    ['80000', 1407, 1623, 6260, 1395],
    ['90000', 1573, 1830, 7028, 1487],
    ['100000', 1761, 2041, 7763, 1660],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_write___Trivial_4096_'));
    var options = {curveType: "function",title: "write - Trivial<4096>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"us"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_write___Trivial_4096_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_number_crunching___Trivial_8_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'deque', 'list', 'vector'],
    ['10000', 14, 179, 10],
    ['20000', 58, 1021, 43],
    ['30000', 135, 2593, 102],
    ['40000', 251, 4897, 194],
    ['50000', 402, 7917, 330],
    ['60000', 606, 11595, 472],
    ['70000', 823, 15840, 655],
    ['80000', 1094, 21019, 873],
    ['90000', 1447, 26789, 1107],
    ['100000', 1763, 33428, 1379],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_number_crunching___Trivial_8_'));
    var options = {curveType: "function",title: "number_crunching - Trivial<8>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"ms"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_number_crunching___Trivial_8_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_number_crunching___Trivial_32_(){
    var data = google.visualization.arrayToDataTable([
    ['x', 'deque', 'list', 'vector'],
    ['10000', 37, 255, 36],
    ['20000', 170, 1262, 178],
    ['30000', 405, 2945, 425],
    ['40000', 736, 5383, 792],
    ['50000', 1159, 8546, 1236],
    ['60000', 1695, 12676, 1778],
    ['70000', 2319, 17857, 2417],
    ['80000', 3043, 23655, 3157],
    ['90000', 3872, 30960, 4013],
    ['100000', 4865, 40274, 5022],
    ]);
    var graph = new google.visualization.LineChart(document.getElementById('graph_number_crunching___Trivial_32_'));
    var options = {curveType: "function",title: "number_crunching - Trivial<32>",animation: {duration:1200, easing:"in"},width: 700, height: 400,hAxis: {title:"Number of elements", slantedText:true},vAxis: {viewWindow: {min:0}, title:"ms"}};
    graph.draw(data, options);
    var button = document.getElementById('graph_button_number_crunching___Trivial_32_');
    button.onclick = function(){
    if(options.vAxis.logScale){
    button.value="Logarithmic Scale";
    } else {
    button.value="Normal scale";
    }
    options.vAxis.logScale=!options.vAxis.logScale;
    graph.draw(data, options);
    };
    }
    function draw_all(){
    draw_fill_back___Trivial_8_();
    draw_fill_back___Trivial_128_();
    draw_fill_back___Trivial_4096_();
    draw_fill_back___NonTrivialStringMovable();
    draw_fill_back___NonTrivialStringMovableNoExcept();
    draw_emplace_back___Trivial_8_();
    draw_emplace_back___NonTrivialStringMovable();
    draw_fill_front___Trivial_8_();
    draw_linear_search___Trivial_8_();
    draw_linear_search___Trivial_128_();
    draw_linear_search___Trivial_4096_();
    draw_write___Trivial_8_();
    draw_write___Trivial_32_();
    draw_write___Trivial_128_();
    draw_write___Trivial_4096_();
    draw_sort___Trivial_8_();
    draw_sort___Trivial_128_();
    draw_sort___Trivial_4096_();
    draw_number_crunching___Trivial_8_();
    draw_number_crunching___Trivial_32_();
    draw_destruction___Trivial_8_();
    draw_destruction___Trivial_128_();
    draw_destruction___Trivial_4096_();
    draw_destruction___NonTrivialStringMovable();
    }
    google.setOnLoadCallback(draw_all);
    </script>
