# Flux.2 [pro] Image

Génère une image avec Flux.2 [pro] via l'API BFL à partir d'un prompt et de dimensions de sortie explicites, éventuellement guidée par des images de référence.

**Remarque :** Ce nœud est marqué comme obsolète dans le code source.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt pour la génération ou l'édition de l'image. | STRING | Oui | - |
| `largeur` | Largeur de l'image générée en pixels (valeur par défaut : 1024). | INT | Oui | 256 à 2048 (pas de 32) |
| `hauteur` | Hauteur de l'image générée en pixels (valeur par défaut : 768). | INT | Oui | 256 à 2048 (pas de 32) |
| `graine` | Graine aléatoire utilisée pour créer le bruit (valeur par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `suréchantillonnage de l'invite` | Indique s'il faut effectuer un suréchantillonnage (upsampling) du prompt. Si cette option est active, le prompt est modifié automatiquement pour une génération plus créative (valeur par défaut : `True`). Il s'agit d'un réglage avancé. | BOOLEAN | Oui | True / False |
| `images` | Images de référence facultatives pour la génération image à image. Chaque image est réduite à un maximum de 2048x2048 pixels avant l'envoi. | IMAGE | Non | 0 à 9 images |

**Contraintes :**

* Connecter plus de 9 images de référence génère une erreur.
* La taille de sortie est facturée au mégapixel ; des valeurs `width` et `height` plus grandes coûtent donc plus cher.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ProImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `ffa3934abaa38e030eedf2624e7a91333e24a92d7ac89af8637e59d59341eb6d`
