import * as THREE from 'three';
import { updateCamera } from './camera';
import { playerControls, firstPersonPlayerControls, updateGhosts } from './controls';
import { getCells, getGhosts } from './data';
import { startScene } from './story/sceneManager';
import { updateGame } from './update';
import { FeatureManager } from './featureManager/featureManager';

const featureManager = new FeatureManager();
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

if (featureManager.isFeatureEnabled('audio')) {
  import('./audio/backgroundMusic').then(({ playBackgroundMusic }) => playBackgroundMusic());
}

if (featureManager.isFeatureEnabled('levels')) {
  import('./levels/levelManager').then(({ loadLevel }) => loadLevel('level1'));
}

// Add control panel for feature toggling
import('./ui/controlPanel').then(({ createControlPanel }) => createControlPanel());

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const animate = () => {
  requestAnimationFrame(animate);
  updateGame();
  renderer.render(scene, camera);
};

animate();
