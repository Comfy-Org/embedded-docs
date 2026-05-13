> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/fr.md)

Le nœud VAEDecode est conçu pour décoder des représentations latentes en images à l'aide d'un autoencodeur variationnel (VAE) spécifié. Il permet de générer des images à partir de représentations de données compressées, facilitant ainsi la reconstruction d'images à partir de leurs encodages dans l'espace latent.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `samples` | `LATENT`        | Le paramètre `samples` représente les représentations latentes à décoder en images. Il est essentiel au processus de décodage car il fournit les données compressées à partir desquelles les images sont reconstruites. |
| `vae`     | VAE             | Le paramètre `vae` spécifie le modèle d'autoencodeur variationnel à utiliser pour décoder les représentations latentes en images. Il est indispensable pour déterminer le mécanisme de décodage et la qualité des images reconstruites. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `image`   | `IMAGE`         | La sortie est une image reconstruite à partir de la représentation latente fournie, en utilisant le modèle VAE spécifié. |