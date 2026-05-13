> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/fr.md)

Le nœud SamplerEulerCFGpp fournit une méthode d'échantillonnage Euler CFG++ pour générer des sorties. Ce nœud propose deux versions d'implémentation différentes de l'échantillonneur Euler CFG++, qui peuvent être sélectionnées selon les préférences de l'utilisateur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `version` | STRING | Oui | `"regular"`<br>`"alternative"` | Version d'implémentation de l'échantillonneur Euler CFG++ à utiliser (par défaut : "regular") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `sampler` | SAMPLER | Retourne une instance configurée de l'échantillonneur Euler CFG++ |

---
**Source fingerprint (SHA-256):** `f01732fc39a76fca697aaddefc8cec58d54ba9761eb8d93da806ddd162d42513`
