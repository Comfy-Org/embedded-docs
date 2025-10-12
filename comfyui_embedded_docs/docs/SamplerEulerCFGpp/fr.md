> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/fr.md)

Le nœud SamplerEulerCFGpp fournit une méthode d'échantillonnage Euler CFG++ pour générer des sorties. Ce nœud propose deux versions d'implémentation différentes de l'échantillonneur Euler CFG++ qui peuvent être sélectionnées selon les préférences de l'utilisateur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `version` | STRING | Oui | `"regular"`<br>`"alternative"` | La version d'implémentation de l'échantillonneur Euler CFG++ à utiliser |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne une instance d'échantillonneur Euler CFG++ configurée |
