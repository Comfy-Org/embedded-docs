> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/fr.md)

Le nœud SamplerLCMUpscale fournit une méthode d'échantillonnage spécialisée qui combine l'échantillonnage par modèle de cohérence latente (LCM) avec des capacités de suréchantillonnage d'image. Il vous permet de suréchantillonner les images pendant le processus d'échantillonnage en utilisant diverses méthodes d'interpolation, ce qui le rend utile pour générer des sorties de plus haute résolution tout en maintenant la qualité de l'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `ratio_échelle` | FLOAT | Non | 0,1 - 20,0 | Le facteur d'échelle à appliquer pendant le suréchantillonnage (par défaut : 1,0) |
| `étapes_échelle` | INT | Non | -1 - 1000 | Le nombre d'étapes à utiliser pour le processus de suréchantillonnage. Utilisez -1 pour un calcul automatique (par défaut : -1) |
| `méthode_agrandissement` | COMBO | Oui | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | La méthode d'interpolation utilisée pour le suréchantillonnage de l'image |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne un objet échantillonneur configuré qui peut être utilisé dans le pipeline d'échantillonnage |