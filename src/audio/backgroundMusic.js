import { FeatureManager } from '../featureManager/featureManager';

const featureManager = new FeatureManager(); // Singleton or shared instance

export const playBackgroundMusic = () => {
  if (featureManager.isFeatureEnabled('audio')) {
    const audio = new Audio('path/to/music.mp3');
    audio.loop = true;
    audio.play();
  }
};
