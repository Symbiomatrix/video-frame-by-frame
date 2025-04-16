# Frame by frame browser
Javascript based manual frame browser / player for short animations.

I have so far been unable to find a free, precise, convenient player for frame by frame, particularly for genned videos; potplayer, mpebc, vlc - it's a very tacked on feature for all of these.
So instead I had gepetto write one to spec in browser.

## General features
- Support for modern chromium browsers (chrome, brave). Firefox kinda works, not all features fully functional on my end. Possibly edge, but who cares.
- Support for (short) mp4 and webp - video frames are fully prerendered so quite memory intensive for >30s.
- Local app (can actually be run as a standalone app by creating a shortcut, see: https://superuser.com/questions/1643889/how-to-open-local-html-file-as-app).
  Drag and drop anywhere to load file.
- A manual control for frames with forward / backward buttons.
- An autoplay control playing the animation continuously with a frame counter.
- Controls are mostly responsive, their size will adjust to page size whilst maintaining frames' aspect ratio.
## Navigation
- Can zoom in / out on either control using mouse wheel, move around by click+move, reset the zoom by double clicking.
  The max / min zoom values can be set freely according to animation quality or preference.
- Autoplay fps is controllable (it might try to load from file, but I think it doesn't actually work), upper limit can be changed like zoom (but capped by cpu / gpu limits).
- The manual buttons can be held down to play continuously, and frames will change in accordance with set fps.
  A short click will always change one frame.
- Arrow keys are supported instead of buttons, but they will follow os' repeat rate.
## Output
- Button to download current (manual) frame, considering current zoom and canvas size - the image will be exactly what is shown, aside from cropping what lies outside the frame borders.

## Todo
- Add support for gifs and other common video types - each time I've tried this all the features were broken and gifs still failed to load (hallucinated commands).
  Probably need to request a standalone render then combine it in as I did with mp4.
- Frame limit / caching / live interpretation - Long vids consume far too much ram and time.
  Only really need to render a few frames forward and back (and maybe keyframes), and handle the slider jumps slowly.
- UI could use some improvement.
- More advanced features: Selectable AB play loop, labelled jump points, exporting segments.
  I haven't really planned on making this a full blown editor, frankly. There are far more optimised tools for that.

## Samples
![Demo1](https://github.com/user-attachments/assets/67df53e2-3e55-44b9-b049-e6545c27e403)

![Demo2](https://github.com/user-attachments/assets/bfa22779-bf48-4a8b-872c-41d9e32150a9)
