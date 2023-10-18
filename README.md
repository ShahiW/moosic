# MOOSIC - Music Recommendation System

MOOSIC was created in the course of a capstone project at the IT school neuefische Hamburg. We - Christian, Grace and Shahi - formed a team with the goal to build an alternative music recommendation system. With our common love for music, joy for creative work and no shyness for challenges, we planned and implemented this project. The final product is a trained model that makes predictions based on the user input wrapped in a Web App. 
<br>

How did we come up with our project idea?
We were talking about how unsatisfied we are with the music recommendations we get from Spotify or other music streaming platforms. When we talked about why we don’t like the recommendations we figured out, that the same songs were proposed partly repeatedly or the tracks didn’t fit the mood we were in or the activity we were engaged in. By thinking of ways how to tackle these problems we came to the conclusion, that it would be nice to have some kind of user input, to make the track recommendations fit the user preferences. We then pinpointed the two features mood and genre to act as filters for better predictions.
<br>

Why did we go with these two features mood and genre?
The problem with music recommendations at present is that the recommended tracks often times don’t fit the listeners mood. For example Spotify uses a complex system of a variety of factors to personalize the listening experience for each user. These factors include the user's listening history, their favorite songs and artists, and the genres and playlists they listen to. The problem is, that mood isn’t tracked. And it’s the most human thing to change moods over the course of time - be it days or hours. So, when we are sad on one day for example and listen extensively to sad songs, the algorithm is bound to recommend these songs again to the user, even if the user isn’t in a sad mood any more. 
<br>

Curious about the final product? Click here: [MOOSIC](https://moosic.winderling.net)

Want to take a look at our cool Slides Presentation? Click here: [Capstone Endpresentation](https://docs.google.com/presentation/d/1Ka-l_OXa4FF1w02ZJ6dam3xc3z0_auSv6qDpuckh5uY/edit?usp=sharing)


<div id="header" align="center">
 <img scr="https://github.com/ShahiW/moosic/tree/main/Moosic-web-app/moosic/static/images/moosic.png"> 
 </div>


<br>




__Install environment:__

```bash
python -m venv .venv 
source .venv/bin/activate 
pip install --upgrade pip 
pip install -r requirements.txt 
```

