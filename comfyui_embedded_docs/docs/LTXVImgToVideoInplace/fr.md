> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/fr.md)

Le nœud LTXVImgToVideoInplace conditionne une représentation latente vidéo en encodant une image d'entrée dans ses premières trames. Il fonctionne en utilisant un VAE pour encoder l'image dans l'espace latent, puis en la fusionnant avec les échantillons latents existants selon une intensité spécifiée. Cela permet à une image de servir de point de départ ou de signal de conditionnement pour la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent. |
| `image` | IMAGE | Oui | - | L'image d'entrée à encoder et à utiliser pour conditionner le latent vidéo. |
| `latent` | LATENT | Oui | - | La représentation latente vidéo cible à modifier. |
| `strength` | FLOAT | Non | 0.0 - 1.0 | Contrôle l'intensité de fusion de l'image encodée dans le latent. Une valeur de 1.0 remplace complètement les premières trames, tandis que des valeurs plus faibles les fusionnent. (par défaut : 1.0) |
| `bypass` | BOOLEAN | Non | - | Contourne le conditionnement. Lorsqu'il est activé, le nœud renvoie le latent d'entrée inchangé. (par défaut : False) |

**Note :** L'`image` sera automatiquement redimensionnée pour correspondre aux dimensions spatiales requises par le `vae` pour l'encodage, en fonction de la largeur et de la hauteur de l'entrée `latent`.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latent` | LATENT | La représentation latente vidéo modifiée. Elle contient les échantillons mis à jour et un `noise_mask` qui applique l'intensité de conditionnement aux premières trames. |
