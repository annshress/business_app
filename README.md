### Requirements
* A user must be defined with at least 6 attributes.
* You need to have attributes of at least the following types: integer, string, float, boolean...
* There must be a table with many-to-one or many-to-many relation with users (e.g., books bought by users).
* This table must have some columns containing numerical data or categorical data.
* The application should have two pages. 
* Both pages should have a header, a navigation bar at the left side, and a footer.
* The first page should display a list of users in tabular format. The table must have 
    * sorting, (*click the username or profile age columns*)
    * filter and (*by username*)
    * pagination features. (*page number pagination*)
* Clicking a row in this table should navigate to the second page. 
* The second page should display some statistics about the user selected in the first page. 

* Examples of some statistics to be computed:
    * Average (e.g., average price of the books bought by the user)
    * Minimum (e.g. cheapest book bought by the user)
    * Maximum (e.g. most expensive book bought by the user)
    * Count (e.g. number of books bought by the user)
    * etc. (*most loved category by the user*)
    

**Auth**

username: aayu

password: adminadmin


**If using different database,** initialize with dummy data:

`python manage.py init_db`
