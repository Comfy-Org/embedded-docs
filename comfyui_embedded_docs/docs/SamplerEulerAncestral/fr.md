> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/fr.md)

Le nœud SamplerEulerAncestral crée un échantillonneur Euler Ancestral pour générer des images. Cet échantillonneur utilise une approche mathématique spécifique qui combine l'intégration d'Euler avec des techniques d'échantillonnage ancestral pour produire des variations d'images. Le nœud vous permet de configurer le comportement de l'échantillonnage en ajustant les paramètres qui contrôlent l'aléatoire et la taille des pas pendant le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la taille des pas et la stochasticité du processus d'échantillonnage (par défaut : 1.0) |
| `s_noise` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne un échantillonneur Euler Ancestral configuré qui peut être utilisé dans le pipeline d'échantillonnage |