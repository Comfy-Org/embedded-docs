# LTXVScheduler

Le nœud LTXVScheduler génère des valeurs sigma pour les processus d'échantillonnage personnalisés. Il calcule les paramètres du programme de bruit en fonction du nombre de jetons dans le latent d’entrée et applique une transformation sigmoïde pour créer le programme d’échantillonnage. Le nœud peut éventuellement étirer les sigma résultants pour correspondre à une valeur terminale spécifiée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `étapes` | Nombre d'étapes d'échantillonnage (par défaut : 20) | INT | Oui | 1-10000 |
| `décalage_max` | Valeur de décalage maximale pour le calcul de sigma (par défaut : 2.05) | FLOAT | Oui | 0.0-100.0 |
| `décalage_base` | Valeur de décalage de base pour le calcul de sigma (par défaut : 0.95) | FLOAT | Oui | 0.0-100.0 |
| `étirement` | Étire les sigma pour qu'ils soient dans la plage [terminal, 1] (par défaut : True) | BOOLEAN | Oui | True/False |
| `terminal` | La valeur terminale des sigma après étirement (par défaut : 0.1) | FLOAT | Oui | 0.0-0.99 |
| `latent` | Entrée latente facultative utilisée pour calculer le nombre de jetons pour l'ajustement des sigma | LATENT | Non | - |

**Remarque :** Le paramètre `latent` est facultatif. Lorsqu'il n'est pas fourni, le nœud utilise un nombre de jetons par défaut de 4096 pour les calculs.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Valeurs sigma générées pour le processus d'échantillonnage | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
