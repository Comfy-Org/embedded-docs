# SamplerLCMUpscale

Le nœud SamplerLCMUpscale fournit une méthode d'échantillonnage spécialisée qui combine l'échantillonnage du modèle de cohérence latente (LCM) avec des capacités d'agrandissement d'image. Il vous permet d'agrandir des images pendant le processus d'échantillonnage en utilisant diverses méthodes d'interpolation, ce qui est utile pour générer des sorties en résolution plus élevée tout en maintenant la qualité de l'image. L'agrandissement est appliqué progressivement sur les étapes d'échantillonnage jusqu'à ce que le `scale_ratio` cible soit atteint.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `scale_ratio` | Le facteur d'échelle à appliquer lors de l'agrandissement (par défaut : 1.0) | FLOAT | Non | 0.1 - 20.0 |
| `scale_steps` | Le nombre d'étapes à utiliser pour le processus d'agrandissement. Utilisez -1 pour le calcul automatique (par défaut : -1) | INT | Non | -1 - 1000 |
| `upscale_method` | La méthode d'interpolation utilisée pour agrandir l'image (par défaut : bislerp) | COMBO | Oui | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

Remarque : Lorsque `scale_steps` est défini sur une valeur positive, le nombre effectif d'étapes d'agrandissement est limité par le nombre total d'étapes d'échantillonnage de l'échantillonneur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré qui peut être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/fr.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
