export const animateCamera = (camera, fromPosition, toPosition, duration) => {
  const start = Date.now();

  const animate = () => {
    const elapsed = Date.now() - start;
    const progress = Math.min(elapsed / duration, 1);

    camera.position.lerpVectors(fromPosition, toPosition, progress);

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  };

  animate();
};
