# Obtenir les composants vidéo

Le nœud **Obtenir les composants vidéo** extrait tous les éléments principaux d'un fichier vidéo. Il sépare la vidéo en images individuelles, extrait la piste audio et fournit les informations de fréquence d'images de la vidéo. Cela vous permet de travailler avec chaque composant de manière indépendante pour un traitement ou une analyse ultérieure.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | La vidéo dont extraire les composants. | VIDEO | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Les images individuelles extraites de la vidéo sous forme d'images séparées. | IMAGE |
| `ips` | La piste audio extraite de la vidéo. | AUDIO |
| `bit_depth` | La fréquence d'images de la vidéo en images par seconde. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/fr.md)

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`
