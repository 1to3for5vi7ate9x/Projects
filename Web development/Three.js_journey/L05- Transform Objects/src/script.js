import './style.css'
import * as THREE from 'three'

//console.log('Hello from src/script.js')

// Canvas
const canvas = document.querySelector('canvas.webgl')

// Scene
const scene = new THREE.Scene()

//Creating one object and doing all tranformation on it 
/* Objects - Creating one object and doing all tranformation on it

const geometry = new THREE.BoxGeometry(1, 1, 1)
const material = new THREE.MeshBasicMaterial({ color: 0xff0000 })
const mesh = new THREE.Mesh(geometry, material)

//-----------------  Position ----------------------\\

// mesh.position.x = 0.7     // .position helps to move th3 object in different direction along the different axis
// mesh.position.y = -0.6
// mesh.position.z = 1

scene.add(mesh)

//console.log(mesh.position.length())  // # Tells the position of the object which is mesh itself from the centre or basically the length of vector.
//mesh.position.normalize() // # Reduces the vector length to 1 in all axis like x,y,z

mesh.position.set(0.7, -0.6, -1) // .set(x,y,z) sets the position on axis can directly set from here 

//Scale
// mesh.scale.x = 2
// mesh.scale.y = 0.5
// mesh.scale.z = 0.5
mesh.scale.set(2,0.5,0.5)  //Scale the size of the object we can do .scale.x = 1

//Rotation
mesh.rotation.reorder('YXZ') // We can set the order of rotation to be followed according to our needs 
//mesh.rotation.x = Math.PI * 0.25 // # Math.PI denotes the circular rotation we wanna make for example we can rotate half if we multiply pi with half
mesh.rotation.set(Math.PI*0.25,Math.PI*0.25,0) // Rotates the object on different axis
*/

//Group

const group = new THREE.Group()
group.rotation.y = Math.PI * 1
group.scale.set(0.5,0.5,0.5)
group.position.y = -1
scene.add(group)

const cube1 = new THREE.Mesh(
    new THREE.BoxGeometry(1,1,1),
    new THREE.MeshBasicMaterial({ color: 0xff0000 })
)
cube1.position.set(-2,0,0)
group.add(cube1)

const cube2 = new THREE.Mesh(
    new THREE.BoxGeometry(1,1,1),
    new THREE.MeshBasicMaterial({ color: 0x00ff00 })
)
group.add(cube2)

const cube3 = new THREE.Mesh(
    new THREE.BoxGeometry(1,1,1),
    new THREE.MeshBasicMaterial({ color: 0x0000ff })
)
cube3.position.set(2,0,0)
group.add(cube3)


// Axes helper
const axeshelper = new THREE.AxesHelper(0.5)
scene.add(axeshelper)

/**
 * Sizes
 */
const sizes = {
    width: 800,
    height: 600
}

/**
 * Camera
 */
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height)
//camera.position.z = 3
camera.position.set(0,0,3)
//camera.lookAt(mesh.position) // # Focus camera on the mesh aka object

scene.add(camera)

//console.log(mesh.position.distanceTo(camera.position))  // # Tells the distance of vector from the camera

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.render(scene, camera)