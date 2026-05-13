> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/fr.md)

Le nœud Hunyuan Video 15 Latent Upscale With Model augmente la résolution d'une représentation d'image latente. Il commence par suréchantillonner les échantillons latents à une taille spécifiée à l'aide d'une méthode d'interpolation choisie, puis affine le résultat suréchantillonné à l'aide d'un modèle de suréchantillonnage spécialisé Hunyuan Video 1.5 pour améliorer la qualité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | LATENT_UPSCALE_MODEL | Oui | N/A | Le modèle de suréchantillonnage latent Hunyuan Video 1.5 utilisé pour affiner les échantillons suréchantillonnés. |
| `échantillons` | LATENT | Oui | N/A | La représentation d'image latente à suréchantillonner. |
| `méthode_d_agrandissement` | COMBO | Non | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | L'algorithme d'interpolation utilisé pour l'étape de suréchantillonnage initiale (par défaut : `"bilinear"`). |
| `largeur` | INT | Non | 0 à 16384 | La largeur cible du latent suréchantillonné, en pixels. Une valeur de 0 calculera automatiquement la largeur en fonction de la hauteur cible et du rapport d'aspect d'origine. La largeur de sortie finale sera un multiple de 16 (par défaut : 1280). |
| `hauteur` | INT | Non | 0 à 16384 | La hauteur cible du latent suréchantillonné, en pixels. Une valeur de 0 calculera automatiquement la hauteur en fonction de la largeur cible et du rapport d'aspect d'origine. La hauteur de sortie finale sera un multiple de 16 (par défaut : 720). |
| `rogner` | COMBO | Non | `"disabled"`<br>`"center"` | Détermine comment le latent suréchantillonné est recadré pour correspondre aux dimensions cibles. |

**Remarque sur les dimensions :** Si `width` et `height` sont tous deux définis sur 0, le nœud renvoie les `samples` d'entrée inchangés. Si une seule dimension est définie sur 0, l'autre dimension est calculée pour préserver le rapport d'aspect d'origine. Les dimensions finales sont toujours ajustées pour être d'au moins 64 pixels et divisibles par 16.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `LATENT` | LATENT | La représentation d'image latente suréchantillonnée et affinée par le modèle. |

---
**Source fingerprint (SHA-256):** `1de9e157c1a0433f1b3d5ff4d428a1aa392fd65da5e314e6e818ce66495d5ef4`
