'use strict';

import React, { Component } from 'react';

import {
	StyleSheet,
	View,
	TouchableHighlight,
	Text,
} from 'react-native';
import Camera from 'react-native-camera';

var styles = StyleSheet.create({
	description: {
		fontSize: 20,
		textAlign: 'center',
		color: "#FFFFFF"
	},
	container: {
		flex: 1,
		 justifyContent: 'center',
		 alignItems: 'center',
		 backgroundColor: '#123456'
	}
});

class Game extends Component {
	render() {
		return (
			<View style={styles.container}>
        <Camera 
          style={styles.camera}
          captureTarget={Camera.constants.CaptureTarget.disk, 
                         Camera.constants.CaptureQuality.low, 
                         Camera.constants.Orientation.portrait }
          ref={(cam) => {
            this.camera = cam;
          }}>
          <TouchableHighlight style={styles.timerButton} onPress={this.takePicture.bind(this)}>
            <Text>Welcome to Notate!</Text>
          </TouchableHighlight>
        </Camera>
			</View>
		);
	}
	takePicture() {
    this.camera.capture()
      .then((data) => console.log(data))
      .catch(err => console.error(err));
  }  
}

module.exports = Game;