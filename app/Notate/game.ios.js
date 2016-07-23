'use strict';

import React, { Component } from 'react';

import {
	StyleSheet,
	View,
	Dimensions,
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
          style={styles.preview}
          aspect={Camera.constants.Aspect.fill}
          captureTarget={Camera.constants.CaptureTarget.disk, 
                         Camera.constants.CaptureQuality.low, 
                         Camera.constants.Orientation.portrait }
          ref={(cam) => {
            this.camera = cam;
          }}>
          <Text style={styles.capture} onPress={this.takePicture.bind(this)}>[CAPTURE]</Text>
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

const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  preview: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    height: Dimensions.get('window').height,
    width: Dimensions.get('window').width
  },
  capture: {
    flex: 0,
    backgroundColor: '#fff',
    borderRadius: 5,
    color: '#000',
    padding: 10,
    margin: 40
  }
});

module.exports = Game;