# Load3DAdvanced

Ce nœud charge un fichier de modèle 3D depuis votre répertoire d'entrée ComfyUI et fournit les données du modèle ainsi que les informations de la caméra et de la fenêtre d'affichage. Il prend en charge les formats de fichiers 3D courants et vous permet de spécifier les dimensions de l'image de sortie pour le rendu.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_file` | Le fichier de modèle 3D à charger. Sélectionnez "none" pour ignorer le chargement d'un modèle. | STRING | Oui | `"none"`<br>Liste des fichiers 3D disponibles dans le répertoire input/3d |
| `viewport_state` | L'état actuel de la fenêtre d'affichage contenant les informations de la caméra et du modèle provenant du visualiseur 3D. | LOAD3D | Oui | - |
| `width` | La largeur de l'image de sortie en pixels (par défaut : 1024) | INT | Oui | Min : 1<br>Max : 4096<br>Pas : 1 |
| `height` | La hauteur de l'image de sortie en pixels (par défaut : 1024) | INT | Oui | Min : 1<br>Max : 4096<br>Pas : 1 |

**Remarques sur les paramètres :**
- Le paramètre `model_file` n'affiche que les fichiers avec les extensions suivantes : .gltf, .glb, .obj, .fbx, .stl
- Les fichiers doivent être placés dans le répertoire `input/3d` de votre installation ComfyUI
- Si `model_file` est défini sur "none", aucune donnée de modèle 3D ne sera chargée (la sortie `model_3d` sera vide)

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `model_3d_info` | Les données du modèle 3D chargé, ou vides si aucun fichier de modèle n'a été sélectionné | FILE3DANY |
| `camera_info` | Informations sur le modèle 3D chargé provenant de l'état de la fenêtre d'affichage | LOAD3DMODELINFO |
| `width` | Informations de la caméra provenant de l'état de la fenêtre d'affichage | LOAD3DCAMERA |
| `height` | La largeur spécifiée de l'image de sortie | INT |
| `height` | La hauteur spécifiée de l'image de sortie | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `fdacea8abf627621150e1196743e36f61534333837c33cc9a7416a6d11700c4d`
