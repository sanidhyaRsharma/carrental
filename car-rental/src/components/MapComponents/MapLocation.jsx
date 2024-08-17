import React, {PropTypes, Component} from 'react';
import { MapLocationStyle, MapLocationStyleHover } from './MapStyle.js';

export default class MapLocation extends Component {

    static defaultProps = {};

    constructor(props) {
        super(props);
    }

    render() {
        const style = this.props.$hover ? MapLocationStyleHover : MapLocationStyle;

        return (
            <div style = {style}>
                {this.props.text}
            </div>
        );
    }
}