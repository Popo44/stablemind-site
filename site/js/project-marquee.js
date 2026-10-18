// Start the carousel when it enters view, so Ensol is visible on arrival.
document.querySelectorAll('[data-project-marquee]').forEach(function (carousel) {
  if (!('IntersectionObserver' in window)) {
    carousel.classList.add('is-running');
    return;
  }
  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        carousel.querySelectorAll('.layout414_image-list').forEach(function (row) {
          row.getAnimations().forEach(function (animation) {
            if (animation.animationName === 'project-marquee') animation.currentTime = 0;
          });
        });
      }
      carousel.classList.toggle('is-running', entry.isIntersecting);
    });
  }, {threshold: 0.1});
  observer.observe(carousel);
});
