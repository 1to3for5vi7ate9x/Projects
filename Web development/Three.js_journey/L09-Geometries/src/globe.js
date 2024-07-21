import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'


const canvas = document.querySelector('canvas.webgl')

// Sizes
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}

window.addEventListener('resize', () =>
{
    // Update sizes
    sizes.width = window.innerWidth
    sizes.height = window.innerHeight

    // Update camera
    camera.aspect = sizes.width / sizes.height
    camera.updateProjectionMatrix()

    // Update renderer
    renderer.setSize(sizes.width, sizes.height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

})


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10);
camera.position.z = 5
const renderer = new THREE.WebGLRenderer({
    canvas:  canvas
});

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0xffffff, 1)


// Globe creation (simplified)
const earthGroup = new THREE.Group()
earthGroup.rotation.z = -23.4 * Math.PI / 180
scene.add(earthGroup)

new OrbitControls(camera, renderer.domElement)
const loader = new THREE.TextureLoader()
const geometry = new THREE.IcosahedronGeometry(2.5, 12)
const material = new THREE.MeshStandardMaterial({
    map: loader.load("./attractive.jpg"),
})
const earthMesh = new THREE.Mesh(geometry, material)
earthGroup.add(earthMesh)

const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444)
scene.add(hemiLight)

// Render loop
const animate = () => {
    requestAnimationFrame(animate);

    earthMesh.rotation.y += 0.002;

    renderer.render(scene, camera);
};

animate();