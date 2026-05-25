> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3D/fr.md)

Voici la traduction en français de la documentation du nœud Preview3D :

Le nœud Preview3D est principalement utilisé pour prévisualiser les sorties de modèles 3D. Ce nœud accepte deux entrées : l'une est le `camera_info` provenant du nœud Load3D, et l'autre est le chemin vers le fichier du modèle 3D. Le chemin du fichier modèle doit se trouver dans le dossier `ComfyUI/output`.

**Formats pris en charge**
Actuellement, ce nœud prend en charge plusieurs formats de fichiers 3D, notamment `.gltf`, `.glb`, `.obj`, `.fbx` et `.stl`.

**Préférences des nœuds 3D**
Certaines préférences relatives aux nœuds 3D peuvent être configurées dans le menu des paramètres de ComfyUI. Veuillez vous référer à la documentation suivante pour les paramètres correspondants :
[Menu des paramètres](https://docs.comfy.org/interface/settings/3d)

## Entrées

| Nom du paramètre | Type          | Description                                  |
| ---------------- | ------------- | -------------------------------------------- |
| camera_info      | LOAD3D_CAMERA | Informations de la caméra                    |
| model_file       | LOAD3D_CAMERA | Chemin du fichier modèle sous `ComfyUI/output/` |

## Description de la zone Canvas

Actuellement, les nœuds liés à la 3D dans l'interface frontale de ComfyUI partagent le même composant canvas, donc leurs opérations de base sont largement cohérentes, à l'exception de quelques différences fonctionnelles.

> Le contenu et l'interface suivants sont principalement basés sur le nœud Load3D. Veuillez vous référer à l'interface réelle du nœud pour les fonctionnalités spécifiques.

La zone Canvas comprend diverses opérations de vue, telles que :

- Paramètres de la vue de prévisualisation (grille, couleur d'arrière-plan, vue de prévisualisation)
- Contrôle de la caméra : FOV, type de caméra
- Intensité de l'éclairage global : ajustement de l'éclairage
- Exportation du modèle : prend en charge les formats `GLB`, `OBJ`, `STL`
- etc.

![Interface utilisateur du nœud Load 3D](./asset/preview3d_canvas.jpg)

1. Contient plusieurs menus et menus cachés du nœud Load 3D
2. Axe d'opération de la vue 3D

### 1. Opérations de vue

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la lecture vidéo.
</video>

Opérations de contrôle de la vue :

- Clic gauche + glisser : Rotation de la vue
- Clic droit + glisser : Panoramique de la vue
- Molette centrale ou clic central + glisser : Zoom avant/arrière
- Axe de coordonnées : Changement de vue

### 2. Fonctions du menu de gauche

![Menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Dans la zone de prévisualisation, certains menus d'opération de vue sont cachés dans le menu. Cliquez sur le bouton du menu pour développer différents menus.

- 1. Scène : Contient la grille de la fenêtre de prévisualisation, la couleur d'arrière-plan, les paramètres de vignette
- 2. Modèle : Mode de rendu du modèle, matériau de texture, paramètres de direction vers le haut
- 3. Caméra : Bascule entre les vues orthographique et perspective, réglage de l'angle de perspective
- 4. Lumière : Intensité de l'éclairage global de la scène
- 5. Exportation : Exportation du modèle vers d'autres formats (GLB, OBJ, STL)

#### Scène

![menu scène](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Le menu Scène fournit quelques fonctions de paramétrage de base de la scène :

1. Afficher/Masquer la grille
2. Définir la couleur d'arrière-plan
3. Cliquer pour télécharger une image d'arrière-plan
4. Masquer la vignette de prévisualisation

#### Modèle

![Menu_Scène](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Le menu Modèle fournit quelques fonctions liées au modèle :

1. **Direction vers le haut** : Déterminer quel axe est la direction vers le haut pour le modèle
2. **Mode matériau** : Basculer les modes de rendu du modèle - Original, Normal, Filaire, Lineart

#### Caméra

![menu_modèle_menu_caméra](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Ce menu permet de basculer entre les vues orthographique et perspective, ainsi que de régler la taille de l'angle de perspective :

1. **Caméra** : Basculer rapidement entre les vues orthographique et perspective
2. **FOV** : Ajuster l'angle FOV

#### Lumière

![menu_modèle_menu_caméra](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Via ce menu, vous pouvez rapidement ajuster l'intensité de l'éclairage global de la scène

#### Exportation

![menu_exportation](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Ce menu offre la possibilité de convertir et d'exporter rapidement les formats de modèle