# Charger le modèle de corps SAM3D

Charge un modèle SAM3D Body à partir d'un fichier de points de contrôle (checkpoint) stocké dans le dossier de détection et le prépare pour une utilisation de détection de corps 3D. Le nœud charge les poids du modèle, détecte et applique les paramètres de quantification s'ils sont présents, et enveloppe le modèle pour une gestion automatique de la mémoire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Le fichier de points de contrôle (checkpoint) SAM3D Body à charger. Le fichier doit être placé dans le dossier de détection. | COMBO | Oui | Tous les fichiers de modèle disponibles dans le dossier de détection |

Remarque : Le fichier de modèle doit être situé dans le dossier de détection. Le chargement échoue avec une erreur si les clés du dictionnaire d'état du checkpoint ne correspondent pas à la structure du modèle SAM3D Body.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `sam3d_body_model` | Le modèle SAM3D Body chargé, enveloppé pour une gestion automatique de la mémoire entre GPU et CPU. Les poids de détection des mains sont supprimés, de sorte que le modèle est spécialisé pour la détection de corps uniquement. | SAM3D_BODY_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/fr.md)

---
**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`
