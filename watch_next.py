import spacy
nlp = spacy.load('en_core_web_md')

with open("movies.txt", "r") as file:
    lines = [line.split(":") for line in file]    

#funcion check_similarity takes in a sentance and uses nlp to compare it a list of arrays of names and sentances
#It looks for the most similar sentance in the second position of the array and returns the first posion of the
#array of the highest similarity
def check_similarity(sentance_to_compare, lines):
    store_similarity = 0
    store_movie = ""

    for line in lines:
        model_sentance = nlp(sentance_to_compare)
        similarity = nlp(line[1]).similarity(model_sentance)
        if (similarity > store_similarity):
            store_similarity = similarity
            store_movie = line[0]

    return(store_movie)   
  
    
sentance_to_compare = "Will he save the world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planer where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar wher he is sold into slavery and trained as gladiator"

print(f"Based on your previous selection we recommend you watch {check_similarity(sentance_to_compare,lines)}")