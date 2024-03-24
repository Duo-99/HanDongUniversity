#1
items = [ 
    "Machu Picchu",
    "The Great Wall",
    "Taj Mahal",
    "Pyramids of Giza",
    "Eiffel Tower",
    "Statue of Liberty",
    "Angkor Wat",
    "The Colosseum",
    "Great Barrier Reef",
    "Santorini"
]

descriptions = [
    "Located in the Andes Mountains, Machu Picchu is an ancient Incan citadel dating back to the 15th century. It's renowned for its sophisticated dry-stone walls, stunning panoramic views, and mysterious history.",
    "One of the most iconic symbols of China, the Great Wall stretches over 13,000 miles across northern China. It was built over centuries to protect China from invasions and is a UNESCO World Heritage Site.",
    "Built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal, the Taj Mahal is a masterpiece of Mughal architecture. Its white marble domes and intricate carvings make it one of the most beautiful buildings in the world.",
    "The Pyramids of Giza, including the Great Pyramid of Khufu, are ancient monumental tombs built for the pharaohs. They stand as a testament to the ancient Egyptian civilization's architectural and engineering prowess.",
    "An iconic symbol of Paris, the Eiffel Tower was constructed for the 1889 World's Fair. Designed by Gustave Eiffel, it stands 1,063 feet tall and offers breathtaking views of the city.",
    "A gift from France to the United States, the Statue of Liberty stands on Liberty Island in New York Harbor. It symbolizes freedom and democracy and has welcomed immigrants to the United States for over a century.",
    "The largest religious monument in the world, Angkor Wat is a temple complex in Cambodia built in the 12th century by the Khmer Empire. It is renowned for its intricate carvings and stunning architecture.",
    "Located in Rome, the Colosseum is an ancient amphitheater built by the Roman Empire in the 1st century AD. It could hold up to 80,000 spectators and was used for gladiatorial contests and public spectacles.",
    "The Great Barrier Reef is the world's largest coral reef system, stretching over 1,400 miles off the coast of Queensland, Australia. It is home to a diverse array of marine life, including coral, fish, and sea turtles.",
    "Santorini is a volcanic island in the Aegean Sea known for its stunning sunsets, white-washed buildings, and crystal-clear waters. Its cliffside villages, including Oia and Fira, are world-famous for their beauty."
]


def print_detail(index):
    items_1 = [ 
    "Machu Picchu",
    "The Great Wall",
    "Taj Mahal",
    "Pyramids of Giza",
    "Eiffel Tower",
    "Statue of Liberty",
    "Angkor Wat",
    "The Colosseum",
    "Great Barrier Reef",
    "Santorini"
]
    descriptions_1 = [
    "Located in the Andes Mountains, Machu Picchu is an ancient Incan citadel dating back to the 15th century. It's renowned for its sophisticated dry-stone walls, stunning panoramic views, and mysterious history.",
    "One of the most iconic symbols of China, the Great Wall stretches over 13,000 miles across northern China. It was built over centuries to protect China from invasions and is a UNESCO World Heritage Site.",
    "Built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal, the Taj Mahal is a masterpiece of Mughal architecture. Its white marble domes and intricate carvings make it one of the most beautiful buildings in the world.",
    "The Pyramids of Giza, including the Great Pyramid of Khufu, are ancient monumental tombs built for the pharaohs. They stand as a testament to the ancient Egyptian civilization's architectural and engineering prowess.",
    "An iconic symbol of Paris, the Eiffel Tower was constructed for the 1889 World's Fair. Designed by Gustave Eiffel, it stands 1,063 feet tall and offers breathtaking views of the city.",
    "A gift from France to the United States, the Statue of Liberty stands on Liberty Island in New York Harbor. It symbolizes freedom and democracy and has welcomed immigrants to the United States for over a century.",
    "The largest religious monument in the world, Angkor Wat is a temple complex in Cambodia built in the 12th century by the Khmer Empire. It is renowned for its intricate carvings and stunning architecture.",
    "Located in Rome, the Colosseum is an ancient amphitheater built by the Roman Empire in the 1st century AD. It could hold up to 80,000 spectators and was used for gladiatorial contests and public spectacles.",
    "The Great Barrier Reef is the world's largest coral reef system, stretching over 1,400 miles off the coast of Queensland, Australia. It is home to a diverse array of marine life, including coral, fish, and sea turtles.",
    "Santorini is a volcanic island in the Aegean Sea known for its stunning sunsets, white-washed buildings, and crystal-clear waters. Its cliffside villages, including Oia and Fira, are world-famous for their beauty."
]
    if items_1[index] in items_1:
        print(f"{items_1[index]}")
        print(descriptions_1[index])
        print("\n")
    else:
        print("Wrong Input. The number should be between 1 to 10.\n")
    

while True:
    print("Here are 10-15 famous places in the world. These man-made landmarks and monuments are so well known because of their location or special architecture. We will introduce the some detail information of each place")
    print(" ")

    print("Here is world most famous places.")
    print("---------------------------------")

    for i in range(len(items)):
        print(f"{i+1}  {items[i]}")
    
    print("---------------------------------")
    name = input("Choose number for information that you wanna know : ")
    print(" ")

    if name.isdigit():
        name_as_int =  int(name)
        if 0 < name_as_int < 11:
            print_detail(name_as_int)
    else:
        print("Wrong Input. The number should be between 1 to 10.\n")
    
    terminate = input("Do you want to quit(y/n)? ").lower()
    print("")
    if terminate == 'y':
        n = 11
        for i in range(1,n):
            print("*"*i," Good Bye ","*"*(11-i))
        break
        


