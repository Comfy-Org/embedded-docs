> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/fr.md)

Le nœud WanHuMoImageToVideo convertit des images en séquences vidéo en générant des représentations latentes pour les images vidéo. Il traite les entrées de conditionnement et peut incorporer des images de référence et des plongements audio pour influencer la génération vidéo. Le nœud produit en sortie des données de conditionnement modifiées et des représentations latentes adaptées à la synthèse vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Entrée de conditionnement positive qui guide la génération vidéo vers le contenu souhaité |
| `negative` | CONDITIONING | Oui | - | Entrée de conditionnement négative qui éloigne la génération vidéo du contenu indésirable |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images de référence dans l'espace latent |
| `width` | INT | Oui | 16 à MAX_RESOLUTION | Largeur des images vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur des images vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la séquence vidéo générée (par défaut : 97) |
| `batch_size` | INT | Oui | 1 à 4096 | Nombre de séquences vidéo à générer simultanément (par défaut : 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Non | - | Données d'encodage audio optionnelles qui peuvent influencer la génération vidéo basée sur le contenu audio |
| `ref_image` | IMAGE | Non | - | Image de référence optionnelle utilisée pour guider le style et le contenu de la génération vidéo |

**Remarque :** Lorsqu'une image de référence est fournie, elle est encodée et ajoutée aux conditionnements positif et négatif. Lorsqu'une sortie d'encodeur audio est fournie, elle est traitée et incorporée dans les données de conditionnement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec l'image de référence et/ou les plongements audio incorporés |
| `negative` | CONDITIONING | Conditionnement négatif modifié avec l'image de référence et/ou les plongements audio incorporés |
| `latent` | LATENT | Représentation latente générée contenant les données de la séquence vidéo |