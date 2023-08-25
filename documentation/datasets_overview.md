# Metadata of potential datasets

---

## 1.  __Spotify Dataset 600k Tracks ([kaggle link](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks)):__


> Dataset of over 600,000 tracks  from 1921 to 2020,  detailing the audio features of the tracks and also containing the popularity metrics of 1 million artists and more.


### Data Overview

| feature column | description | data type  |
|:--------:|:------------------------:| :--------------:| 
| id  | what is the track id? |  object  |
| name | what is the name of song (track)? |   object |
| popularity  | how popular is the track (0 -100)? |  int64|
| duration_ms | length of track (ms) | int64 |
| explicit     |   does it contain explicit lyrical content? |  int64  | 
| artists     |    what is the name of artist(s)? | object | 
|  id_artists    |  what is the  artists id?  | object | 
|  release_date  |   what was the date of realease for track? | object | 
|  danceability   |  can one dance to the track? | float64 | 
|  energy         |   does the track have a certain level of intensity? | float64 | 
| key            |  what is the key (pitch?) of the track? |  int64   | 
|  loudness    |    how loud (in dB) is the track? | float64 | 
|  mode           |   modality (major or minor) |  int64  | 
|  speechiness      | are there spoken words (lyrics) in the track? |  float64 | 
| acousticness    |  a measure of how acoustic a track is |  float64 | 
| instrumentalness | does the track contain only beats/ intrumentals? |  float64 | 
| liveness        |  was the track performed infront of a live audience? |  float64 | 
|  valence         |  what is the mood of the track?  |  float64 | 
| tempo           |  what is the speed of the track? |  float64 | 
|  time_signature  |  how many beats per bar? |  int64   | 


<br>


## 2.  __Spotify Tracks Dataset ([kaggle link](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)):__


> Similar to the Spotify 600k+ Dataset, contains over 125 genres


### Data Overview

| feature column | description | data type  |
|:--------:|:------------------------:| :--------------:| 
| track_id  | The Spotify ID for the track |  object  |
| artists     |    The artists' names who performed the track. If there is more than one artist, they are separated by a ; | object | 
| album_name     |    The album name in which the track appears | object | 
| track_name | Name of the track |   object |
| popularity  | The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are. Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. |  int64|
| duration_ms | The track length in milliseconds | int64 |
| explicit     |   Whether or not the track has explicit lyrics (true = yes it does; false = no it does not OR unknown) |  int64  | 
|  danceability   |  Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable| float64 | 
|  energy         |    Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale | float64 | 
| key            |  The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1 |  int64   | 
|  loudness    |    The overall loudness of a track in decibels (dB) | float64 | 
|  mode           |   Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0 |  int64  | 
|  speechiness      | Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks|  float64 | 
| acousticness    | A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic |  float64 | 
| instrumentalness | Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content |  float64 | 
| liveness        |  Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live |  float64 | 
|  valence         |  A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry) |  float64 | 
| tempo           |  The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration |  float64 | 
|  time_signature  |  An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of 3/4, to 7/4. |  int64   | 
|  track_genre    |  The genre in which the track belongs  | object | 


<br>



## 3.  __Emotion Labeled Spotify Songs - 278k ([kaggle link](https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset)):__


> Moodify dataset containing 278,000 songs from spotify for classifying songs based on lyrical and musical features as well as emotions. All songs are labeled with emotions


### Data Overview

| feature column | description | data type  |
|:--------:|:------------------------:| :--------------:| 
| labels  | {'sad': 0, 'happy': 1, 'energetic': 2, 'calm': 3} |  object  |
| acousticness    |  A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. |  float64 | 
|  danceability   |  Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. | float64 | 
|  energy         |   Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. | float64 | 
| instrumentalness | Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. |  float64 | 
| liveness        |  Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides a strong likelihood that the track is live. |  float64 | 
|  loudness    |    he overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing the relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db. | float64 | 
|  speechiness      | Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audiobook, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. |  float64 | 
|  valence         |  A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). |  float64 | 
| tempo           |  The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, the tempo is the speed or pace of a given piece and derives directly from the average beat duration. |  float64 | 


<br>

## 4.  __Spotify User Behaviour Dataset ([kaggle link](https://www.kaggle.com/datasets/meeraajayakumar/spotify-user-behavior-dataset)):__


> Similar to the Spotify 600k+ Dataset, contains over 125 genres


### Data Overview

| feature column | description | data type  |
|:--------:|:------------------------:| :--------------:| 
| age  | Age group of user? |  int  |
| gender | Gender of user? |   object |
|spotify_usage_period  | How long have you been using Spotify? |  --|
| spotify_listening_device | Which of the following devices do you primarily use to listen to Spotify? | -- |
| spotify_subscription_plan     |   Which Spotify subscription plan do you currently have? |  --  | 
| premium_sub_willingness     |    Are you willing to take a premium subscription or willing to continue with premium subscription in future? | -- | 
|  preffered_premium_plan    |  If premium or willing to take premium, what amount do you pay for the subscription?| -- | 
|  preferred_listening_content  |   What do you prefer to listen more? | -- | 
|  fav_music_genre   |  What genre(s) of music do you enjoy the most? | -- | 
|  music_time_slot         |   What is your favourite time slot to listen to music?| -- | 
| music_Influencial_mood           |  When it comes to listening to music, which of the following moods or situations most strongly influences your choice of music? |  --   | 
|  music_lis_frequency    |    When do you listen to music more often? | -- | 
|  music_expl_method           |   How do you discover new music on Spotify? |  -- | 
|  music_recc_rating      | How do you rate the spotify music recommendations? |  -- | 
| pod_lis_frequency    | How often do you listen to Podcast? |  -- | 
| fav_pod_genre | What genre(s) of Podcast do you enjoy the most? |  -- | 
| preffered_pod_format        |  What podcast format you generally prefer? |  -- | 
|  pod_host_preference         |  Are you more inclined to listen to podcasts from unknown personalities, or do you prefer podcasts hosted by well-known individuals? |  -- | 
| preffered_pod_duration           |  Do you prefer shorter podcast episodes (under 30 minutes) or longer episodes (over 30 minutes) |  -- | 
|  pod_variety_satisfaction  |  Are you satisfied with the variety and availability of podcasts on Spotify? |  --   | 


<br>


## 5.  __Billboard Top 100 ([kaggle link](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs)):__


> Billboard Top 100


### Data Overview - TBD

| feature column | description | data type  |
|:--------:|:------------------------:| :--------------:| 
| date  | date | --   |
| rank | billboard ranking |   -- |
|song  | name of song |  --|
| artist | name of artist(s) | -- |
| last-week     |    ranking based on previous week | -- | 
|  peak-rank    |  highest rank ever gotten | -- | 
|  weeks-on-board  |   number of weeks it has been on billboard | -- | 

<br>



## 6.  __Music Artist Popularity ([kaggle link](https://www.kaggle.com/datasets/pieca111/music-artists-popularity)):__


> Music Artist Popularity


### Data Overview - TBD

| feature column | description | data type  |
|:--------:|:------------------------:| :--------------:| 
|mbid  | id | --   |
| artist_mb | name of artist(s) |   -- |
|artist_lastfm  | -- |  --|
| country_mb | country | -- |
| country_lastfm     |    --  | -- | 
|  tags_mb	    |  genre tags | -- | 
|  tags_lastfm  |   -- | -- | 
| listeners_lastfm | -- | -- |
| scrobbles_lastfm     |    -- | -- | 
|  ambiguous_artist    |  -- | -- | 
								
<br>


<br>

