> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/fr.md)

Le nœud **LatentUpscaleBy** est conçu pour le suréchantillonnage des représentations latentes d'images. Il permet d'ajuster le facteur d'échelle et la méthode de suréchantillonnage, offrant ainsi une flexibilité pour améliorer la résolution des échantillons latents.

## Entrées

| Paramètre | Type de données | Description |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | La représentation latente des images à suréchantillonner. Ce paramètre est essentiel pour déterminer les données d'entrée qui subiront le processus de suréchantillonnage. |
| `méthode_de_mise_à_l'échelle` | COMBO[STRING] | Spécifie la méthode utilisée pour le suréchantillonnage des échantillons latents. Le choix de la méthode peut affecter considérablement la qualité et les caractéristiques de la sortie suréchantillonnée. |
| `mise_à_l'échelle_par`    | `FLOAT`      | Détermine le facteur par lequel les échantillons latents sont mis à l'échelle. Ce paramètre influence directement la résolution de la sortie, permettant un contrôle précis du processus de suréchantillonnage. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La représentation latente suréchantillonnée, prête pour d'autres traitements ou tâches de génération. Cette sortie est essentielle pour améliorer la résolution des images générées ou pour les opérations ultérieures du modèle. |