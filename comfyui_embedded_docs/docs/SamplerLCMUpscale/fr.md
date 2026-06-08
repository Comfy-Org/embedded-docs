Le nœud SamplerLCMUpscale fournit une méthode d'échantillonnage spécialisée qui combine l'échantillonnage par modèle de cohérence latente (LCM) avec des capacités de suréchantillonnage d'image. Il permet de suréchantillonner les images pendant le processus d'échantillonnage en utilisant diverses méthodes d'interpolation, ce qui le rend utile pour générer des sorties à plus haute résolution tout en préservant la qualité de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ratio_échelle` | Le facteur d'échelle à appliquer lors du suréchantillonnage (par défaut : 1.0) | FLOAT | Non | 0.1 - 20.0 |
| `étapes_échelle` | Le nombre d'étapes à utiliser pour le processus de suréchantillonnage. Utilisez -1 pour un calcul automatique (par défaut : -1) | INT | Non | -1 - 1000 |
| `méthode_agrandissement` | La méthode d'interpolation utilisée pour le suréchantillonnage de l'image | COMBO | Oui | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré pouvant être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/fr.md)

---
**Source fingerprint (SHA-256):** `fe0d4c8676454a9e8ecf4bb4e149c9b5e22083322447749116d624984d75e73c`
