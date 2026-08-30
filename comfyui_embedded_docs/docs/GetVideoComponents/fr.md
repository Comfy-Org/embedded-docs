# Obtenir les composants vidéo

Le nœud Get Video Components extrait tous les éléments principaux d'un fichier vidéo. Il sépare la vidéo en images individuelles, extrait la piste audio et fournit la fréquence d'images, la profondeur de bits et l'espace colorimétrique de la vidéo. Cela vous permet de travailler avec chaque composant indépendamment pour un traitement ou une analyse ultérieure.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | La vidéo à partir de laquelle extraire les composants. | VIDEO | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images individuelles extraites de la vidéo sous forme d'images séparées. | IMAGE |
| `audio` | La piste audio extraite de la vidéo. | AUDIO |
| `ips` | La fréquence d'images de la vidéo en images par seconde. | FLOAT |
| `bit_depth` | La profondeur de bits de la vidéo. | COMBO |
| `color_space` | L'espace colorimétrique de la vidéo. | COMBO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/fr.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`
