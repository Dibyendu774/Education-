// this is an OLD version! For the updated v3 one that includes snapping to the closest section, see https://codepen.io/GreenSock/pen/ExvZjZQ?editors=0010

console.clear();

var slideDelay = 1.5;
var slideDuration = 1;
var slides = document.querySelectorAll(".slide");
var numSlides = slides.length;

TweenLite.set(slides, {
  xPercent:function(i, target){
    return i * 100;
  }
});

var wrap = wrapPartial(-100, (numSlides - 1) * 100);
var timer = TweenLite.delayedCall(slideDelay, autoPlay).pause();
var proxy = document.createElement("div");
TweenLite.set(proxy, { x: "+=0" });
var transform = proxy._gsTransform;
var slideWidth = 0;
var wrapWidth = 0;
var animation = new TimelineMax({repeat:-1});
resize();

var draggable = new Draggable(proxy, {
  trigger: ".slides-container",
  throwProps: true,
  onPressInit: function() {
    animation.pause();
    timer.pause();
    updateProgress();
  },
  onDrag: updateProgress,
  onThrowUpdate: updateProgress,
  onThrowComplete: function() {
    timer.restart(true);
  }
});

window.addEventListener("resize", resize);

function animateSlides(direction) {
  var progress = animation.progress() + direction / numSlides;
  timer.pause();
  animation.pause();
  TweenLite.to(animation, slideDuration, {
    progress:progress,
    overwrite:true,
    modifiers:{
      progress:function(value) {
        return (value < 0 || value === 1 ? 1 : 0) + (value % 1);
      }
    },
    onComplete:function() {
      timer.restart(true);
    }
  });
}

function autoPlay() {
  animation.play();
  TweenLite.fromTo(animation, 1, {timeScale:0}, {timeScale:1, ease:Power1.easeIn})
}

function updateProgress() {
  animation.progress(transform.x / wrapWidth);
}

function resize() {
  var progress = animation.progress();
  slideWidth = slides[0].offsetWidth;
  wrapWidth = slideWidth * numSlides;

  animation.progress(0).clear().to(slides, 100, {
    xPercent: "+=" + (numSlides * 100),
    ease: Linear.easeNone,
    modifiers: {
      xPercent: wrap
    }
  })
  .to(proxy, 100, {x:wrapWidth, ease:Linear.easeNone}, 0)
  .progress(progress);
}

function wrapPartial(min, max) {
  var r = max - min;
  return function(value) {
    var v = value - min;
    return ((r + v % r) % r) + min;
  }
}

Hamster($('.slides-container')[0]).wheel(function(event, delta, deltaX, deltaY) {
  event.preventDefault();
  animateSlides(delta/30);
});