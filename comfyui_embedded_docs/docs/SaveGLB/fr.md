# SaveGLB

Le nœud SaveGLB enregistre des données de maillage 3D ou des fichiers 3D dans le répertoire de sortie. Il accepte des données de maillage ou divers formats de fichiers 3D (GLB, GLTF, OBJ, FBX, STL, USDZ) et les exporte avec un préfixe de nom de fichier spécifié. Lors de l'enregistrement de données de maillage, il peut gérer plusieurs maillages et ajoute automatiquement les métadonnées du workflow aux fichiers lorsque les métadonnées sont activées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `maillage` | Maillage ou fichier 3D à enregistrer. Accepte les données de maillage ou les formats de fichiers 3D incluant GLB, GLTF, OBJ, FBX, STL et USDZ | MESH ou FILE3D | Oui | - |
| `préfixe_du_nom_de_fichier` | Le préfixe pour le nom du fichier de sortie (par défaut : "3d/ComfyUI") | STRING | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `ui` | Affiche les fichiers 3D enregistrés dans l'interface utilisateur avec les informations de nom de fichier, sous-dossier et type | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/fr.md)

---
**Source fingerprint (SHA-256):** `bd36600185aeb793cd4e9f37f3b4464267cb36f451fdcf71aff83077bb8c3f53`
