import { storyText, displayStory } from './story/story';
import { updateGame, checkForUpdates } from './update/update';

// Call displayStory to start the story
displayStory(scene, camera);

// Call updateGame periodically
setInterval(() => {
  updateGame(scene, camera);
}, 60000); // Update every minute

// Call checkForUpdates periodically
setInterval(() => {
  checkForUpdates();
}, 3600000); // Check for updates every hour
import { checkStoryEvents } from './story/storyManager';
import { saveGame, loadGame } from './saveLoad/saveLoad';
import { fetchUpdates } from './update/updateManager';

// Call displayStory to start the story
displayStory(scene, camera);

// Call updateGame periodically
setInterval(() => {
  updateGame(scene, camera);
}, 60000); // Update every minute

// Call checkForUpdates periodically
setInterval(() => {
  checkForUpdates();
}, 3600000); // Check for updates every hour

// Load game state on start
loadGame(player);

// Save game state periodically or on specific events
setInterval(() => {
  saveGame(player);
}, 60000); // Save every minute

// Check for updates periodically
setInterval(fetchUpdates, 3600000); // Check for updates every hour
import { checkStoryEvents } from './story/storyManager';
import { saveGame, loadGame } from './saveLoad/saveLoad';
import { fetchUpdates } from './update/updateManager';

// Call displayStory to start the story
displayStory(scene, camera);

// Call updateGame periodically
setInterval(() => {
  updateGame(scene, camera);
}, 60000); // Update every minute

// Call checkForUpdates periodically
setInterval(() => {
  checkForUpdates();
}, 3600000); // Check for updates every hour

// Load game state on start
loadGame(player);

// Save game state periodically or on specific events
setInterval(() => {
  saveGame(player);
}, 60000); // Save every minute

// Check for updates periodically
setInterval(fetchUpdates, 3600000); // Check for updates every hour
