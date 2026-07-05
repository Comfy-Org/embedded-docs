# Images de référence HiDream-O1

Voici la traduction en français de la documentation du nœud ComfyUI :

## Aperçu

Attachez des images de référence aux conditionnements positif et négatif. Ce nœud vous permet de fournir une ou plusieurs images de référence qui seront utilisées pour guider le processus de génération d'images, que ce soit pour une édition basée sur une instruction ou pour une personnalisation pilotée par un sujet.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Le conditionnement positif auquel attacher les images de référence. | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif auquel attacher les images de référence. | CONDITIONING | Oui | - |
| `images` | Images de référence. 1 image permet l'édition basée sur une instruction ; 2 à 10 images permettent la personnalisation multi-référence pilotée par un sujet. | IMAGE | Oui | 1 à 10 images |

**Remarque sur le paramètre `images` :** Il s'agit d'une entrée à croissance automatique qui accepte entre 1 et 10 images. Les images sont étiquetées `image_1` à `image_10`. Vous devez fournir au moins 1 image. Le nombre d'images détermine le mode de fonctionnement : une seule image est utilisée pour les instructions d'édition, tandis que plusieurs images (2 à 10) sont utilisées pour la personnalisation pilotée par un sujet.


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif avec les images de référence attachées. | CONDITIONING |
| `negative` | Le conditionnement négatif avec les images de référence attachées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/fr.md)

---
**Source fingerprint (SHA-256):** `b14a8fc2acd44618370bd7e94758d469ff37530f2e19498a6c72ee3748559303`
