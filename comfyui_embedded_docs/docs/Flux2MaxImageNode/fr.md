# Flux.2 [max] Image

Génère une image avec Flux.2 [max] via l'API BFL à partir d'un prompt et de dimensions de sortie explicites, éventuellement guidé par des images de référence. Il expose les mêmes entrées que Flux.2 [pro] Image.

**Remarque :** Ce nœud est marqué comme obsolète dans le code source.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt pour la génération ou la modification de l'image. | STRING | Oui | - |
| `largeur` | Largeur de l'image générée en pixels (valeur par défaut : 1024). | INT | Oui | 256 à 2048 (pas de 32) |
| `hauteur` | Hauteur de l'image générée en pixels (valeur par défaut : 768). | INT | Oui | 256 à 2048 (pas de 32) |
| `graine` | Graine aléatoire utilisée pour créer le bruit (valeur par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `suréchantillonnage de l'invite` | Indique s'il faut effectuer un suréchantillonnage du prompt. S'il est actif, le prompt est modifié automatiquement pour une génération plus créative (valeur par défaut : `True`). Il s'agit d'un réglage avancé. | BOOLEAN | Oui | True / False |
| `images` | Images de référence facultatives pour la génération image à image. Chaque image est réduite à au plus 2048x2048 pixels avant le téléversement. | IMAGE | Non | 0 à 9 images |

**Contraintes :**

* Connecter plus de 9 images de référence génère une erreur.
* La taille de sortie est facturée au mégapixel ; des valeurs plus grandes de `width` et `height` coûtent donc plus cher.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2MaxImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `cd540606835e7808861d9a96584731100b1bf9c996f18586fed39e8a2d32a29f`
