import * as THREE from 'three';

export const storyText = [
  "Welcome to the Echo of Silence. Your journey begins here...",
  "You find yourself in a mysterious land filled with forgotten echoes.",
  "Your goal is to uncover the secrets hidden within these shadows...",
  "Beware of the ghosts that lurk in the darkness. They hold the key to your next clue."
];

export const displayStory = (scene, camera, storyIndex = 0) => {
  const storyElement = document.createElement('div');
  storyElement.style.position = 'absolute';
  storyElement.style.top = '10px';
  storyElement.style.left = '10px';
  storyElement.style.color = '#FFF';
  storyElement.style.fontSize = '24px';
  storyElement.style.fontFamily = 'Arial, sans-serif';
  storyElement.innerHTML = storyText[storyIndex];
  
  document.body.appendChild(storyElement);
  
  setTimeout(() => {
    document.body.removeChild(storyElement);
    if (storyIndex < storyText.length - 1) {
      displayStory(scene, camera, storyIndex + 1);
    }
  }, 5000); // Display each part for 5 seconds
};
