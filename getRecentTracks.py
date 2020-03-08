# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from sklearn import tree
#import sklearn
## def show_tracks(tracks):
    ## for i, item in enumerate(tracks['items']):
        ## track = item['track']
        ## print '   %d %32.32s %s' % (i, track['artists'][0]['name'], track['name'])
if __name__ == '__main__':
    ## if len(sys.argv) > 1:
    username = '1234fll2014'
    ## else:
        ##print ("Whoops, need your username!")
        ##print ("usage: python user_playlists.py [username]")
        ##sys.exit()

    token = 'BQCNwGvS9gMILHBt53VDe4Xjc4YsOH__3BKPgDsv_43tFF-7Y1A9qdcKF1mDP-QJoGUipakd8-yLP9vJRAqmtzQFIidGncOW7mWQGALb8oBJNcNMhpzq8KPsvXLWPYGHGMdul1TsPmJgbjTZJQ'

    numbers = [[0.74,0.613,8,-4.88,1,0.145,0.258,0.00372,0.123,0.473,75.023], [0.872,0.391,0,-9.144,0,0.242,0.469,4.13e-06,0.297,0.437,134.021],[0.669,0.308,11,-10.068,1,0.029,0.883,0,0.0984,0.52,64.934],[.558,.801,7,-5.795,1,0.131,.133,0,.392,.831,105.006],[0.453,0.496,5,-5.785,1,0.0453,0.554,2.65e-05,0.0772,0.501,80.994,],[0.479,0.419,0,-6.517,1,0.0389,0.568,0.000217,0.11,0.186,85.014],[0.661,0.373,5,-8.249,1,0.0505,0.615,0,0.177,0.523,91.5],[0.522,0.833,0,-3.715,1,0.0575,0.0454,0,0.127,0.296,180.009],[0.716,0.805,4,-3.839,1,0.0856,0.014,3.1e-06,0.291,0.719,142.886],[0.762,0.576,1,-4.951,0,0.0829,0.0556,0,0.869,0.316,142.096],[0.762,0.576,1,-4.951,0,0.0829,0.0556,0,0.869,0.316,142.096]]
    labels = ["sad", "sad","sad","happy","sad","sad","sad","sad","happy","happy","happy"]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(numbers,labels)

    if token:
        sp = spotipy.Spotify(auth=token)
        recentMusic = sp.current_user_recently_played(limit=50)
        x = str(recentMusic)
        ##print(x)
        codes = []

        for a in range(0,len(x),1):
            code = ""
            if (x[a] == 't') and (x[a+1] == 'r') and (x[a+2] == 'a') and (x[a+3] == 'c') and (x[a+4] == 'k') and (x[a+5] == '/'):
                for b in range(1,23):
                    code+=x[a+5+b]
                codes.append(code)
            else:
                continue
        featureNames = ["danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo"]
        happyCounter = 0
        sadCounter = 0
        for i in range(0,len(codes)-1):
            analyzed = sp.audio_features(codes[i])
            features = []
            for z in range(0,11):
                 features.append(analyzed[0][featureNames[z]])
                 #print(len(features))
            result = clf.predict([features])
            print (result)
            if(result == "happy"):
                happyCounter = happyCounter + 1
            else:
                sadCounter = sadCounter + 1
        if(sadCounter>=35):
            print ("You may be depressed")
        else:
            print ("You most likely are not depressed")








        ##for playlist in playlists['items']:
            ##if playlist['owner']['id'] == username:
                ##print
                ##print (playlist['name'])
                ##print ('  total tracks', playlist['tracks']['total'])

                ##tracks = results['tracks']
                ##show_tracks(tracks)
                ##while tracks['next']:
                    ##tracks = sp.next(tracks)
                    ##show_tracks(tracks)
    else:
        print ("Can't get token for", username)
