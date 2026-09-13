# SamplerLCMUpscale

Ce nœud fournit une méthode d'échantillonnage spécialisée qui combine l'échantillonnage LCM (Latent Consistency Model) avec un agrandissement progressif de l'image. Pendant l'échantillonnage, l'image est agrandie étape par étape vers un ratio d'échelle cible à l'aide d'une méthode d'interpolation choisie, ce qui permet d'obtenir des résultats à plus haute résolution en une seule passe d'échantillonnage. Le nœud produit un objet sampler configuré qui peut être connecté à un nœud d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `scale_ratio` | Le facteur d'échelle total à appliquer pendant l'agrandissement. Une valeur de 1.0 conserve la résolution d'origine (par défaut : 1.0) | FLOAT | Oui | 0.1 - 20.0 |
| `scale_steps` | Le nombre d'étapes à utiliser pour le processus d'agrandissement. Utilisez -1 pour un calcul automatique basé sur le programme d'échantillonnage (par défaut : -1) | INT | Oui | -1 - 1000 |
| `upscale_method` | La méthode d'interpolation utilisée pour agrandir l'image à chaque étape d'agrandissement (par défaut : "bislerp") | COMBO | Oui | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` et `scale_steps` sont des paramètres avancés. L'image est agrandie progressivement depuis sa taille d'origine jusqu'au `scale_ratio` cible au fil des étapes d'agrandissement. Lorsque `scale_steps` vaut -1, le nombre d'étapes d'agrandissement est calculé automatiquement comme environ la moitié du nombre d'étapes d'échantillonnage, avec un minimum de 2 ; lorsqu'une valeur positive est fournie, le nœud l'ajuste en interne et la limite en fonction du nombre total d'étapes d'échantillonnage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet sampler configuré qui effectue un échantillonnage LCM avec agrandissement progressif, prêt à être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/fr.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
