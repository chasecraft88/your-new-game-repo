export const animateObject = (object, fromProps, toProps, duration) => {
  const start = Date.now();
  const initialProps = { ...fromProps };

  const animate = () => {
    const elapsed = Date.now() - start;
    const progress = Math.min(elapsed / duration, 1);

    Object.keys(toProps).forEach((prop) => {
      object[prop] = initialProps[prop] + (toProps[prop] - initialProps[prop]) * progress;
    });

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  };

  animate();
};
