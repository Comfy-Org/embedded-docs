# Enregistrer 3D (Avancé)

Enregistre un modèle 3D dans un fichier du répertoire de sortie de ComfyUI et produit un aperçu de la scène enregistrée. Il transmet également le modèle 3D, son placement dans la scène, les informations de caméra et les dimensions du viewport aux nœuds en aval. Lorsque les entrées de placement du modèle ou d'informations de caméra ne sont pas connectées, le nœud utilise les valeurs stockées dans l'état du viewport.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant d'un nœud 3D en amont. | FILE3D | Oui | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Préfixe utilisé pour le nom du fichier enregistré (par défaut : "3d/ComfyUI"). | STRING | Oui | Texte libre |
| `viewport_state` | État du viewport contenant les informations de caméra et de placement du modèle, généralement issues d'un nœud Load 3D. | LOAD3D | Oui | - |
| `model_3d_info` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde Y-up). Remplace le placement du modèle stocké dans `viewport_state` lorsque cette entrée est connectée. | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations de caméra du viewport : position, cible de visée, zoom et type. Remplace les informations de caméra stockées dans `viewport_state` lorsque cette entrée est connectée. | LOAD3DCAMERA | Non | - |
| `width` | Largeur de rendu du viewport en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `height` | Hauteur de rendu du viewport en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |

Remarque : `model_3d_info` et `camera_info` sont facultatifs. Lorsque l'une de ces entrées n'est pas connectée, le nœud utilise les valeurs correspondantes stockées dans `viewport_state`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de modèle 3D transmis depuis l'entrée. | FILE3D |
| `model_3d_info` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde Y-up). | LOAD3DMODELINFO |
| `camera_info` | Informations de caméra du viewport : position, cible de visée, zoom et type. | LOAD3DCAMERA |
| `width` | Valeur de largeur de rendu transmise depuis l'entrée. | INT |
| `height` | Valeur de hauteur de rendu transmise depuis l'entrée. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
