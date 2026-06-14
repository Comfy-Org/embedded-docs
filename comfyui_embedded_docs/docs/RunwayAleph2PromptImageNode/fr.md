# Runway Aleph2 Prompt Image

Ce nœud ancre une image de guidage à un moment spécifique de la vidéo de sortie, contrôlant l'apparence de la vidéo éditée à cet instant. Connectez ce nœud à l'entrée `prompt_images` du nœud Runway Aleph2 Video to Video, et enchaînez plusieurs instances (jusqu'à 5) en utilisant l'entrée optionnelle `prompt_images`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image de guidage à placer au moment choisi de la vidéo de sortie. | IMAGE | Oui | - |
| `position` | Comment placer cette image sur la timeline de la vidéo de sortie. Choisissez entre un minutage absolu (secondes depuis le début) ou un minutage fractionnaire (pourcentage de la durée vidéo). | COMBO | Oui | `Absolute (seconds)`<br>`Fraction (0.0 to 1.0)` |
| `prompt_images` | Images de guidage optionnelles antérieures à chaîner avec celle-ci. Connectez la sortie d'un autre nœud Runway Aleph2 Prompt Image ici pour construire une chaîne allant jusqu'à 5 images de guidage. | PROMPT_IMAGE_CHAIN | Non | - |

**Détails du mode Position :**

Lorsque `position` est défini sur `Absolute (seconds)`, vous devez fournir une valeur `seconds` (par défaut : 0.0, plage : 0.0 à 30.0, pas : 0.1). Cela spécifie le moment exact en secondes depuis le début de la vidéo de sortie où cette image s'applique.

Lorsque `position` est défini sur `Fraction (0.0 to 1.0)`, vous devez fournir une valeur `fraction` (par défaut : 0.0, plage : 0.0 à 1.0, pas : 0.01). Cela spécifie l'emplacement dans la vidéo de sortie où cette image s'applique, sous forme de fraction de sa durée totale (0.0 = début, 1.0 = fin).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `prompt_images` | Une chaîne d'images de guidage pouvant être connectée à l'entrée `prompt_images` du nœud Runway Aleph2 Video to Video. | PROMPT_IMAGE_CHAIN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`
