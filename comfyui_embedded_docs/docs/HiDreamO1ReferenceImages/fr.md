# Images de référence HiDream-O1

## Aperçu

Attachez des images de référence à la fois au conditionnement positif et négatif. Ce nœud vous permet de fournir de 1 à 10 images de référence ; une seule image est utilisée pour l'édition basée sur des instructions, tandis que plusieurs images (2-10) permettent la personnalisation par sujet.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Le conditionnement positif auquel attacher les images de référence. | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif auquel attacher les images de référence. | CONDITIONING | Oui | - |
| `images` | Images de référence. 1 image = édition par instructions ; 2-10 images = référence multiple. | IMAGE | Oui | 1 à 10 images |

**Remarque sur le paramètre `images` :** Il s'agit d'une entrée à croissance automatique qui accepte entre 1 et 10 images. Les images sont étiquetées `image_1` à `image_10`. Vous devez fournir au moins 1 image. Le nombre d'images détermine le mode de fonctionnement : une seule image est utilisée pour les instructions d'édition, tandis que plusieurs images (2-10) sont utilisées pour la personnalisation par sujet.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif avec les images de référence attachées. | CONDITIONING |
| `négatif` | Le conditionnement négatif avec les images de référence attachées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/fr.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
