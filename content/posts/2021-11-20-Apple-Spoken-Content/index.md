+++
title = "Get an Audio Version of Any Blog Post"
description = "How to turn any article into a podcast."

[extra]
social_image = "SpokenContentCover.png"
+++

{{ soundcloud(id="1163756371") }}

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

{{ video(
    sources=["./spoken-content-setup.mp4"],
    w="300px",
    alt="iOS Spoken Content Setup Demo",
    loop=true) }}

It's a pain to select text and then tap on the screen to speak. That's where the
second trick comes in. Another feature hidden in accessibility is an alternative
input method. If you head over to `Settings > Accessibility > Touch > Back Tap`,
you can set either of the taps to turn on `Speak Screen`. I personally, set
`Triple Tap : Speak Screen`.

On macOS, it's a similar process. Head to
`System Preferences > Accessibility > Spoken Content` and turn on
`Speak Selection`. The default keyboard shortcut is `⌥ + Esc`.

{{ video(
    sources=["./macos-setup.mp4"],
    w="650px",
    alt="macOS Desktop Spoken Content Setup Demo",
    loop=true) }}

The thing I like the most about this setup is that it's native--so I know it'll
work on all my apps, system-wide. (I used the
[Wavenet Chrome extension](https://chrome.google.com/webstore/detail/wavenet-for-chrome/iefankigbnlnlaolflbcopliocibkffc?hl=en)
in the past) I often find myself using it on my Mac to read things I've written
back to me to catch typos. Anecdotally, I've also found that I retain content
better if I'm listening to it while I'm reading it. This seems to be
[borne out in the literature](https://moritz.digital/reading/)
as well.

{{ video(
    sources=["./python-paradox.mp4"],
    w="300px",
    alt="Safari Reader Mode Demo",
    loop=true) }}

It works great with iBooks and also with blog posts and longer news articles.
Sometimes the articles have superfluous bits of text (ads, call to actions, and
so on) that you might want to avoid. Safari has a built-in reader mode that
works well on most articles. Just tap the left part of the address bar on iOS,
and it'll swap to a reader view that works much better with `Spoken Content`. On
desktop Chrome, you can do something very similar by heading to
[chrome flags](chrome://flags/) and setting `Enable Reader Mode : Enabled`.

{{ image(src="./ChromeReaderMode.png", alt="Chrome Reader Mode Setup") }}

I also set up keyboard shortcuts for this by going to
`System Preferences > Keyboard > Shortcuts` and adding an entry for
`Enter Reader Mode` and `Exit Reader Mode`. I use `⌃ + ⇧ + R`.

{{ image(
    src="./ChromeReaderModeKeyboardShortcuts.png",
    alt="Chrome Reader Mode Keyboard Shortcut") }}
