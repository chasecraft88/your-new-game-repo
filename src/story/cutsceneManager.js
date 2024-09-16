import { cutscenes } from './cutscenes';

let cutsceneTimeouts = [];

export const showCutscene = (scene, cutsceneKey) => {
  const cutsceneData = cutscenes[cutsceneKey];
  if (!cutsceneData) return;

  const cutsceneElement = document.createElement('div');
  cutsceneElement.style.position = 'absolute';
  cutsceneElement.style.top = '50%';
  cutsceneElement.style.left = '50%';
  cutsceneElement.style.transform = 'translate(-50%, -50%)';
  cutsceneElement.style.color = 'white';
  cutsceneElement.style.fontSize = '24px';
  cutsceneElement.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
  cutsceneElement.style.padding = '20px';
  cutsceneElement.style.borderRadius = '10px';
  cutsceneElement.style.textAlign = 'center';
  cutsceneElement.style.zIndex = '10';
  document.body.appendChild(cutsceneElement);

  let currentIndex = 0;

  const showNextLine = () => {
    if (currentIndex >= cutsceneData.length) {
      document.body.removeChild(cutsceneElement);
      clearTimeouts();
      return;
    }
    cutsceneElement.innerText = cutsceneData[currentIndex].text;
    setTimeout(() => {
      currentIndex++;
      showNextLine();
    }, cutsceneData[currentIndex].duration);
  };

  const clearTimeouts = () => {
    cutsceneTimeouts.forEach(timeout => clearTimeout(timeout));
    cutsceneTimeouts = [];
  };

  showNextLine();
};
