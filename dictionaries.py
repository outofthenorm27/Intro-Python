# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------


# Create a dictionary to hold the actor's names.
# actors = {}


# Create a dictionary using the built-in function.
# actors = dict()



# A dictionary of an actor.
actors = {"name":"Tom Cruise"}
# print({actors["Tom Cruise"]})


# Add an actor to the dictionary with the key "name"
# and the value "Denzel Washington".
actors["name"] = "Denzel Washington"



# Print the actors dictionary.
# print(actors)

# Print only the actor.
# print(actors["name"])

# A list of actors
actors_list = [
    "Chadwick Boseman",
    "Denzel Washington",
    "The Rock",
    "Kevin Hart"]
# print(actors_list)
# print(actors)
# Overwrite the value, "Denzel Washington", with the list of actors.
actors["name"] = actors_list
# print(actors)
# A dictionary can contain multiple pairs of information
actress = {
    "name":["Angelia Jolie","Issa Raye"],
    "genre":["Action","Comedy"],
    "nationality":"USA"
    }

# print(actress)

# A dictionary can contain multiple types of information
film = {
    "title": "Interstellar",
    "revenues": {
        "US":360,
        "China":250,
        "UK":80
    }
}

print(film["title"])


# A dictionary can even contain another dictionary












