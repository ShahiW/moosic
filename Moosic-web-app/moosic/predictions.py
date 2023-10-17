import pickle
import numpy as np


# dump dataframe here:
with open('df2.bin', 'rb') as f:
    df2 = pickle.load(f)


# print(df2.head())


def get_results(genre: str, mood: str): 
# Random choice
    moosic_randomN_idx = np.random.choice(
                                df2.index,
                                size = 5, #playlist_length,
                                replace= False #random n = 5
                                )
    # Filter
    recommended_moosic_playlist = df2[['track_id', 'track_name', 'artist_name']].iloc[moosic_randomN_idx]

    return recommended_moosic_playlist.to_dict('records')
    #print(recommended_moosic_playlist)

#get_results('recommended_moosic_playlist', 'metal', 'happy')