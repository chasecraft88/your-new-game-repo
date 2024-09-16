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
