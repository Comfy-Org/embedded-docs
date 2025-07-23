Le nœud Preview3D est principalement utilisé pour prévisualiser la sortie des modèles 3D. Ce nœud prend deux entrées : l'une est le `camera_info` du nœud Load3D, l'autre est le chemin du fichier du modèle 3D. Le chemin du fichier du modèle doit se trouver dans le dossier `ComfyUI/output`.

**Formats pris en charge**
Actuellement, ce nœud prend en charge plusieurs formats de fichiers 3D, y compris `.gltf`, `.glb`, `.obj`, `.fbx` et `.stl`.

**Préférences du nœud 3D**
Certaines préférences liées aux nœuds 3D peuvent être configurées dans le menu des paramètres de ComfyUI. Veuillez consulter la documentation suivante pour les réglages correspondants :
[Menu des paramètres](https://docs.comfy.org/interface/settings/3d)

## Entrées

| Nom du paramètre | Type           | Description                                                        |
|------------------|----------------|--------------------------------------------------------------------|
| camera_info      | LOAD3D_CAMERA  | Informations de la caméra                                          |
| model_file       | LOAD3D_CAMERA  | Chemin du fichier du modèle dans `ComfyUI/output/`                 |

## Description de la zone Canevas (Canvas)

Actuellement, les nœuds liés à la 3D dans l’interface ComfyUI partagent le même composant de canevas, donc leurs opérations de base sont pour la plupart cohérentes, à l’exception de quelques différences fonctionnelles.

> Le contenu et l’interface suivants sont principalement basés sur le nœud Load3D. Veuillez vous référer à l’interface réelle du nœud pour les fonctionnalités spécifiques.

La zone Canvas comprend diverses opérations de vue, telles que :

- Paramètres d’aperçu (grille, couleur de fond, aperçu)
- Contrôle de la caméra : FOV, type de caméra
- Intensité de l’éclairage global : ajuster la lumière
- Exportation de modèle : prend en charge les formats `GLB`, `OBJ`, `STL`
- etc.

![UI du nœud Load 3D](./asset/preview3d_canvas.jpg)

1. Contient plusieurs menus et menus cachés du nœud Load 3D
2. Axe d’opération de vue 3D

### 1. Opérations de vue

<video controls width="640" height="360">
  <source src="../Load3D/asset/view_operations.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la lecture vidéo.
</video>

Opérations de contrôle de la vue :

- Clic gauche + glisser : faire pivoter la vue
- Clic droit + glisser : déplacer la vue
- Molette de la souris ou clic central : zoom avant/arrière
- Axe de coordonnées : changer de vue

### 2. Fonctions du menu de gauche

![Menu](../Load3D/asset/menu.webp)

Dans la zone d’aperçu, certains menus liés aux opérations de vue sont cachés dans le menu. Cliquez sur le bouton de menu pour développer les différents menus.

- 1. Scène (Scene) : comprend la grille de la fenêtre d’aperçu, la couleur de fond, les paramètres de la miniature
- 2. Modèle (Model) : mode de rendu du modèle, matériau de texture, réglage de la direction haut
- 3. Caméra (Camera) : basculer entre la vue orthographique et la vue en perspective, régler l’angle de perspective
- 4. Lumière (Light) : intensité de l’éclairage global de la scène
- 5. Exportation (Export) : exporter le modèle vers d’autres formats (GLB, OBJ, STL)

#### Scène (Scene)

![scene menu](../Load3D/asset/menu_scene.webp)

Le menu Scène propose quelques fonctions de configuration de base de la scène :

1. Afficher/Masquer la grille
2. Définir la couleur de fond
3. Télécharger une image de fond
4. Masquer la miniature d’aperçu

#### Modèle (Model)

![Menu_Scene](../Load3D/asset/menu_model.webp)

Le menu Modèle propose quelques fonctions liées au modèle :

1. **Direction haut (Up direction)** : détermine quel axe est la direction haut du modèle
2. **Mode matériel (Material mode)** : basculer entre les modes de rendu du modèle - Original, Normal, Fil de fer, Dessin au trait

#### Caméra (Camera)

![menu_modelmenu_camera](../Load3D/asset/menu_camera.webp)

Ce menu permet de basculer entre la vue orthographique et la vue en perspective, et de régler l’angle de perspective :

1. **Caméra (Camera)** : basculer rapidement entre la vue orthographique et la vue en perspective
2. **FOV** : ajuster l’angle FOV

#### Lumière (Light)

![menu_modelmenu_camera](../Load3D/asset/menu_light.webp)

Ce menu permet d’ajuster rapidement l’intensité de l’éclairage global de la scène

#### Exportation (Export)

![menu_export](../Load3D/asset/menu_export.webp)

Ce menu permet de convertir et d’exporter rapidement les formats de modèle
