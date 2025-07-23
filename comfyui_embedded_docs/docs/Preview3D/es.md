El nodo Preview3D se utiliza principalmente para previsualizar la salida de modelos 3D. Este nodo recibe dos entradas: una es la `camera_info` del nodo Load3D y la otra es la ruta al archivo del modelo 3D. La ruta del archivo del modelo debe estar ubicada en la carpeta `ComfyUI/output`.

**Formatos soportados**
Actualmente, este nodo soporta varios formatos de archivos 3D, incluyendo `.gltf`, `.glb`, `.obj`, `.fbx` y `.stl`.

**Preferencias del nodo 3D**
Algunas preferencias relacionadas con los nodos 3D se pueden configurar en el menú de configuración de ComfyUI. Consulta el siguiente documento para ver los ajustes correspondientes:
[Menú de configuración](https://docs.comfy.org/interface/settings/3d)

## Entradas

| Nombre del parámetro | Tipo           | Descripción                                  |
| -------------------- | -------------- | -------------------------------------------- |
| camera_info          | LOAD3D_CAMERA  | Información de la cámara                     |
| model_file           | LOAD3D_CAMERA  | Ruta del archivo del modelo en `ComfyUI/output/` |

## Descripción del área de lienzo (Canvas)

Actualmente, los nodos relacionados con 3D en el frontend de ComfyUI comparten el mismo componente de canvas, por lo que sus operaciones básicas son en su mayoría consistentes, salvo algunas diferencias funcionales.

> El siguiente contenido e interfaz están basados principalmente en el nodo Load3D. Consulta la interfaz real del nodo para características específicas.

El área Canvas incluye varias operaciones de vista, como:

- Configuración de vista previa (cuadrícula, color de fondo, vista previa)
- Control de cámara: FOV, tipo de cámara
- Intensidad de iluminación global: ajustar la luz
- Exportación de modelo: soporta formatos `GLB`, `OBJ`, `STL`
- etc.

![UI del nodo Load 3D](./asset/preview3d_canvas.jpg)

1. Incluye varios menús y menús ocultos del nodo Load 3D
2. Eje de operaciones de vista 3D

### 1. Operaciones de vista

<video controls width="640" height="360">
  <source src="../Load3D/asset/view_operations.mp4" type="video/mp4">
  Tu navegador no soporta la reproducción de video.
</video>

Operaciones de control de vista:

- Clic izquierdo + arrastrar: rotar la vista
- Clic derecho + arrastrar: mover la vista
- Rueda del ratón o clic central: acercar/alejar
- Eje de coordenadas: cambiar de vista

### 2. Funciones del menú izquierdo

![Menu](../Load3D/asset/menu.webp)

En el área de previsualización, algunos menús relacionados con operaciones de vista están ocultos en el menú. Haz clic en el botón de menú para expandir los diferentes menús.

- 1. Escena (Scene): incluye cuadrícula de la ventana de previsualización, color de fondo, configuración de miniatura
- 2. Modelo (Model): modo de renderizado del modelo, material de textura, configuración de dirección superior
- 3. Cámara (Camera): cambiar entre vista ortográfica y perspectiva, ajustar el ángulo de perspectiva
- 4. Luz (Light): intensidad de iluminación global de la escena
- 5. Exportar (Export): exportar el modelo a otros formatos (GLB, OBJ, STL)

#### Escena (Scene)

![scene menu](../Load3D/asset/menu_scene.webp)

El menú Escena proporciona algunas funciones básicas de configuración de la escena:

1. Mostrar/ocultar cuadrícula
2. Establecer color de fondo
3. Subir imagen de fondo
4. Ocultar miniatura de previsualización

#### Modelo (Model)

![Menu_Scene](../Load3D/asset/menu_model.webp)

El menú Modelo proporciona algunas funciones relacionadas con el modelo:

1. **Dirección superior (Up direction)**: determina qué eje es la dirección superior del modelo
2. **Modo de material (Material mode)**: cambiar modos de renderizado del modelo - Original, Normal, Malla, Dibujo lineal

#### Cámara (Camera)

![menu_modelmenu_camera](../Load3D/asset/menu_camera.webp)

Este menú permite cambiar entre vistas ortográfica y perspectiva, y ajustar el ángulo de perspectiva:

1. **Cámara (Camera)**: cambiar rápidamente entre vistas ortográfica y perspectiva
2. **FOV**: ajustar el ángulo FOV

#### Luz (Light)

![menu_modelmenu_camera](../Load3D/asset/menu_light.webp)

A través de este menú puedes ajustar rápidamente la intensidad de la iluminación global de la escena

#### Exportar (Export)

![menu_export](../Load3D/asset/menu_export.webp)

Este menú permite convertir y exportar rápidamente formatos de modelo
