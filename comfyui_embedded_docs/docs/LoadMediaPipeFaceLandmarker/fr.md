# Charger MediaPipe Face Landmarker

Ce nœud charge un modèle MediaPipe Face Landmarker v2, qui détecte les visages et les repères faciaux (tels que les yeux, le nez et la bouche) dans les images. Le modèle chargé regroupe deux variantes de détection (courte portée et pleine portée) ainsi que des données de maillage partagées, des blendshapes et une géométrie canonique utilisée pour l'analyse faciale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Modèle de détection de visage issu de models/detection/. | COMBO | Oui | Liste des noms de fichiers de modèles disponibles dans le répertoire `models/detection/` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `FACE_DETECTION_MODEL` | Objet modèle FaceLandmarker chargé contenant les deux variantes de détection (short/full), des ensembles de connexions pour la topologie faciale, des données canoniques et des patcheurs de modèle pour la gestion du GPU. | FACE_DETECTION_MODEL |

**Remarque :** La sortie est un objet complexe qui peut être utilisé par d'autres nœuds pour des tâches de détection de visage et d'extraction de repères. Elle contient deux variantes de détection : « short » pour la détection à courte portée et « full » pour la détection à pleine portée.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/fr.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
