> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/fr.md)

Le nœud SamplerLMS crée un échantillonneur LMS (Least Mean Squares) pour une utilisation dans les modèles de diffusion. Il génère un objet échantillonneur qui peut être utilisé dans le processus d'échantillonnage, vous permettant de contrôler l'ordre de l'algorithme LMS pour la stabilité numérique et la précision.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `order` | INT | Oui | 1 à 100 | Le paramètre d'ordre pour l'algorithme de l'échantillonneur LMS, qui contrôle la précision et la stabilité de la méthode numérique (par défaut : 4) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objet échantillonneur LMS configuré qui peut être utilisé dans le pipeline d'échantillonnage |