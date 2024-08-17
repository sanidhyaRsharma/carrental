const ICON_SIZE = 50;

const MapLocationStyle = {
    position: 'absolute',
    width: ICON_SIZE,
    height: ICON_SIZE,
    left: -ICON_SIZE/2,
    top: -ICON_SIZE/2,

    border: '5px solid #fca450',
    borderRadius: ICON_SIZE,
    backgroundColor: 'white',
    textAlign: 'center',
    color: '#3f51b5',
    fontSize: 16,
    padding: 4,
    cursor: 'pointer'
};

const MapLocationStyleHover = {
    ...MapLocationStyle,
    border: '5px solid #3f51b5',
    color: '#f44336'
}

export {MapLocationStyle, MapLocationStyleHover, ICON_SIZE};
