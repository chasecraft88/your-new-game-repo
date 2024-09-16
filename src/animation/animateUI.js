export const animateUI = (element, animation) => {
  element.style.transition = animation;
  element.classList.add('animated');
};
