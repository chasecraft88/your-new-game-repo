import * as THREE from 'three';
import { createSkybox, createGround, createWall, createFood, createPowerUp, createPlayer, createGhost, createLevel } from './src/geometry/geometry';
import { playerControls, firstPersonPlayerControls, updateGhosts } from './src/controls/controls';
import { updateCamera } from './src/camera/camera';
import { drawLives } from './src/data/data';
import { storyIntro } from './src/story/story';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('gameContainer').appendChild(renderer.domElement);

const player = createPlayer(scene);
createSkybox(scene, 50);
createGround(scene, 50);
createLevel(scene);

const controls = {};
const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  
  const delta = clock.getDelta();
  
  // Update player and ghosts
  playerControls(player, controls);
  updateGhosts(cells, ghosts);
  
  // Update camera
  updateCamera(camera, player, 1, 0, 0); // Example: first person view
  
  // Render scene
  renderer.render(scene, camera);
}

animate();

// Initialize story
storyIntro();
