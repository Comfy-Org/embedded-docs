> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/fr.md)

Le nœud TrimVideoLatent supprime les images du début d'une représentation vidéo latente. Il prend un échantillon vidéo latent et retire un nombre spécifié d'images depuis le début, renvoyant la partie restante de la vidéo. Cela permet de raccourcir les séquences vidéo en supprimant les premières images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `échantillons` | LATENT | Oui | - | La représentation vidéo latente d'entrée contenant les images vidéo à rogner |
| `quantité de découpe` | INT | Oui | 0 à 99999 | Le nombre d'images à supprimer du début de la vidéo (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | LATENT | La représentation vidéo latente rognée, avec le nombre spécifié d'images supprimées du début |

---
**Source fingerprint (SHA-256):** `7fd482533d1f63219565a3a25776173c77c419fbf5086015d42136f5bfdfbed2`
