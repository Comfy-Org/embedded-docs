# Hunyuan Video 15 Latent Upscale With Model

Le nœud Hunyuan Video 15 Latent Upscale With Model augmente la résolution d'une représentation d'image latente. Il met d'abord à l'échelle les échantillons latents à une taille spécifiée à l'aide d'une méthode d'interpolation choisie, puis affine le résultat mis à l'échelle à l'aide d'un modèle d'upscale spécialisé Hunyuan Video 1.5 pour améliorer la qualité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'upscale latent Hunyuan Video 1.5 utilisé pour affiner les échantillons mis à l'échelle. | LATENT_UPSCALE_MODEL | Oui | N/A |
| `échantillons` | La représentation d'image latente à mettre à l'échelle. | LATENT | Oui | N/A |
| `méthode_d_agrandissement` | L'algorithme d'interpolation utilisé pour l'étape initiale de mise à l'échelle (par défaut : `"bilinear"`). | COMBO | Oui | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `largeur` | La largeur cible pour le latent mis à l'échelle, en pixels. Une valeur de 0 calcule automatiquement la largeur en fonction de la hauteur cible et du rapport d'aspect d'origine. La largeur de sortie finale sera un multiple de 16 (par défaut : 1280). | INT | Oui | 0 à 16384 (pas : 8) |
| `hauteur` | La hauteur cible pour le latent mis à l'échelle, en pixels. Une valeur de 0 calcule automatiquement la hauteur en fonction de la largeur cible et du rapport d'aspect d'origine. La hauteur de sortie finale sera un multiple de 16 (par défaut : 720). | INT | Oui | 0 à 16384 (pas : 8) |
| `rogner` | Détermine comment le latent mis à l'échelle est recadré pour s'adapter aux dimensions cibles. | COMBO | Oui | `"disabled"`<br>`"center"` |

**Remarque sur les dimensions :** Si `width` et `height` sont tous deux définis sur 0, le nœud renvoie l'entrée `samples` inchangée. Si une seule dimension est définie sur 0, l'autre dimension est calculée pour préserver le rapport d'aspect d'origine. Les deux valeurs sont limitées à un minimum de 64, et la cible de mise à l'échelle transmise à l'étape d'interpolation est `width // 16` par `height // 16`, de sorte que les dimensions demandées sont effectivement arrondies à l'inférieur à des multiples de 16.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation d'image latente mise à l'échelle et affinée par le modèle, renvoyée sous forme de tenseur float sur le CPU. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/fr.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
