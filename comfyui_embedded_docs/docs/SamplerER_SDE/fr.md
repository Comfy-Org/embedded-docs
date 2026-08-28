# ÉchantillonneurER_SDE

Le nœud SamplerER_SDE fournit des méthodes d'échantillonnage spécialisées pour les modèles de diffusion, proposant différents types de solveurs : ER-SDE, Reverse-time SDE et ODE. Il vous permet de contrôler le comportement stochastique et le nombre d'étapes de calcul du processus d'échantillonnage. Le nœud ajuste automatiquement les paramètres en fonction du type de solveur choisi pour garantir le bon fonctionnement de l'échantillonneur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `type_solveur` | Le type de solveur à utiliser pour l'échantillonnage. Détermine l'approche mathématique du processus de diffusion (par défaut : "ER-SDE"). | COMBO | Oui | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `étape_max` | Le nombre maximal d'étapes pour le processus d'échantillonnage (par défaut : 3). Contrôle la complexité de calcul et la qualité. | INT | Oui | 1-3 |
| `eta` | Force stochastique des SDE.<br>Lorsque eta=0, ils se réduisent à une ODE déterministe.<br>Une valeur élevée d'eta peut produire des résultats invalides. Si cela se produit, essayez de diminuer cette valeur. (par défaut : 1.0) | FLOAT | Oui | 0.0-10.0 (pas : 0.01) |
| `s_bruit` | Facteur d'échelle du bruit pour le processus d'échantillonnage (par défaut : 1.0). Contrôle la quantité de bruit appliquée pendant l'échantillonnage. | FLOAT | Oui | 0.0-100.0 (pas : 0.01) |

**Contraintes des paramètres :**

- Lorsque `solver_type` est défini sur "ODE" ou lorsque `eta` est 0, le nœud bascule en mode ODE et définit `s_noise` sur 0.0, quelle que soit la valeur saisie pour `s_noise`.
- Le paramètre `eta` contrôle la force stochastique des types de solveurs "ER-SDE" et "Reverse-time SDE". Il n'a aucun effet lorsque le solveur fonctionne en mode ODE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur configuré qui peut être utilisé dans le pipeline d'échantillonnage avec les paramètres de solveur spécifiés. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
