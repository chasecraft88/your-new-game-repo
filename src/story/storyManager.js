git import * as THREE from 'three';
import { displayStory } from './story';

// List of story events with conditions
const storyEvents = [
  { id: 1, message: "You've entered the Dark Forest. Something feels off...", condition: (player) => player.position.z > 10 },
  { id: 2, message: "You found an ancient artifact. It seems to be glowing...", condition: (player) => player.position.x < 5 },
  // Add more events here
];

export const checkStoryEvents = (player) => {
  for (const event of storyEvents) {
    if (event.condition(player)) {
      displayStory(scene, camera, event.id);
      // Remove or update event after triggering if needed
    }
  }
};
