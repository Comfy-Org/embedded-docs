# Hunyuan Video 15 Latent Upscale With Model

Le nœud Hunyuan Video 15 Latent Upscale With Model augmente la résolution d'une représentation d'image latente. Il agrandit d'abord les échantillons latents à une taille spécifiée à l'aide d'une méthode d'interpolation choisie, puis affine le résultat agrandi à l'aide d'un modèle d'agrandissement spécialisé Hunyuan Video 1.5 pour améliorer la qualité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'agrandissement latent Hunyuan Video 1.5 utilisé pour affiner les échantillons agrandis. | LATENT_UPSCALE_MODEL | Oui | N/A |
| `échantillons` | La représentation d'image latente à agrandir. | LATENT | Oui | N/A |
| `méthode_d_agrandissement` | L'algorithme d'interpolation utilisé pour l'étape d'agrandissement initiale (par défaut : `"bilinear"`). | COMBO | Non | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `largeur` | La largeur cible pour le latent agrandi, en pixels. Une valeur de 0 calcule automatiquement la largeur en fonction de la hauteur cible et du ratio d'aspect d'origine. La largeur finale de sortie sera un multiple de 16 (par défaut : 1280). | INT | Non | 0 à 16384 (pas : 8) |
| `hauteur` | La hauteur cible pour le latent agrandi, en pixels. Une valeur de 0 calcule automatiquement la hauteur en fonction de la largeur cible et du ratio d'aspect d'origine. La hauteur finale de sortie sera un multiple de 16 (par défaut : 720). | INT | Non | 0 à 16384 (pas : 8) |
| `rogner` | Détermine comment le latent agrandi est recadré pour correspondre aux dimensions cibles. | COMBO | Non | `"disabled"`<br>`"center"` |

**Remarque sur les dimensions :** Si `width` et `height` sont tous deux définis à 0, le nœud renvoie les `samples` d'entrée inchangés. Si une seule dimension est définie à 0, l'autre dimension est calculée pour préserver le ratio d'aspect d'origine. Les dimensions finales sont toujours ajustées pour être d'au moins 64 pixels et divisibles par 16.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation d'image latente agrandie et affinée par le modèle. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/fr.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
