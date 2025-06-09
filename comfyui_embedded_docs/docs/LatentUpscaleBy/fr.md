
Le nœud LatentUpscaleBy est conçu pour agrandir les représentations latentes des images. Il permet l'ajustement du facteur d'échelle et de la méthode d'agrandissement, offrant une flexibilité dans l'amélioration de la résolution des échantillons latents.

## Entrées

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | La représentation latente des images à agrandir. Ce paramètre est crucial pour déterminer les données d'entrée qui subiront le processus d'agrandissement. |
| `upscale_method` | COMBO[STRING] | Spécifie la méthode utilisée pour agrandir les échantillons latents. Le choix de la méthode peut affecter de manière significative la qualité et les caractéristiques de la sortie agrandie. |
| `scale_by`    | `FLOAT`      | Détermine le facteur par lequel les échantillons latents sont agrandis. Ce paramètre influence directement la résolution de la sortie, permettant un contrôle précis du processus d'agrandissement. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La représentation latente agrandie, prête pour des tâches de traitement ou de génération ultérieures. Cette sortie est essentielle pour améliorer la résolution des images générées ou pour des opérations de modèle ultérieures. |
