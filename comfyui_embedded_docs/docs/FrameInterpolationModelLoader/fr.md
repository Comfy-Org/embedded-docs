# Charger un modèle d’interpolation d’images

Ce nœud charge un fichier de modèle d'interpolation de trames et le prépare pour une utilisation dans le flux de travail. Il détecte automatiquement si le fichier est un modèle FILM ou RIFE et configure le modèle pour le matériel disponible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_du_modèle` | Sélectionnez un modèle d'interpolation de trames à charger. Les modèles doivent être placés dans le dossier 'frame_interpolation'. | COMBO | Oui | Liste des fichiers de modèle dans le dossier `frame_interpolation` |

Remarque : Le nœud prend en charge les formats de modèle FILM et RIFE. Si le fichier sélectionné n'est pas dans un format reconnu, une erreur est générée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | Le modèle d'interpolation de trames chargé et configuré, prêt à être utilisé dans d'autres nœuds. | INTERP_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
