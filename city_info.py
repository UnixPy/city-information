# This is my soulition to the test at page 112. 6-11 cities.py

cities = {"oslo" :
            {
                "country" : "Norway",
                "population" : "681,067",
            },
          "new_york" :
            {
                "country" : "The USA",
                "population" : "18,804,000",
                "fact" : "A little over 8 million people live in New York City. \nThat means 1 in every 38 people in the United States call the city home.",
            },
          "sydney" :
            {
                "country" : "Australia",
                "population" : "4,925,987",
                "fact" : "More than half of Australia's top 100 companies have their headquarters in Sydney.",
            },
          }

for key, value in cities.items():
    print(f"information about {key.title()}:")
    
    population = value['population']
    country = value['country']
    fact = value['fact']
    
    print(f"{key.title()} is located in {country}") 
    print(f"The population of {key.title()} is: {population}")
    print(f"One fact about {key.title()} is that: {fact}")
    
    print("\n")