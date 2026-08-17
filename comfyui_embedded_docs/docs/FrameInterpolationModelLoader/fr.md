# Charger un modèle d’interpolation d’images

## Aperçu

Ce nœud charge un modèle d'interpolation d'images depuis un fichier et le prépare pour une utilisation dans le workflow. Il détecte automatiquement le type de modèle (FILM ou RIFE) et le configure pour des performances optimales sur votre matériel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Sélectionnez un modèle d'interpolation d'images à charger. Les modèles doivent être placés dans le dossier 'frame_interpolation'. | COMBO | Oui | Liste des fichiers de modèles dans le dossier `frame_interpolation` |

Remarque : si le fichier sélectionné n'est pas un modèle d'interpolation d'images FILM ou RIFE reconnu, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | Le modèle d'interpolation d'images chargé et configuré, prêt à être utilisé dans d'autres nœuds. | INTERP_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
