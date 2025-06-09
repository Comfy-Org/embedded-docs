
Ce nœud est conçu pour encoder les images en une représentation dans l'espace latent en utilisant un modèle VAE spécifié. Il simplifie la complexité du processus d'encodage, offrant un moyen direct de transformer les images en leurs représentations latentes.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | Le paramètre 'pixels' représente les données d'image à encoder dans l'espace latent. Il joue un rôle crucial en déterminant la représentation latente de sortie en servant d'entrée directe pour le processus d'encodage. |
| `vae`     | VAE       | Le paramètre 'vae' spécifie le modèle d'Autoencodeur Variationnel à utiliser pour encoder les données d'image dans l'espace latent. Il est essentiel pour définir le mécanisme d'encodage et les caractéristiques de la représentation latente générée. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une représentation dans l'espace latent de l'image d'entrée, encapsulant ses caractéristiques essentielles sous une forme compressée. |
