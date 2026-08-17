# ZImageFunControlnet

Le nœud ZImageFunControlnet applique un réseau de contrôle spécialisé pour influencer le processus de génération ou d'édition d’images. Il utilise un modèle de base, un patch de modèle et un VAE, vous permettant d’ajuster la force de l’effet de contrôle. Ce nœud peut fonctionner avec une image de base, une image d’inpainting et un masque pour des modifications plus ciblées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de base utilisé pour le processus de génération. | MODEL | Oui | - |
| `model_patch` | Un modèle de patch spécialisé qui applique les directives du réseau de contrôle. | MODEL_PATCH | Oui | - |
| `vae` | L’autoencodeur variationnel utilisé pour encoder et décoder les images. | VAE | Oui | - |
| `strength` | La force de l’influence du réseau de contrôle. Les valeurs positives appliquent l’effet, tandis que les valeurs négatives peuvent l’inverser (par défaut : 1.0). | FLOAT | Oui | -10.0 à 10.0 |
| `image` | Une image de base facultative pour guider le processus de génération. | IMAGE | Non | - |
| `inpaint_image` | Une image facultative utilisée spécifiquement pour l’inpainting des zones définies par un masque. | IMAGE | Non | - |
| `mask` | Un masque facultatif qui définit les zones de l’image à éditer ou à remplir (inpainting). | MASK | Non | - |

**Remarque :** Le paramètre `inpaint_image` est généralement utilisé en conjonction avec un `mask` pour spécifier le contenu à remplir (inpainting). Le comportement du nœud peut changer selon les entrées facultatives fournies (par exemple, utiliser `image` pour le guidage ou utiliser `image`, `mask` et `inpaint_image` pour l’inpainting).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec le patch de réseau de contrôle appliqué, prêt à être utilisé dans un pipeline d’échantillonnage. | MODEL |
| `positive` | Le conditionnement positif, potentiellement modifié par les entrées du réseau de contrôle. | CONDITIONING |
| `negative` | Le conditionnement négatif, potentiellement modifié par les entrées du réseau de contrôle. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
