import React from "react";
import GoogleMap from 'google-map-react';
import MapLocation from "../MapComponents/MapLocation";
import { ICON_SIZE } from "../MapComponents/MapStyle";

const MarkerComponent = ({text}) => <div>{text}</div>;

export default function SimpleMap(){
    const defaultProps = {
        center: {
            lat: 41.11699813791513,
            lng: -85.10900177043406
        },
        zoom: 12
    
    };

    return (
        <div style = {{ height: '100vh', width: '100%' }}>
            <GoogleMap
            bootstrapURLKeys={{ key: "" }}
            defaultCenter={defaultProps.center}
            defaultZoom={defaultProps.zoom} 
            hoverDistance={ICON_SIZE/2}>
                {/* <MarkerComponent 
                    lat = {41.11779580415948}
                    lng = {-85.10800181555999}
                    text = "Java Spot"
                /> */}
                <MapLocation 
                    lat = {41.11779580415948}
                    lng = {-85.10800181555999}
                    text = {'CR1'}
                />
                <MapLocation 
                    lat = {41.11699813791513}
                    lng = {-85.10900177043406}
                    text = {'CR2'}
                />
            </GoogleMap>
        </div>
    );
}
