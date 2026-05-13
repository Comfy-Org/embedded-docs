> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/fr.md)

Le nœud LTXVScheduler génère des valeurs sigma pour des processus d'échantillonnage personnalisés. Il calcule les paramètres du plan de bruit en fonction du nombre de jetons dans le latent d'entrée et applique une transformation sigmoïde pour créer le plan d'échantillonnage. Le nœud peut éventuellement étirer les sigmas résultants pour correspondre à une valeur terminale spécifiée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `étapes` | INT | Oui | 1-10000 | Nombre d'étapes d'échantillonnage (par défaut : 20) |
| `décalage_max` | FLOAT | Oui | 0.0-100.0 | Valeur de décalage maximale pour le calcul sigma (par défaut : 2.05) |
| `décalage_base` | FLOAT | Oui | 0.0-100.0 | Valeur de décalage de base pour le calcul sigma (par défaut : 0.95) |
| `étirement` | BOOLEAN | Oui | Vrai/Faux | Étirer les sigmas pour qu'ils soient dans la plage [terminal, 1] (par défaut : Vrai) |
| `terminal` | FLOAT | Oui | 0.0-0.99 | Valeur terminale des sigmas après étirement (par défaut : 0.1) |
| `latent` | LATENT | Non | - | Entrée latente facultative utilisée pour calculer le nombre de jetons pour l'ajustement sigma |

**Remarque :** Le paramètre `latent` est facultatif. Lorsqu'il n'est pas fourni, le nœud utilise un nombre de jetons par défaut de 4096 pour les calculs.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `sigmas` | SIGMAS | Valeurs sigma générées pour le processus d'échantillonnage |

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
