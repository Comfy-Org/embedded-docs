# SamplerLCMUpscale

Le nœud SamplerLCMUpscale fournit une méthode d'échantillonnage spécialisée qui combine l'échantillonnage par modèle de cohérence latente (LCM) avec des capacités d'agrandissement d'image. Il agrandit l'image progressivement pendant le processus d'échantillonnage en utilisant diverses méthodes d'interpolation, permettant de générer des sorties haute résolution en une seule passe d'échantillonnage. La sortie est un objet échantillonneur configuré qui peut être connecté à un nœud d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ratio_échelle` | Le facteur d'échelle total à appliquer lors de l'agrandissement. Une valeur de 1.0 conserve la résolution d'origine (défaut : 1.0) | FLOAT | Oui | 0.1 - 20.0 |
| `étapes_échelle` | Le nombre d'étapes à utiliser pour le processus d'agrandissement. Utilisez -1 pour un calcul automatique basé sur le calendrier d'échantillonnage (défaut : -1) | INT | Oui | -1 - 1000 |
| `méthode_agrandissement` | La méthode d'interpolation utilisée pour agrandir l'image à chaque étape d'agrandissement (défaut : "bislerp") | COMBO | Oui | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` et `scale_steps` sont des paramètres avancés. L'image est agrandie progressivement de sa taille d'origine à la `scale_ratio` cible au fil des étapes d'agrandissement. Lorsque `scale_steps` est défini sur -1, le nombre d'étapes d'agrandissement est calculé automatiquement comme environ la moitié du nombre d'étapes d'échantillonnage, avec un minimum de 2 ; lorsqu'une valeur positive est fournie, le nœud l'ajuste en interne et la limite en fonction du nombre total d'étapes d'échantillonnage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur configuré qui effectue un échantillonnage LCM avec agrandissement progressif, prêt à être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/fr.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
