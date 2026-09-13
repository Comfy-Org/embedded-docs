# LTXVScheduler

Le nœud LTXVScheduler génère des valeurs sigma pour un processus d'échantillonnage personnalisé. Il calcule le calendrier de bruit à partir du nombre de tokens dans le latent fourni, ou utilise une valeur par défaut de 4096 tokens lorsqu'aucun latent n'est connecté, et peut éventuellement étirer les valeurs sigma afin que la valeur finale corresponde à la valeur `terminal` spécifiée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `steps` | Nombre d'étapes d'échantillonnage (par défaut : 20) | INT | Oui | 1-10000 |
| `max_shift` | Valeur de décalage maximale utilisée dans le calcul des sigma (par défaut : 2.05) | FLOAT | Oui | 0.0-100.0 (pas : 0.01) |
| `base_shift` | Valeur de décalage de base utilisée dans le calcul des sigma (par défaut : 0.95) | FLOAT | Oui | 0.0-100.0 (pas : 0.01) |
| `stretch` | Étire les sigmas pour qu'ils soient dans l'intervalle [terminal, 1] (par défaut : True) | BOOLEAN | Oui | True/False |
| `terminal` | Valeur terminale des sigmas après étirement (par défaut : 0.1). Utilisée uniquement lorsque `stretch` est activé. | FLOAT | Oui | 0.0-0.99 (pas : 0.01) |
| `latent` | Entrée latent optionnelle utilisée pour calculer le nombre de tokens pour l'ajustement des sigma. Lorsqu'elle n'est pas fournie, un nombre de tokens par défaut de 4096 est utilisé. | LATENT | Non | - |

**Remarque :** Lorsque `stretch` est activé, les valeurs sigma non nulles sont remises à l'échelle afin que le dernier sigma non nul soit égal à la valeur `terminal`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Valeurs sigma générées pour le processus d'échantillonnage | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
