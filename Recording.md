# Recording

Some quick notes on how I set up Audcity for each blog post

1. Record the audio in tracks
   1. When you mess up--that's okay, just stop the recording and then go to
   `Tracks > Add New > Stereo Track`
   2. Then, when you've got the entire post recorded, use the following steps to
   flatten the tracks into a single track
      1. Select all tracks and then, `Tracks > Align Tracks > Align End-to-End`
      2. Select all again and then, `Tracks > Mix > Mix and Render`
   3. Now sample the noise at the start and remove the background audio
      1. Select the start without audio, `Effect > Noise Reduction >
      Get Audio Profile`
      2. Then apply the noise reduction `Effect > Noise Reduction > OK`
         1. The numbers: 12, 6, 3
   4. Now do the rough cut and remove any large silences
      1. Run `Truncate Silence` if you would like
   5. Now equalize the audio
      1. `Effect > Filter Curve`
         1. Apply the following settings if the settings have been reset
         2. ![Filter Curve Settings](https://i.imgur.com/lHxSF3b.png)
   6. Then export the audio as mp3
   7. Upload the audio to Soundcloud
      1. Don't forget to add the blog post image
      2. Grab the embed html and insert it into the blog post
