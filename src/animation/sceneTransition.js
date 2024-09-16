export const fadeTransition = (outElement, inElement, duration) => {
  outElement.style.transition = \opacity \ms\;
  outElement.style.opacity = '0';

  inElement.style.opacity = '0';
  inElement.style.transition = \opacity \ms\;
  inElement.style.opacity = '1';

  setTimeout(() => {
    document.body.removeChild(outElement);
  }, duration);
};
