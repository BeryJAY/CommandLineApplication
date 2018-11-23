import requests
#making the introduction of the application
banner = "Trending stories is a news application that displays a list containing four news sources and gives a user a chance to select any preferred source.After the selection is made, another list of the top 10 headlines is displayed whereby each has a a title, description and  URL in case the user wishes to follow up"
print(banner)

sources = []


print('\n')
def list_of_sources():
        """
        displays the list of the first four sources of news
        """
        url = ('https://newsapi.org/v2/sources?apiKey=24224cf967964be8b4c5476c1c8f5f42')
        response = requests.get(url).json()
        # bringing back the sources from data that has been collected
        data = response["sources"]
        

        for g in data:
                sources.append(g['id'])
            
        for m in sources[0:4]:
                print(m)

def make_choice():
    """
    prompts the user to make a choice from the displayed list of sources and then displays the headlines.
    """

    choosing = input("Kindly enter the choice you have made:")
    is_choosing_wrong = choosing not in sources
    while is_choosing_wrong:
        choosing = input("Wrong choice!!, kindly choose from the list above:")
        is_choosing_wrong = choosing not in sources
        
        
    if choosing not in sources:
        print("")
    headline_url = ('https://newsapi.org/v2/top-headlines?apiKey=24224cf967964be8b4c5476c1c8f5f42&sources=' + choosing)
    response1 = requests.get(headline_url).json()
    check = response1["status"]
    if check == "ok":
        data1 = response1['articles']
        print(len(data1))
        for headline in data1[:11]:
            print("\n")
            print("TITLE: " + headline["title"])
            print("DESCRIPTION: " + headline["description"])
            print("THE LINK TO FOLLOW: " + headline["url"])
    elif check == "error":
            print("There is an error")
    else:
            print("something went wrong")

   



if __name__ == "__main__":
     list_of_sources()
     make_choice()
    


 