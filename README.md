# ISL web
Inclined Line Simulator Web is a web adaptation of existing implementation.

# Changes to standard implementation
- added async wrapper for async processing
- wrapped in Django framework
    
# Available sites
- `/` - which is entry point, as well as data input
- `/show` - used to present results
    
# Usage
One must run Django projects. Then hit index site of newly created server.
After data entry, server redirect user to site with results. As computation 
finish temporary site will be replaced by proper charts. Same as in previous
version, animated gif with entire simulation will apear as first
    
# Known bugs
- Refreshing `/show` site when simulation is in place, cause show of partial
previous results, e.g. gif animation 
