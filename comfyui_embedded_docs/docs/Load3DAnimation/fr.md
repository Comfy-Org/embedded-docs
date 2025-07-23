Le nœud Load3DAnimation est un nœud principal pour charger et traiter des fichiers de modèles 3D. Lors du chargement du nœud, il récupère automatiquement les ressources 3D disponibles dans `ComfyUI/input/3d/`. Vous pouvez également téléverser des fichiers 3D pris en charge pour les prévisualiser à l'aide de la fonction de téléversement.

> - La plupart des fonctions de ce nœud sont identiques à celles du nœud Load 3D, mais ce nœud prend en charge le chargement de modèles avec animations, et vous pouvez prévisualiser les animations correspondantes dans le nœud.
> - Le contenu de cette documentation est le même que celui du nœud Load3D, car à l’exception de la prévisualisation et de la lecture des animations, leurs capacités sont identiques.

**Formats pris en charge**
Actuellement, ce nœud prend en charge plusieurs formats de fichiers 3D, y compris `.gltf`, `.glb`, `.obj`, `.fbx` et `.stl`.

**Préférences du nœud 3D**
Certaines préférences liées aux nœuds 3D peuvent être configurées dans le menu des paramètres de ComfyUI. Veuillez consulter la documentation suivante pour les réglages correspondants :

[Menu des paramètres](https://docs.comfy.org/interface/settings/3d)

En plus des sorties habituelles du nœud, Load3D propose de nombreuses options liées à la vue 3D dans le menu de la zone d’aperçu.

## Entrées

| Nom du paramètre | Type           | Description                                                        | Par défaut | Plage         |
|------------------|----------------|--------------------------------------------------------------------|------------|---------------|
| model_file       | File Selection | Chemin du fichier du modèle 3D, prise en charge du téléversement, lit par défaut les fichiers dans `ComfyUI/input/3d/` | -          | Formats pris en charge |
| width            | INT            | Largeur de rendu du canevas                                        | 1024       | 1-4096        |
| height           | INT            | Hauteur de rendu du canevas                                        | 1024       | 1-4096        |

## Sorties

| Nom de sortie    | Type de donnée | Description                                                        |
|------------------|----------------|--------------------------------------------------------------------|
| image            | IMAGE          | Image rendue sur le canevas                                        |
| mask             | MASK           | Masque contenant la position actuelle du modèle                    |
| mesh_path        | STRING         | Chemin du fichier du modèle (dans le dossier `ComfyUI/input`)      |
| normal           | IMAGE          | Carte des normales                                                 |
| lineart          | IMAGE          | Sortie d’image de dessin au trait, le `edge_threshold` peut être ajusté dans le menu du modèle du canevas |
| camera_info      | LOAD3D_CAMERA  | Informations de la caméra                                          |
| recording_video  | VIDEO          | Vidéo enregistrée (uniquement si une vidéo existe)                 |

Aperçu de toutes les sorties :
![Démonstration des opérations de vue](../Load3D/asset/load3d_outputs.webp)

## Description de la zone Canevas (Canvas)

La zone Canvas du nœud Load3D contient de nombreuses opérations de vue, notamment :

- Paramètres d’aperçu (grille, couleur de fond, aperçu)
- Contrôle de la caméra : contrôle du FOV, type de caméra
- Intensité de l’éclairage global : ajuster l’intensité de la lumière
- Enregistrement vidéo : enregistrer et exporter des vidéos
- Exportation de modèle : prend en charge les formats `GLB`, `OBJ`, `STL`
- Etc.

![UI du nœud Load 3D](../Load3D/asset/load3d_ui.jpg)

1. Contient plusieurs menus et menus cachés du nœud Load 3D
2. Menu pour redimensionner la fenêtre d’aperçu et enregistrer la vidéo du canevas
3. Axe d’opération de vue 3D
4. Miniature d’aperçu
5. Réglage de la taille de l’aperçu, ajustez l’affichage de l’aperçu en définissant les dimensions puis en redimensionnant la fenêtre

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

Dans la zone d’aperçu, certains menus liés aux opérations de vue sont cachés dans le menu. Cliquez sur le bouton de menu pour développer les différents menus

- 1. Scène (Scene) : comprend la grille de la fenêtre d’aperçu, la couleur de fond, les paramètres de la miniature
- 2. Modèle (Model) : mode de rendu du modèle, matériaux de texture, réglage de la direction haut
- 3. Caméra (Camera) : basculer entre la vue orthographique et la vue en perspective, et régler l’angle de perspective
- 4. Lumière (Light) : intensité de l’éclairage global de la scène
- 5. Exportation (Export) : exporter le modèle vers d’autres formats (GLB, OBJ, STL)

#### Scène (Scene)

![scene menu](../Load3D/asset/menu_scene.webp)

Le menu Scène propose quelques fonctions de configuration de base de la scène

1. Afficher/Masquer la grille
2. Définir la couleur de fond
3. Télécharger une image de fond
4. Masquer la miniature d’aperçu

#### Modèle (Model)

![Menu_Scene](../Load3D/asset/menu_model.webp)

Le menu Modèle propose quelques fonctions liées au modèle

1. **Direction haut (Up direction)** : détermine quel axe est la direction haut du modèle
2. **Mode matériel (Material mode)** : basculer entre les modes de rendu du modèle - Original, Normal, Fil de fer, Dessin au trait

#### Caméra (Camera)

![menu_modelmenu_camera](../Load3D/asset/menu_camera.webp)

Ce menu permet de basculer entre la vue orthographique et la vue en perspective, et de régler l’angle de perspective

1. **Caméra (Camera)** : basculer rapidement entre la vue orthographique et la vue en perspective
2. **FOV** : ajuster l’angle FOV

#### Lumière (Light)

![menu_modelmenu_camera](../Load3D/asset/menu_light.webp)

Ce menu permet d’ajuster rapidement l’intensité de l’éclairage global de la scène

#### Exportation (Export)

![menu_export](../Load3D/asset/menu_export.webp)

Ce menu permet de convertir et d’exporter rapidement les formats de modèle

### 3. Fonctions du menu de droite

<video controls width="640" height="360">
  <source src="../Load3D/asset/recording.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la lecture vidéo.
</video>

Le menu de droite a deux fonctions principales :

1. **Réinitialiser le ratio de vue** : après avoir cliqué sur le bouton, la vue ajustera le ratio de la zone de rendu du canevas selon la largeur et la hauteur définies
2. **Enregistrement vidéo** : permet d’enregistrer les opérations de vue 3D actuelles en vidéo, permet l’importation et peut être exporté comme `recording_video` vers les nœuds suivants
