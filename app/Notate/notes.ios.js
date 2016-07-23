'use strict';

import React, { Component } from 'react';

import {
	StyleSheet,
	View,
	Text,
} from 'react-native';

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
		 backgroundColor: '#234123'
	}
});

class Notes extends Component {
	render() {
		return (
			<View style={styles.container}>
			<Text style={styles.description}>
			This is where the notations will be shown
			</Text>
			</View>
		);
	}
}

module.exports = Notes;