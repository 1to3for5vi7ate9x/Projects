
fetch('https://globe.gl/example/datasets/ne_110m_admin_0_countries.geojson').then(res => res.json()).then(countries => {
    const greenShades = ['#016EBD'];
    function getRandomGreenShade() {
        const randomIndex = Math.floor(Math.random() * greenShades.length);
        return greenShades[randomIndex];
    }
    const lightGreenTransparent = polished.transparentize(0.1, '#52B6FF');
    //const lightBlueTransparent = polished.transparentize(0.4, '#6AC5FE');
    const lightBlueTransparent = polished.transparentize(0.1, '#FFFFFF');
    const locations = [
        {
            "latitude": 51.4416,
            "longitude": 0.1487
        }, {
            "latitude": 50.1112,
            "longitude": 8.6831
        }, {
            "latitude": 53.3331,
            "longitude": -6.2489
        }, {
            "latitude": 56.8519,
            "longitude": 60.6122
        }, {
            "latitude": 35.617,
            "longitude": 139.7486
        }, {
            "latitude": 34.0522,
            "longitude": -118.2437
        }, {
            "latitude": 50.1155,
            "longitude": 8.6842
        }, {
            "latitude": 40.7128,
            "longitude": -74.006
        },
        {
            "latitude": -22.9068,
            "longitude": -43.1729
        }, {
            "latitude": -34.6037,
            "longitude": -58.3816
        }, {
            "latitude": 41.8919,
            "longitude": 12.5113
        }, {
            "latitude": 48.8566,
            "longitude": 2.3522
        }, {
            "latitude": -33.8688,
            "longitude": 151.2093
        }, {
            "latitude": 55.7558,
            "longitude": 37.6176
        }, {
            "latitude": 41.3851,
            "longitude": 2.1734
        }, {
            "latitude": 37.7749,
            "longitude": -122.4194
        }, {
            "latitude": 51.5074,
            "longitude": -0.1278
        }, {
            "latitude": -33.9248,
            "longitude": 18.4233
        },

    ];

    const points = locations.map(entry => ({
        lat: entry.latitude,
        lng: entry.longitude
    }));
    const MAX_CONCURRENT_ARCS = 5;
    const arcsData = [];
    const ringsData = [];
    // Array to hold the rings
    locations.forEach((source, idx) => {
        let availableIndexes = new Set(locations.map((_, index) => index));
        availableIndexes.delete(idx);
        availableIndexes = [...availableIndexes];
        const randomIndex = Math.floor(Math.random() * availableIndexes.length);
        const target = locations[availableIndexes[randomIndex]];
        const animationDuration = Math.random() * 15000 + 5000;
        // between 5 to 20 seconds
        const initialDelay = (animationDuration / MAX_CONCURRENT_ARCS) * (idx % MAX_CONCURRENT_ARCS);
        // stagger the start times
        arcsData.push({
            startLat: source.latitude,
            startLng: source.longitude,
            endLat: target.latitude,
            endLng: target.longitude,
            color: [lightGreenTransparent, lightGreenTransparent],
            arcDashLength: Math.random() * 0.4 + 0.6,
            arcAltitude: (0.5),
            arcDashGap: Math.random(),
            arcDashAnimateTime: animationDuration,
            arcDashInitialGap: initialDelay / animationDuration
        });
        // Add a ring for the destination
        ringsData.push({
            lat: target.latitude,
            lng: target.longitude,
            alt: 0.9,
            color: 'rgba(255,100,50,${1-idx/locations.length})'
        });
    }
    );
    const RINGS_MAX_R = 0.5;
    const RING_PROPAGATION_SPEED = 0.03;
    // const FLIGHT_TIME = 10000;
    // const ARC_REL_LEN = 1;
    // const NUM_RINGS = 5;
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    let globeWidth, globeHeight;
    if (isMobile) {
        globeWidth = '400';
        globeHeight = '400';
        // or any other preferred height for mobile
    } else {
        globeWidth = '1000';
        globeHeight = '1000';
    }
    const world = Globe().globeImageUrl('lightBlueColor.png')
        .width(globeWidth).height(globeHeight).hexPolygonsData(countries.features).hexPolygonResolution(3).hexPolygonMargin(0.3).hexPolygonUseDots(true).hexPolygonColor(() => getRandomGreenShade()).backgroundColor('white').pointColor(() => lightBlueTransparent).pointRadius(0.1).pointAltitude(0.05).arcsData(arcsData).arcColor('color').arcDashLength(d => d.arcDashLength).arcAltitude(0.2).arcDashGap(d => d.arcDashGap).arcDashAnimateTime(d => d.arcDashAnimateTime)
        (document.getElementById('globeViz'));
    const controls = world.controls();
    // Get the controls
    controls.enableZoom = false;
    // Disable zooming
    // world.pointOfView({ distance: 1, lat: 40, lng: -100, azimuth: 30, polar: 30 });
    // world.pointOfView({ lat: 40, lng: -100, altitude: 1.5, polar: 40 });
    world.pointOfView({
        lat: 20,
        lng: -100,
        altitude: 1.9
    });
    world.controls().autoRotate = true;
    // Enable auto-rotation
    world.controls().autoRotateSpeed = 0.5;
    // Set the rotation speed
    world.pointsData(points);
}
);