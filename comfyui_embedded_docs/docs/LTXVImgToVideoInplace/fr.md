Le nœud LTXVImgToVideoInplace conditionne une représentation latente vidéo en encodant une image d'entrée dans ses trames initiales. Il fonctionne en utilisant un VAE pour encoder l'image dans l'espace latent, puis en la fusionnant avec les échantillons latents existants selon une force spécifiée. Cela permet à une image de servir de point de départ ou de signal de conditionnement pour la génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent. | VAE | Oui | - |
| `image` | L'image d'entrée à encoder et à utiliser pour conditionner le latent vidéo. | IMAGE | Oui | - |
| `latent` | La représentation latente vidéo cible à modifier. | LATENT | Oui | - |
| `force` | Contrôle la force de fusion de l'image encodée dans le latent. Une valeur de 1.0 remplace complètement les trames initiales, tandis que des valeurs plus faibles les fusionnent. (par défaut : 1.0) | FLOAT | Non | 0.0 - 1.0 |
| `contournement` | Ignorer le conditionnement. Lorsque cette option est activée, le nœud renvoie le latent d'entrée inchangé. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** L'`image` sera automatiquement redimensionnée pour correspondre aux dimensions spatiales requises par le `vae` pour l'encodage, en fonction de la largeur et de la hauteur de l'entrée `latent`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | La représentation latente vidéo modifiée. Elle contient les échantillons mis à jour et un `noise_mask` qui applique la force de conditionnement aux trames initiales. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/fr.md)

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
