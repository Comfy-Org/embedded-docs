# Hunyuan Video 15 Latent Upscale With Model

Le nœud Hunyuan Video 15 Latent Upscale With Model augmente la résolution d'une représentation d'image latente. Il met d'abord à l'échelle les échantillons latents à une taille spécifiée à l'aide d'une méthode d'interpolation choisie, puis affine le résultat mis à l'échelle à l'aide d'un modèle de mise à l'échelle spécialisé Hunyuan Video 1.5 pour améliorer la qualité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de mise à l'échelle latente Hunyuan Video 1.5 utilisé pour affiner les échantillons mis à l'échelle. | LATENT_UPSCALE_MODEL | Oui | N/A |
| `samples` | La représentation d'image latente à mettre à l'échelle. | LATENT | Oui | N/A |
| `upscale_method` | L'algorithme d'interpolation utilisé pour l'étape de mise à l'échelle initiale (par défaut : `"bilinear"`). | COMBO | Non | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | La largeur cible pour le latent mis à l'échelle, en pixels. Une valeur de 0 calculera automatiquement la largeur en fonction de la hauteur cible et du rapport hauteur/largeur d'origine. La largeur de sortie finale sera un multiple de 16 (par défaut : 1280). | INT | Non | 0 à 16384 (pas de 8) |
| `height` | La hauteur cible pour le latent mis à l'échelle, en pixels. Une valeur de 0 calculera automatiquement la hauteur en fonction de la largeur cible et du rapport hauteur/largeur d'origine. La hauteur de sortie finale sera un multiple de 16 (par défaut : 720). | INT | Non | 0 à 16384 (pas de 8) |
| `crop` | Détermine comment le latent mis à l'échelle est recadré pour correspondre aux dimensions cibles. | COMBO | Non | `"disabled"`<br>`"center"` |

**Remarque sur les dimensions :** si `width` et `height` sont tous deux définis sur 0, le nœud renvoie les `samples` d'entrée inchangés. Si une seule dimension est définie sur 0, l'autre dimension est calculée pour préserver le rapport hauteur/largeur d'origine. Les dimensions finales sont toujours ajustées pour être d'au moins 64 pixels et divisibles par 16.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation d'image latente mise à l'échelle et affinée par le modèle. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/fr.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
