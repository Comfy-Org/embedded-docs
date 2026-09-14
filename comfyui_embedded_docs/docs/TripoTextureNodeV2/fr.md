# TripoTextureNodeV2

Ce nœud ajoute des textures à un modèle 3D existant issu d’un flux de travail Tripo, identifié par un ID de tâche provenant d’une étape de génération précédente. Il peut produire des cartes de matières PBR ou une texture de couleur unie, et le résultat peut être guidé par un prompt textuel, une image de style ou des images de référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|------------------|--------|-------|
| `model_task_id` | ID de tâche du modèle source produit par un nœud Tripo antérieur (génération de modèle ou segmentation de modèle). | MODEL_TASK_ID / SEGMENT_TASK_ID | Oui | - |
| `pbr` | Cartes de matières PBR (couleur de base, métallique, rugosité, normale) ; désactivé donne une texture de couleur unie. (par défaut : true) | BOOLEAN | Non | true<br>false |
| `texture_seed` | Graine utilisée pour la génération de texture. (par défaut : 42) Entrée avancée. | INT | Non | 0 à 2147483647 |
| `texture_quality` | Qualité des textures générées. `detailed` = textures HD, `extreme` = textures Ultra 8K. (par défaut : "standard") Entrée avancée. | COMBO | Non | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Mode d’alignement des textures sur le modèle. (par défaut : "original_image") Entrée avancée. | COMBO | Non | "original_image"<br>"geometry" |
| `texture_prompt` | Guidage textuel facultatif pour la texturation. En pratique, requis pour les modèles importés (Tripo : Import Model), qui n’ont pas d’image source à partir de laquelle déduire les couleurs. Ne peut pas être combiné avec des images de référence. (par défaut : vide) | STRING | Non | - |
| `model_version` | Modèle de texture : v3.0 pour les maillages générés avec v3.x, v2.5 pour les maillages générés avec v2.5. (par défaut : v3_0_20250812) | COMBO | Non | Versions du modèle de texture Tripo, par défaut "v3_0_20250812" |
| `style_image` | Image de référence pour le style artistique des textures. Utilisée uniquement avec `texture_prompt`. | IMAGE | Non | - |
| `reference` | Images de référence guidant les textures. Ne peut pas être combiné avec `texture_prompt` ou `style_image`. (par défaut : "none") | DYNAMIC_COMBO | Non | "none"<br>"image"<br>"multiview" |
| `part_names` | Noms de parties séparés par des virgules, issus de Tripo : Segment Model, à texturer. Une valeur vide applique une texture à chaque partie. (par défaut : vide) Entrée avancée. | STRING | Non | - |

### Entrées de référence d’image

Affichées lorsque `reference` est défini sur "image".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|------------------|--------|-------|
| `reference_image` | Image de référence unique que les textures doivent suivre. | IMAGE | Oui | - |

### Entrées de référence multivue

Affichées lorsque `reference` est défini sur "multiview".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|------------------|--------|-------|
| `image_front` | Vue de face (0°). | IMAGE | Oui | - |
| `image_left` | Vue de gauche (90°). | IMAGE | Oui | - |
| `image_back` | Vue arrière (180°). | IMAGE | Oui | - |
| `image_right` | Vue de droite (270°). | IMAGE | Oui | - |

**Remarques sur les contraintes des paramètres :**

- Les images de référence (modes de référence "image" ou "multiview") ne peuvent pas être combinées avec `texture_prompt` ou `style_image`.
- `style_image` nécessite qu’un `texture_prompt` soit fourni.
- Lorsqu’aucun `texture_prompt` n’est fourni, le modèle source doit provenir d’une tâche de type text-to-model, image-to-model, multiview-to-model ou texture-model. Les modèles sans image source (modèles importés, segmentés, complétés ou retopologisés) nécessitent un `texture_prompt`, car Tripo n’accepte les images de référence que pour les modèles qu’il a lui-même générés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|------------------|
| `model task_id` | ID de tâche de l’opération de texturation, qui peut être transmis à d’autres nœuds Tripo. | MODEL_TASK_ID |
| `GLB` | Modèle texturé au format GLB. Vide lorsque la source est un maillage quadrangulaire ou un import FBX. | FILE_3D_GLB |
| `FBX` | Modèle texturé au format FBX. Tripo renvoie du FBX pour les maillages quadrangulaires et les imports FBX ; vide sinon. | FILE_3D_FBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`
