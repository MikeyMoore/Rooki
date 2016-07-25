'use strict';

import React, { Component } from 'react';
import {
  AppRegistry,
  TabBarIOS,
  StyleSheet,
  Dimensions,
  Text,
  View,
  TouchableHighlight,
} from 'react-native'

import Camera from 'react-native-camera';

var Game = require('./game.ios');
var Notes = require('./notes.ios');

class Notate extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedTab: 'game'
    };
  }

  render() {
    return (
      <TabBarIOS selectedTab={this.state.selectedTab}>

      <TabBarIOS.Item
      style={styles.tabs}
      selected={this.state.selectedTab === 'game'}
      // icon={{uri:'gameplay'}}
      title='Game'
      onPress={() => {
        this.setState({
          selectedTab: 'game'
        });
      }}>
      <Game />
      </TabBarIOS.Item>

      <TabBarIOS.Item
      style={styles.tabs}
      selected={this.state.selectedTab === 'notes'}
      // icon={{uri:'notations'}}
      title="Notations"
      onPress={() => {
        this.setState({
          selectedTab: 'notes'
        });
      }}>
      <Notes />
      </TabBarIOS.Item>

      </TabBarIOS>
    )
  }
}

const styles = StyleSheet.create({
    tabs: {
      // fontSize: 12
    }
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//     backgroundColor: '#F5FCFF',
//   },
//   navbar: {
//     backgroundColor:  "white" ,
//     position: 'absolute',
//     flexDirection: 'row',
//     top: 0,
//   },
//   camera: {
// //     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//     backgroundColor: '#F5FCFF',
//   },
//   timerButton: {
//     margin: 100,
//     borderWidth: 2,
//     backgroundColor: '#000000',
//   },
});

AppRegistry.registerComponent('Notate', () => Notate);
