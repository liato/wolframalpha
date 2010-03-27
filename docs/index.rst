:mod:`wolframalpha` --- A python interface to WolframAlpha
==========================================================

..  module:: wolframalpha
    :synopsis: A python interface to WolframAlpha.


Retrieve text results from the computational knowledge engine
`Wolfram|Alpha <http://www.wolframalpha.com/>`_.

.. toctree::
   :maxdepth: 1

   changes
   todo

Installation and requirements
-----------------------------

Make sure you have a working Python installation (>= 2.5) and that
`lxml <http://codespeak.net/lxml/>`_ is installed. Download the latest version
of wolframalpha from `GitHub <http://github.com/liato/wolframalpha>`_ or
clone it using git.::

    git clone git://github.com/liato/wolframalpha.git
    cd wolframalpha
    python setup.py install


Usage
-----

The following classes are available in the he wolframalpha lib.

* :class:`WolframAlpha` --- Query `WolframAlpha <http://www.wolframalpha.com/>`__ and return all non graphical results.
* :class:`WolframAlphaResult` --- Contains the retrieved information.


A short example of retrieving and printing out information with wolframalpha::
    
    import wolframalpha
    
    query = wolframalpha.WolframAlpha('New York')
    print 'Found %d result sets:' % len(query.results)
    for rs in query.results:
        print rs.title
        print rs.result, '\n'
        

And the result::
    
    Input interpretation
    New York,United States 
    
    
    Populations
        city population    | 8.364 million people  (2008 estimate) (country rank: 1st) 
     urban area population |           17.8 million people  (2000 estimate)            
     metro area population |           19.01 million people  (2008 estimate)            
    
    
    Current local time
    7:03 pm EDT  |  Saturday, March 27, 2010 
    
    
    Current weather
    3 deg C  (wind chill: -1 deg C)  |  relative humidity: 41%  |  wind: 5 m/s  |  overcast 
    
    
    Approximate elevation
    10 m 
    
    
    Nearby cities
      Jersey City,New Jersey   |    13 km  (kilometers) west    |    241114 people     
         Newark,New Jersey     |    23 km  (kilometers) west    |    278980 people     
        Hempstead,New York     |    25 km  (kilometers) east    |    751276 people     
        Brookhaven,New York    |    82 km  (kilometers) east    |    472122 people     
     Philadelphia,Pennsylvania | 130 km  (kilometers) southwest | 1.447 million people  
    
    
    Counties
    Kings County, New York  (30.8%  of city population)  |  Queens County, New York  (27.8%  of city population)  |  New York County, New York  (19.2%  of city population)  |  Bronx County, New York  (16.6%  of city population)  |  Richmond County, New York  (5.5%  of city population) 
    
    
    Nicknames
    The Big Apple  |  The Concrete Jungle  |  The City That Never Sleeps  |  The Capital of the World  |  The Empire City  |  The City So Nice They Named It Twice  |  The City 


The WolframAlpha class
~~~~~~~~~~~~~~~

..  class:: WolframAlpha(query[, all = True])

    Create a new :class:`WolframAlpha` instance and retrieve the
    information for *query*.
 
    *query* should be an ASCII string or a unicode string. 
    
    If *all* is ``False`` wolframalpha will not retrieve all the result sets.
    Only the result sets that are found on the first page request are returned.
    
    **Class methods:**

    ..  method:: update
    
        Refresh the information.
       
       
    **Class attributes and example values:**

    ..  attribute:: results
    
        A list of :class:`WolframAlphaResults` objects containing the results.::
        
            [<WolframAlphaResult/'Input interpretation'>,
             <WolframAlphaResult/'Populations'>,
             <WolframAlphaResult/'Current local time'>,
             <WolframAlphaResult/'Current weather'>,
             <WolframAlphaResult/'Approximate elevation'>,
             <WolframAlphaResult/'Nearby cities'>,
             <WolframAlphaResult/'Counties'>,
             <WolframAlphaResult/'Nicknames'>]       
       


The WolframAlphaResult class
~~~~~~~~~~~~~~

..  class:: WolframAlphaResult(title, result, result_raw)

    
    Used by :class:`WolframAlpha` to store results.
       
    **Class attributes and example values:**

    ..  attribute:: title
    
        String with result sets title.::
        
            'Nearby cities'
       
       
    ..  attribute:: result
    
        A formated result String.::
        
            Jersey City,New Jersey   |    13 km  (kilometers) west    |    241114 people     
               Newark,New Jersey     |    23 km  (kilometers) west    |    278980 people     
              Hempstead,New York     |    25 km  (kilometers) east    |    751276 people     
              Brookhaven,New York    |    82 km  (kilometers) east    |    472122 people     
           Philadelphia,Pennsylvania | 130 km  (kilometers) southwest | 1.447 million people         
       
    ..  attribute:: result_raw
    
        String with the raw text result returned by WolframAlpha.::
        
            'Jersey City,New Jersey | 13 km  (kilometers) west | 241114 people\\nNewark,New Jersey | 23 km  (kilometers) west | 278980 people\\nHempstead,New York | 25 km  (kilometers) east | 751276 people\\nBrookhaven,New York | 82 km  (kilometers) east | 472122 people\\nPhiladelphia,Pennsylvania | 130 km  (kilometers) southwest | 1.447 million people'
       

License
-------

This project is released under the MIT License.::

    Copyright (c) 2010 liato
   
    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:
   
    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.
   
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

