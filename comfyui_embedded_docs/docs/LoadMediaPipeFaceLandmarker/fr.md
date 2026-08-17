# Charger MediaPipe Face Landmarker

Ce nœud charge un modèle MediaPipe Face Landmarker v2, capable de détecter les visages et les points de repère faciaux (comme les yeux, le nez et la bouche) dans les images. Le modèle chargé contient deux variantes de détection (courte et complète), ainsi que des données de maillage partagées, des blendshapes et une géométrie canonique pour l’analyse faciale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Modèle de détection faciale provenant de `models/detection/`. | COMBO | Oui | Liste des modèles disponibles dans le répertoire `models/detection/` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `FACE_DETECTION_MODEL` | Objet modèle MediaPipe Face Landmarker chargé contenant les deux variantes de détection (courte/complète), les données de maillage et de blendshapes partagées, la géométrie canonique, les ensembles de connexions topologiques faciales et les correcteurs de modèle pour la gestion du GPU. | FACE_DETECTION_MODEL |

**Remarque :** La sortie est un objet complexe pouvant être utilisé par d’autres nœuds pour des tâches de détection faciale et d’extraction de points de repère. Elle contient deux variantes de détection : « courte » pour la détection rapprochée et « complète » pour la détection à pleine portée.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/fr.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
