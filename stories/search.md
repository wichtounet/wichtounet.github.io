<script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
<script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
<script type="text/javascript">
    $(document).ready(function() {
        $('#tipue_search_input').tipuesearch({
        'mode': 'json',
        'contentLocation': '/assets/js/tipuesearch_content.json',
        'showUrl': false
        });
        });
</script>
<div id="tipue_search_content"></div>