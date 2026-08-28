# ZImageFunControlnet

ZImageFunControlnet applique un réseau de contrôle spécialisé pour influencer le processus de génération ou d'édition d'images. Il utilise un modèle de base, un patch de modèle et un VAE, ce qui vous permet d'ajuster la force de l'effet de contrôle. Ce nœud peut fonctionner avec une image de base, une image d'inpainting et un masque pour des modifications plus ciblées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base utilisé pour le processus de génération. | MODEL | Oui | - |
| `modèle_patch` | Un modèle de patch spécialisé qui applique le guidage du réseau de contrôle. | MODEL_PATCH | Oui | - |
| `vae` | L'autoencodeur variationnel utilisé pour encoder et décoder les images. | VAE | Oui | - |
| `force` | La force de l'influence du réseau de contrôle. Les valeurs positives appliquent l'effet, tandis que les valeurs négatives peuvent l'inverser (défaut : 1.0). | FLOAT | Oui | -10.0 à 10.0 |
| `image` | Une image de base facultative pour guider le processus de génération. | IMAGE | Non | - |
| `image_de_repeinture` | Une image facultative utilisée spécifiquement pour l'inpainting de zones définies par un masque. | IMAGE | Non | - |
| `mask` | Un masque facultatif qui définit les zones d'une image à modifier ou à traiter par inpainting. | MASK | Non | - |

**Remarque :** Le paramètre `inpaint_image` est généralement utilisé en conjonction avec un `mask` pour spécifier le contenu de l'inpainting. Le comportement du nœud peut changer selon les entrées facultatives fournies (par exemple, utiliser `image` comme guide ou utiliser `image`, `mask` et `inpaint_image` pour l'inpainting).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec le patch de réseau de contrôle appliqué, prêt à être utilisé dans un pipeline d'échantillonnage. | MODEL |
| `positive` | Le conditionnement positif, potentiellement modifié par les entrées du réseau de contrôle. | CONDITIONING |
| `negative` | Le conditionnement négatif, potentiellement modifié par les entrées du réseau de contrôle. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
