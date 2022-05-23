import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn import preprocessing

''' 
 Reading data into a pandas DataFrame
    - Pandas treat 'NA' rows as Missing values (don't found any missing value in csv file)
    - For some reason, i can't see any data
'''

# DATA PROCESSING

top_hits = pd.read_csv('..\docs\songs_normalize.csv')

# Check for null values - there are none
null_values = top_hits.isnull().any().sum()
print("Null values: ", null_values)

# Remove rows with set() values in the genre column
top_hits = top_hits[top_hits.genre != "set()"]

# EXPLORATORY ANALYSIS

# Create correlation heatmap for possible aggregation of columns
le = preprocessing.LabelEncoder()
le.fit(top_hits['popularity'])
top_hits['popularity'] = le.transform(top_hits['popularity'])
corr_matrix = top_hits.corr()

plt.figure(figsize=(15,15))
plt.title('Correlation Heatmap of Top Hits Dataset')
a = sb.heatmap(corr_matrix, square=True, annot=True, fmt='.2f', linecolor='black')
a.set_xticklabels(a.get_xticklabels(), rotation=30)
a.set_yticklabels(a.get_yticklabels(), rotation=30)
plt.show()
# Since the hightest correlation between attributes (other than with itselves) is only 0.65, there will be no aggregation of columns


# Remove non-numerical values and change explict column from true & false to 1 and 0 for scatter plot
top_hits_scatter = top_hits
for col in top_hits_scatter.columns:
    if top_hits_scatter[col].dtype == "object":
        top_hits_scatter = top_hits_scatter.drop(columns=[col], axis=1)
    elif top_hits_scatter[col].dtype == "bool":
        top_hits_scatter[col] = top_hits_scatter[col].astype(int)

sb.pairplot(top_hits_scatter, hue='popularity')
plt.savefig('new_new_pairplot.png')

'''
Varibles:
    artist: Name of the Artist.
    song: Name of the Track.
    duration_ms: Duration of the track in milliseconds.
    explicit: The lyrics or content of a song or a music video contain one or 
            more of the criteria which could be considered offensive or unsuitable for children.
    year: Release Year of the track.
    popularity: The higher the value the more popular the song is.
    danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo,
            rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
    energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
    key: The key the track is in. Integers map to pitches using standard Pitch Class notation. 
            E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
    loudness: The overall loudness of a track in decibels (dB). 
            Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. 
            Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). 
            Values typically range between -60 and 0 db.
    mode: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. 
            Major is represented by 1 and minor is 0.
    speechiness: Speechiness detects the presence of spoken words in a track. 
            The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. 
            Values above 0.66 describe tracks that are probably made entirely of spoken words. 
            Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, 
                including such cases as rap music. 
            Values below 0.33 most likely represent music and other non-speech-like tracks.
    acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 
            1.0 represents high confidence the track is acoustic.
    instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. 
            Rap or spoken word tracks are clearly "vocal". 
            The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. 
            Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
    liveness: Detects the presence of an audience in the recording. 
            Higher liveness values represent an increased probability that the track was performed live. 
            A value above 0.8 provides strong likelihood that the track is live.
    valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. 
            Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), 
                while tracks with low valence sound more negative (e.g. sad, depressed, angry).
    tempo: The overall estimated tempo of a track in beats per minute (BPM). 
            In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
    genre: Genre of the track.
'''

# Pelo que percebi pairplot so funciona com 4 vars
# Portanto pensar em que 4 vars usar 
# Não entendi bem o que procurar se 'genre', se 'popularity'...

# Hue acho que faz sentido ser 'popularity', 
# pq acho que o queremos é que um algoritmo possa analizar uma música especifica e determinar se irá ser popular ou não

# sb.pairplot(top_hits.dropna(), hue='genre', vars=["popularity", "danceability", "instrumentalness", "speechiness"])


#sb.pairplot(top_hits.dropna(), hue='popularity')



# Guarda o plot do pairplot
#plt.savefig('new_pairplot.png')
