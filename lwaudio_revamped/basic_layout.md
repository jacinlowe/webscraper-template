classes
    - product 
      - dataclass
      - method for changing the attribute names
      - attributes 
      - to_dict()
      - from_dict()
  
    - scraper
      - abc class
      - selenium scraper
      - regular scraper
  
  
    - website strategy
      - abc class
      - this will allow us to implement different webpages and build products from them
      - takes a scraper
      - init the scraper and gather all the links
      - returns a product at the end
    
      - aamp website
      - aigroup website
      - any others go here
  
    - product builder
      - takes a website strategy and builds the product from it
  
    - comparator
      - compares old data with new and updates accordingly
    
    - file manager
      - for loading and saving csv files
      - utf-8-sig

    - database connector
      - upload data to database
      - download data
      - update data
      - delete data
      - compare data and update it
      - to_csv file
      - from_csv file