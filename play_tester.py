# import source code
from collections import Counter
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)



# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())
janes_data = clean_wave_2_data()
def get_most_watched_genre(janes_data):
    #     popular_genre = get_most_watched_genre(janes_data)

    # # Assert
    # assert popular_genre == "Fantasy"
    watched_genres = []
    for watched_list in janes_data.values():
        for i in range(len(watched_list)):
            watched_genres.append(watched_list[i]['genre'])
    # print(watched_genres)
    # most_watched_genre_dict = {}
    # for genre in watched_genres:
    #     print(genre)
    #     # most_watched_genre_dict[genre] += 1
    # print(most_watched_genre_dict)
    most_watched_genre = Counter(watched_genres).most_common(1)
    # print(most_watched_genre[0][0])

get_most_watched_genre(janes_data)

#print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())

# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())