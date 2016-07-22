import NavigationBar from 'react-native-navbar'
/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  TouchableHighlight,
} from 'react-native'

import Camera from 'react-native-camera';

class Notate extends Component {
  render() {
    return (
      <View style={styles.container}>
        <NavigationBar
          style={styles.navbar}
          title={{ title:  'Notate' , tintColor:  'black' , }}
          leftButton={{ title: 'Back', }}
          rightButton={{ title: 'Forward', }}
          statusBar={{ tintColor: "white", }}
        />
        <Camera
          captureTarget={Camera.constants.CaptureTarget.disk, Camera.constants.CaptureQuality.low, Camera.constants.Orientation.portrait }
          ref={(cam) => {
            this.camera = cam;
          }}>
          <Text style={styles.welcome} onPress={this.takePicture.bind(this)}>Welcome to Notate!</Text>
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
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 100,
    borderWidth: 2,
  },
  navbar: {
    backgroundColor:  "white" ,
  }
});

AppRegistry.registerComponent('Notate', () => Notate);
