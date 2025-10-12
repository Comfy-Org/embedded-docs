> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/fr.md)

Le nœud SamplerEulerAncestralCFGPP crée un échantillonneur spécialisé pour générer des images en utilisant la méthode Euler Ancestral avec un guidage sans classifieur. Cet échantillonneur combine des techniques d'échantillonnage ancestral avec un conditionnement par guidage pour produire des variations d'images diversifiées tout en maintenant la cohérence. Il permet un réglage fin du processus d'échantillonnage grâce à des paramètres qui contrôlent le bruit et les ajustements de la taille des pas.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Oui | 0.0 - 1.0 | Contrôle la taille du pas pendant l'échantillonnage, des valeurs plus élevées entraînant des mises à jour plus agressives (par défaut : 1.0) |
| `s_bruit` | FLOAT | Oui | 0.0 - 10.0 | Ajuste la quantité de bruit ajoutée pendant le processus d'échantillonnage (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne un objet échantillonneur configuré qui peut être utilisé dans le pipeline de génération d'images |