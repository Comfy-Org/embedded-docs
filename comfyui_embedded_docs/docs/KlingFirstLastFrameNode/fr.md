# Kling 3.0 Première-Dernière-Image en Vidéo

Ce nœud utilise le modèle Kling 3.0 pour générer une vidéo. Il crée la vidéo à partir d'une invite textuelle, d'une durée spécifiée et de deux images fournies : une image de début et une image de fin. Le nœud peut également générer un fichier audio d'accompagnement pour la vidéo.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Paramètres du modèle et de génération. La sélection de cette option révèle un paramètre `resolution` imbriqué. | COMBO | Non | `"kling-v3"` |
| `prompt` | La description textuelle qui guide la génération de la vidéo. Doit contenir entre 1 et 2500 caractères. | STRING | Oui | N/A |
| `durée` | La durée de la vidéo en secondes (par défaut : 5). | INT | Non | 3 à 15 |
| `première image` | L'image de départ pour la vidéo. Doit faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1. | IMAGE | Oui | N/A |
| `dernière image` | L'image de fin pour la vidéo. Doit faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1. | IMAGE | Oui | N/A |
| `générer l'audio` | Contrôle si la génération d'un fichier audio pour la vidéo est activée (par défaut : True). | BOOLEAN | Non | N/A |
| `seed` | Le paramètre `seed` contrôle si le nœud doit être exécuté à nouveau ; les résultats ne sont pas déterministes, quelle que soit la valeur de `seed` (par défaut : 0). | INT | Non | 0 à 2147483647 |

### Entrées Kling V3

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | La résolution de la vidéo générée (par défaut : `"1080p"`). | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` |

**Remarque :** Les images `first_frame` et `end_frame` doivent faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1 pour que le nœud fonctionne correctement. Le paramètre `prompt` doit contenir entre 1 et 2500 caractères. L'option `resolution` correspond à un mode de génération Kling : `"4k"`, `"1080p"` (pro) et `"720p"` (standard).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`
