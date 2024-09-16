export class FeatureManager {
  constructor() {
    this.features = {
      audio: false,
      levels: false,
      saveLoad: false,
      ui: false,
      input: false,
      ai: false,
      optimization: false,
      multiplayer: false,
      story: false,
      achievements: false,
      errorHandling: false
    };
  }

  toggleFeature(feature, isEnabled) {
    if (this.features.hasOwnProperty(feature)) {
      this.features[feature] = isEnabled;
      console.log(\\ is now \\);
    } else {
      console.warn(\Feature \ does not exist.\);
    }
  }

  isFeatureEnabled(feature) {
    return this.features[feature];
  }
}
