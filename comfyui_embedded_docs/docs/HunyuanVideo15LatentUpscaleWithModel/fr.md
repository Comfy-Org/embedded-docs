> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/fr.md)

Le nœud Hunyuan Video 15 Latent Upscale With Model augmente la résolution d'une représentation d'image latente. Il procède d'abord à un suréchantillonnage des échantillons latents vers une taille spécifiée en utilisant une méthode d'interpolation choisie, puis affine le résultat suréchantillonné à l'aide d'un modèle de suréchantillonnage spécialisé Hunyuan Video 1.5 pour en améliorer la qualité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Oui | N/A | Le modèle de suréchantillonnage latent Hunyuan Video 1.5 utilisé pour affiner les échantillons suréchantillonnés. |
| `samples` | LATENT | Oui | N/A | La représentation d'image latente à suréchantillonner. |
| `upscale_method` | COMBO | Non | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | L'algorithme d'interpolation utilisé pour l'étape initiale de suréchantillonnage (par défaut : `"bilinear"`). |
| `width` | INT | Non | 0 à 16384 | La largeur cible pour le latent suréchantillonné, en pixels. Une valeur de 0 calculera la largeur automatiquement en fonction de la hauteur cible et du rapport d'aspect original. La largeur finale de sortie sera un multiple de 16 (par défaut : 1280). |
| `height` | INT | Non | 0 à 16384 | La hauteur cible pour le latent suréchantillonné, en pixels. Une valeur de 0 calculera la hauteur automatiquement en fonction de la largeur cible et du rapport d'aspect original. La hauteur finale de sortie sera un multiple de 16 (par défaut : 720). |
| `crop` | COMBO | Non | `"disabled"`<br>`"center"` | Détermine comment le latent suréchantillonné est recadré pour s'adapter aux dimensions cibles. |

**Note sur les dimensions :** Si `width` et `height` sont tous deux définis sur 0, le nœud renvoie les `samples` d'entrée inchangés. Si une seule dimension est définie sur 0, l'autre dimension est calculée pour préserver le rapport d'aspect original. Les dimensions finales sont toujours ajustées pour être d'au moins 64 pixels et être divisibles par 16.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La représentation d'image latente suréchantillonnée et affinée par le modèle. |
