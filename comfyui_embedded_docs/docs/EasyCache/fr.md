# EasyCache

Le nœud EasyCache ajoute un système de mise en cache natif à un modèle de diffusion, ce qui accélère l'échantillonnage en réutilisant les résultats des étapes précédemment calculées au lieu de recalculer chaque étape. Il ne s’active qu’entre un point de début et de fin configurable du processus d’échantillonnage, et ignore des étapes lorsque le changement estimé de la sortie reste en dessous d’un seuil défini par l’utilisateur. Ce nœud est expérimental et destiné à un usage avancé de débogage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel ajouter EasyCache. | MODEL | Oui | - |
| `seuil_de_réutilisation` | Le seuil pour réutiliser les étapes mises en cache (par défaut : 0,2). | FLOAT | Oui | 0,0 - 3,0 |
| `pourcentage_de_départ` | L’étape d’échantillonnage relative où commence l’utilisation d’EasyCache (par défaut : 0,15). | FLOAT | Oui | 0,0 - 1,0 |
| `pourcentage_de_fin` | L’étape d’échantillonnage relative où se termine l’utilisation d’EasyCache (par défaut : 0,95). | FLOAT | Oui | 0,0 - 1,0 |
| `verbeux` | Indique si des informations détaillées doivent être journalisées (par défaut : False). | BOOLEAN | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la fonctionnalité EasyCache ajoutée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/fr.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
