> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/fr.md)

Le nœud SamplerDPMPP_2S_Ancestral crée un échantillonneur qui utilise la méthode d'échantillonnage DPM++ 2S Ancestral pour générer des images. Cet échantillonneur combine des éléments déterministes et stochastiques pour produire des résultats variés tout en maintenant une certaine cohérence. Il vous permet de contrôler l'aléatoire et les niveaux de bruit pendant le processus d'échantillonnage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la quantité de bruit stochastique ajouté pendant l'échantillonnage (par défaut : 1.0) |
| `s_noise` | FLOAT | Oui | 0.0 - 100.0 | Contrôle l'échelle du bruit appliqué pendant le processus d'échantillonnage (par défaut : 1.0) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne un objet échantillonneur configuré qui peut être utilisé dans le pipeline d'échantillonnage |