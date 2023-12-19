# webCrawler

1. Send request with input query -> parse returned HTML doc by the server ->  parse ( name, price, and rating for each product)

2. Pagination: store the links to following pages (not all the products fit in one page) in "not yet visited" queue

3. Add the current link to "visited pages".  Repeat from step 1 with url from que queue.

4. Continue until there are no more links in "not yet visited" queue.


# TO-DO

- [] modularize the code with functions
- [] reasure that you're not evaluating duplicates
- [] try out the same functionality with the async library in order to make async requests 
