# ÉchantillonneurER_SDE

Le nœud SamplerER_SDE fournit des méthodes d'échantillonnage spécialisées pour les modèles de diffusion, proposant trois types de solveurs : ER-SDE, Reverse-time SDE et ODE. Il permet de contrôler le comportement stochastique et le nombre d'étapes de calcul du processus d'échantillonnage. Le nœud ajuste automatiquement les paramètres de bruit lorsque le solveur ODE ou une configuration déterministe (`eta`=0) est sélectionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `solver_type` | Le type de solveur à utiliser pour l'échantillonnage. Détermine le comportement de mise à l'échelle du bruit du processus de diffusion (défaut : "ER-SDE"). | COMBO | Oui | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | Le nombre maximal d'étapes pour le processus d'échantillonnage (défaut : 3). Contrôle la complexité de calcul et la qualité. Paramètre avancé. | INT | Oui | 1-3 |
| `eta` | Force stochastique des SDE.<br>Lorsque eta=0, elles se réduisent à une ODE déterministe.<br>Une valeur élevée de eta peut provoquer des sorties invalides. Si cela se produit, essayez de diminuer cette valeur. (défaut : 1.0). Paramètre avancé. | FLOAT | Oui | 0.0-10.0 |
| `s_noise` | Facteur d'échelle du bruit pour le processus d'échantillonnage (défaut : 1.0). Contrôle la quantité de bruit appliquée pendant l'échantillonnage. Paramètre avancé. | FLOAT | Oui | 0.0-100.0 |

**Contraintes des paramètres :**

- Lorsque `solver_type` est "ODE" ou que `eta` vaut 0, le nœud force `s_noise` à 0.0 et bascule le solveur sur "ODE".
- `eta` affecte à la fois les types de solveurs "ER-SDE" et "Reverse-time SDE". De grandes valeurs peuvent provoquer des sorties invalides.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `sampler` | Un objet sampler configuré qui peut être utilisé dans le pipeline d'échantillonnage avec les paramètres de solveur spécifiés. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
