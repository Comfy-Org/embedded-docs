# Tripo : Texturer le modèle (hérité)

Ce nœud est marqué comme obsolète (legacy) dans la source ; son nom d’affichage est « Tripo: Texture model (Legacy) ». Les tableaux de paramètres de la documentation existante restent exacts vis-à-vis de la source actuelle. Ils sont conservés et le statut legacy est signalé dans la vue d’ensemble.

Le nœud Tripo: Texture model (Legacy) ajoute des textures à un modèle 3D Tripo existant via l’API Tripo. Il prend l’ID de tâche d’un modèle créé par un autre nœud Tripo et renvoie un modèle GLB ou FBX texturé une fois la tâche de texturation terminée. Vous pouvez contrôler les cartes de matériau, la qualité des textures, l’alignement et la graine, et guider les textures avec une consigne textuelle, une image de style ou des images de référence. Ce nœud est une version héritée de l’outil de texturation.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | ID de tâche Tripo du modèle à texturer. Accepte les ID de tâche de modèle et les ID de tâche de segmentation. | MODEL_TASK_ID, SEGMENT_TASK_ID | Oui | - |
| `texture` | Ignoré : ce nœud génère toujours des textures. Conservé pour les anciens workflows. (par défaut : True) | BOOLEAN | Non | true<br>false |
| `pbr` | Cartes de matériau PBR (couleur de base, métallique, rugosité, normale) ; désactivé donne une texture de couleur unie. (par défaut : True) | BOOLEAN | Non | true<br>false |
| `texture_seed` | Graine aléatoire pour la génération de textures. (par défaut : 42) | INT | Non | 0 – 2147483647 |
| `texture_quality` | Qualité de résolution des textures : detailed = textures HD, extreme = textures 8K Ultra. (par défaut : "standard"). Coût approximatif : standard $0.10, detailed $0.20, extreme $0.30. | COMBO | Non | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Méthode utilisée pour aligner les textures générées sur le modèle. (par défaut : "original_image") | COMBO | Non | "original_image"<br>"geometry" |
| `texture_prompt` | Consigne textuelle facultative pour la texturation. En pratique, requis pour les modèles importés (Tripo: Import Model), qui ne comportent aucune image source à partir de laquelle déduire les couleurs. Ne peut pas être combiné avec des images de référence. (par défaut : "") | STRING | Non | - |
| `model_version` | Modèle de texture : v3.0 pour les maillages générés avec v3.x, v2.5 pour les maillages générés avec v2.5. (par défaut : v3.0_20250812) | COMBO | Non | Plusieurs options disponibles |
| `style_image` | Image de référence pour le style artistique des textures. Utilisée uniquement avec `texture_prompt`. | IMAGE | Non | - |
| `reference` | Images de référence guidant les textures. Ne peut pas être combiné avec `texture_prompt` ou `style_image`. (par défaut : "none") | DYNAMIC_COMBO | Non | "none"<br>"image"<br>"multiview" |
| `part_names` | Noms de parties séparés par des virgules provenant de Tripo: Segment Model à texturer. Une valeur vide texture toutes les parties. (par défaut : "") | STRING | Non | - |

### Entrées de référence `image`

Ces entrées sont disponibles lorsque `reference` est défini sur `"image"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_image` | Image de référence unique que les textures doivent suivre. | IMAGE | Oui | - |

### Entrées de référence `multiview`

Ces entrées sont disponibles lorsque `reference` est défini sur `"multiview"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image_front` | Vue de face (0°). | IMAGE | Oui | - |
| `image_left` | Vue de gauche (90°). | IMAGE | Oui | - |
| `image_back` | Vue arrière (180°). | IMAGE | Oui | - |
| `image_right` | Vue de droite (270°). | IMAGE | Oui | - |

**Remarque :** Les modes de référence `"image"` et `"multiview"` ne peuvent pas être combinés avec un `texture_prompt` non vide ni avec `style_image`. L’entrée `style_image` nécessite un `texture_prompt` non vide. Lorsque `texture_prompt` est laissé vide, le modèle source doit déjà disposer de sa propre image source (par exemple, les modèles produits par text-to-model, image-to-model, multiview-to-model ou une tâche de texturation antérieure). Les modèles qui ne comportent aucune image source — comme les modèles importés, segmentés, terminés ou retopologisés — doivent être texturés avec un `texture_prompt` ; les images de référence ne sont acceptées que pour les modèles que l’API Tripo a générés elle-même. L’entrée `part_names` peut être laissée vide pour texturer toutes les parties.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le fichier de modèle généré (uniquement pour la compatibilité ascendante). | STRING |
| `model task_id` | L’ID de la tâche de génération de texture terminée, utilisable comme entrée pour d’autres nœuds Tripo. | MODEL_TASK_ID |
| `GLB` | Le modèle texturé généré au format GLB. Vide lorsque la source est un maillage quadrangulaire ou un import FBX. | FILE3DGLB |
| `FBX` | Le modèle texturé généré au format FBX. Tripo renvoie du FBX pour les maillages quadrangulaires et les imports FBX ; vide sinon. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
