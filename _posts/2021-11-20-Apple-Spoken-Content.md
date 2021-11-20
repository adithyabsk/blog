---
layout: post
description: How to turn any article into a "podcast."
category: productivity
title: Get an Audio Version of Any Blog Post
image: images/chipotle/blog_image.png
---

![]({{ site.baseurl }}/images/spoken_content/SpokenContentCover.png)

### Audio Version

<!-- markdownlint-disable -->
<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1163756371&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/adithyabsk" title="Adithya" target="_blank" style="color: #cccccc; text-decoration: none;">Adithya</a> · <a href="https://soundcloud.com/adithyabsk/spoken-content" title="Get An Audio Version of Any Blog Post" target="_blank" style="color: #cccccc; text-decoration: none;">Get An Audio Version of Any Blog Post</a></div>
<!-- markdownlint-enable -->

I've sometimes found myself distracted while reading a passage or two and then
having to track back to re-read the sentence. Other times, I've been on a walk
and wanted to read a blog post. Although it's not a silver bullet,
I found a solution that works in most cases--a hidden Apple accessibility
feature. It's called
["Spoken Content"](https://support.apple.com/guide/iphone/spoken-content-iph96b214f0/ios)
and it's pretty easy to set up.

On your iOS device, go to `Settings > Accessibility > Spoken Content` and turn
on `Speak Selection`. Also make sure that `Highlight Content` is turned on.
If you then hop into `Voices`, you can pick a voice to narrate the content. I
particularly like `Siri Voice 1` which is not the default.

{% include video.html url="https://i.imgur.com/DSK4krC.mp4" style="width:300px"
alt="iOS Spoken Content Setup Demo" %}

It's a pain to select text and then tap on the screen to speak. That's where the
second trick comes in. Another feature hidden in accessibility is an alternative
input method. If you head over to `Settings > Accessibility > Touch > Back Tap`,
you can set either of the taps to turn on `Speak Screen`. I personally, set
`Triple Tap : Speak Screen`.

On macOS, it's a similar process. Head to
`System Preferences > Accessibility > Spoken Content` and turn on
`Speak Selection`. The default keyboard shortcut is `⌥ + Esc`.

{% include video.html url="https://i.imgur.com/ZwnLSxw.mp4" style="width:650px"
alt="macOS Desktop Spoken Content Setup Demo" %}

The thing I like the most about this setup is that it's native--so I know it'll
work on all my apps, system-wide. (I used the
[Wavenet Chrome extension](https://chrome.google.com/webstore/detail/wavenet-for-chrome/iefankigbnlnlaolflbcopliocibkffc?hl=en)
in the past) I often find myself using it on my Mac to read things I've written
back to me to catch typos. Anecdotally, I've also found that I retain content
better if I'm listening to it while I'm reading it. This seems to be
[borne out in the literature](https://moritz.digital/reading/)
as well.

{% include video.html url="https://i.imgur.com/zWCmFp0.mp4" style="width:300px"
alt="Safari Reader Mode Demo" %}

It works great with iBooks and also with blog posts and longer news articles.
Sometimes the articles have superfluous bits of text (ads, call to actions, and
so on) that you might want to avoid. Safari has a built-in reader mode that
works well on most articles. Just tap the left part of the address bar on iOS,
and it'll swap to a reader view that works much better with `Spoken Content`. On
desktop Chrome, you can do something very similar by heading to
[chrome flags](chrome://flags/) and setting `Enable Reader Mode : Enabled`.

![Chrome Reader Mode Setup]({{ site.baseurl }}/images/spoken_content/ChromeReaderMode.png)

I also set up keyboard shortcuts for this by going to
`System Preferences > Keyboard > Shortcuts` and adding an entry for
`Enter Reader Mode` and `Exit Reader Mode`. I use `⌃ + ⇧ + R`.

![Chrome Reader Mode Keyboard Shortcut]({{ site.baseurl }}/images/spoken_content/ChromeReaderModeKeyboardShortcuts.png)
