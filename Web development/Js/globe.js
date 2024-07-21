fetch('https://globe.gl/example/datasets/ne_110m_admin_0_countries.geojson')
  .then((res) => res.json())
  .then((countries) => {
    const greenShades = ['none']
    function getRandomGreenShade() {
      const randomIndex = Math.floor(Math.random() * greenShades.length)
      return greenShades[randomIndex]
    }
    const lightGreenTransparent = '#f25275'
    const lightredTransparent = '#2BB5B4'
    const bluetransparent = '#37CFA7'

    //const lightBlueTransparent = polished.transparentize(0.4, '#6AC5FE');
    const lightBlueTransparent = '#ffff'
    const locations = [
      {
        latitude: 24.138153,
        longitude: 79.320416,
      },
      {
        latitude: 60.570715,
        longitude: -119.95414,
      },
      {
        latitude: 34.308434,
        longitude: 103.567242,
      },
      {
        latitude: 64.458532,
        longitude: 91.159133,
      },
      {
        latitude: 3.42707,
        longitude: 20.916335,
      },
      {
        latitude: 44.762278,
        longitude: -100.216698,
      },
      {
        latitude: 59.027831,
        longitude: 48.973778,
      },
      {
        latitude: -6.603081,
        longitude: -61.245983,
      },
      {
        latitude: 18.704925,
        longitude: 17.504015,
      },
      {
        latitude: 28.975833,
        longitude: 41.058701,
      },
      {
        latitude: -28.094874,
        longitude: -17.30067,
      },
      {
        latitude: -32.494584,
        longitude: -113.453008,
      },
      {
        latitude: 15.004623,
        longitude: 171.3126,
      },
      {
        latitude: -25.427022,
        longitude: 117.875103,
      },
      {
        latitude: -23.527974,
        longitude: 130.77443,
      },
      {
        latitude: 75.929884,
        longitude: -47.474103,
      },
      {
        latitude: 21.578727,
        longitude: -42.374318,
      },
      {
        latitude: 59.746783,
        longitude: 54.818504,
      },
      {
        latitude: 71.435097,
        longitude: 87.865377,
      },
      {
        latitude: 59.835228,
        longitude: 60.970847,
      },
      {
        latitude: 32.010529,
        longitude: 135.677884,
      },
      {
        latitude: 52.106565,
        longitude: 19.816667,
      },
      {
        latitude: 33.358143,
        longitude: 50.842056,
      },
      {
        latitude: 35.01146187105427,
        longitude: 78.61911552489208,
      },
      {
        latitude: 58.628013,
        longitude: 91.44016,
      },
      {
        latitude: 73.476735,
        longitude: -157.81766,
      },
      {
        latitude: 66.996439,
        longitude: 52.065162,
      },
      {
        latitude: 65.728097,
        longitude: 114.819064,
      },
      {
        latitude: 83.935693,
        longitude: 133.815931,
      },
      {
        latitude: 43.845834,
        longitude: 12.355556,
      },
      {
        latitude: 43.769555,
        longitude: 11.255889,
      },
      {
        latitude: 38.971598,
        longitude: 87.343921,
      },
      {
        latitude: 48.468747,
        longitude: 33.730643,
      },
      {
        latitude: 31.816215,
        longitude: 2.265802,
      },
      {
        latitude: -6.299716,
        longitude: 25.996269,
      },
      {
        latitude: -22.903482,
        longitude: 17.207207,
      },
      {
        latitude: 40.641857,
        longitude: 45.427143,
      },
    ]

    const points = locations.map((entry) => ({
      lat: entry.latitude,
      lng: entry.longitude,
    }))
    const MAX_CONCURRENT_ARCS = 5
    const arcsData = []
    const ringsData = []
    // Array to hold the rings
    locations.forEach((source, idx) => {
      let availableIndexes = new Set(locations.map((_, index) => index))
      availableIndexes.delete(idx)
      availableIndexes = [...availableIndexes]
      const randomIndex = Math.floor(Math.random() * availableIndexes.length)
      const target = locations[availableIndexes[randomIndex]]
      const animationDuration = Math.random() * 15000 + 5000
      // between 5 to 20 seconds
      const initialDelay =
        (animationDuration / MAX_CONCURRENT_ARCS) * (idx % MAX_CONCURRENT_ARCS)
      // stagger the start times
      arcsData.push({
        startLat: source.latitude,
        startLng: source.longitude,
        endLat: target.latitude,
        endLng: target.longitude,
        color: [bluetransparent, lightredTransparent, lightGreenTransparent],
        arcDashLength: Math.random() * 0.4 + 0.6,
        arcAltitude: 0.5,
        arcDashGap: Math.random(),
        arcDashAnimateTime: animationDuration,
        arcDashInitialGap: initialDelay / animationDuration,
      })
      // Add a ring for the destination
      ringsData.push({
        lat: target.latitude,
        lng: target.longitude,
        alt: 0.9,
        color: 'rgba(255,100,50,${1-idx/locations.length})',
      })
    })
    const RINGS_MAX_R = 0.5
    const RING_PROPAGATION_SPEED = 0.03
    // const FLIGHT_TIME = 10000;
    // const ARC_REL_LEN = 1;
    // const NUM_RINGS = 5;
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent)
    let globeWidth, globeHeight
    if (isMobile) {
      globeWidth = 'full'
      globeHeight = '450'
      // or any other preferred height for mobile
    } else {
      globeWidth = 'full'
      globeHeight = 'auto'
    }
    const world = Globe()
      .globeImageUrl('attractive.jpg')
      .width(globeWidth)
      .height(globeHeight)
      .hexPolygonsData(countries.features)
      .hexPolygonResolution(3)
      .hexPolygonMargin(0.3)
      .hexPolygonUseDots(true)
      .hexPolygonColor(() => getRandomGreenShade())
      .backgroundColor('white')
      .pointColor(() => lightBlueTransparent)
      .arcStroke(0.4) //ring stroke
      .pointRadius(0.1)
      .pointAltitude(0.05)
      .arcsData(arcsData)
      .arcColor('color')
      .arcDashLength((d) => d.arcDashLength)
      .arcAltitude(0.2)
      .arcDashGap((d) => d.arcDashGap)
      .arcDashAnimateTime((d) => d.arcDashAnimateTime)(
      document.getElementById('globeViz'),
    )
    const controls = world.controls()
    // Get the controls
    controls.enableZoom = false
    // Disable zooming
    // world.pointOfView({ distance: 1, lat: 40, lng: -100, azimuth: 30, polar: 30 });
    // world.pointOfView({ lat: 40, lng: -100, altitude: 1.5, polar: 40 });
    world.pointOfView({
      lat: 10,
      lng: -280,
      altitude: 1.9,
    })
    world.controls().autoRotate = true
    // Enable auto-rotation
    world.controls().autoRotateSpeed = 0.5
    // Set the rotation speed
    world.pointsData(points)
  })
