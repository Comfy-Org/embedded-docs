> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de base utilisé pour le processus de génération. |
| `model_patch` | MODEL_PATCH | Oui | - | Un modèle de patch spécialisé qui applique les directives du réseau de contrôle. |
| `vae` | VAE | Oui | - | L'autoencodeur variationnel utilisé pour encoder et décoder les images. |
| `strength` | FLOAT | Oui | -10.0 à 10.0 | L'intensité de l'influence du réseau de contrôle. Les valeurs positives appliquent l'effet, tandis que les valeurs négatives peuvent l'inverser (par défaut : 1.0). |
| `image` | IMAGE | Non | - | Une image de base optionnelle pour guider le processus de génération. |
| `inpaint_image` | IMAGE | Non | - | Une image optionnelle utilisée spécifiquement pour la restauration des zones définies par un masque. |
| `mask` | MASK | Non | - | Un masque optionnel qui définit les zones d'une image à modifier ou à restaurer. |

**Note :** Le paramètre `inpaint_image` est généralement utilisé conjointement avec un `mask` pour spécifier le contenu à restaurer. Le comportement du nœud peut changer en fonction des entrées optionnelles fournies (par exemple, utiliser `image` pour le guidage ou utiliser `image`, `mask` et `inpaint_image` pour la restauration).

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec le patch du réseau de contrôle appliqué, prêt à être utilisé dans un pipeline d'échantillonnage. |
| `positive` | CONDITIONING | Le conditionnement positif, potentiellement modifié par les entrées du réseau de contrôle. |
| `negative` | CONDITIONING | Le conditionnement négatif, potentiellement modifié par les entrées du réseau de contrôle. |
