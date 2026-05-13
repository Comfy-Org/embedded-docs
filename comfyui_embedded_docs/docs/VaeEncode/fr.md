> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/fr.md)

Ce nœud est conçu pour encoder des images dans une représentation d'espace latent à l'aide d'un modèle VAE spécifié. Il abstrait la complexité du processus d'encodage, offrant un moyen simple de transformer des images en leurs représentations latentes.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | Le paramètre `pixels` représente les données de l'image à encoder dans l'espace latent. Il joue un rôle crucial dans la détermination de la représentation latente de sortie en servant d'entrée directe pour le processus d'encodage. |
| `vae`     | VAE       | Le paramètre `vae` spécifie le modèle d'autoencodeur variationnel à utiliser pour encoder les données de l'image dans l'espace latent. Il est essentiel pour définir le mécanisme d'encodage et les caractéristiques de la représentation latente générée. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une représentation dans l'espace latent de l'image d'entrée, encapsulant ses caractéristiques essentielles sous une forme compressée. |