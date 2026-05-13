> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/fr.md)

Voici la traduction en français de la documentation, en respectant vos règles :

Le nœud SamplerER_SDE fournit des méthodes d'échantillonnage spécialisées pour les modèles de diffusion, proposant différents types de solveurs incluant les approches ER-SDE, SDE à temps inverse et ODE. Il permet de contrôler le comportement stochastique et les étapes de calcul du processus d'échantillonnage. Le nœud ajuste automatiquement les paramètres en fonction du type de solveur sélectionné pour garantir un fonctionnement correct.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `type_solveur` | COMBO | Oui | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" | Le type de solveur à utiliser pour l'échantillonnage. Détermine l'approche mathématique du processus de diffusion. |
| `étape_max` | INT | Non | 1-3 | Le nombre maximal d'étapes pour le processus d'échantillonnage (par défaut : 3). Contrôle la complexité de calcul et la qualité. |
| `eta` | FLOAT | Non | 0,0-100,0 | Force stochastique du SDE à temps inverse (par défaut : 1,0). Lorsque eta=0, il se réduit à un ODE déterministe. Ce paramètre ne s'applique pas au type de solveur ER-SDE. |
| `s_bruit` | FLOAT | Non | 0,0-100,0 | Facteur d'échelle du bruit pour le processus d'échantillonnage (par défaut : 1,0). Contrôle la quantité de bruit appliquée pendant l'échantillonnage. |

**Contraintes des paramètres :**

- Lorsque `solver_type` est défini sur "ODE" ou lors de l'utilisation de "Reverse-time SDE" avec `eta`=0, `eta` et `s_noise` sont automatiquement définis sur 0, indépendamment des valeurs saisies par l'utilisateur.
- Le paramètre `eta` n'affecte que le type de solveur "Reverse-time SDE" et n'a aucun effet sur le type de solveur "ER-SDE".

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `sampler` | SAMPLER | Un objet échantillonneur configuré qui peut être utilisé dans le pipeline d'échantillonnage avec les paramètres de solveur spécifiés. |

---
**Source fingerprint (SHA-256):** `bc24ec3c5dc645aebf55ef3392c5f4a40dcf0461b4b77731e8fe7ff397dcfadf`
