Voici la traduction en français de la documentation du nœud ComfyUI :

# Planificateur Ideogram 4

Le nœud Planificateur Ideogram 4 génère une séquence de valeurs sigma (niveaux de bruit) pour le processus d'échantillonnage par diffusion, basée sur le planning de référence Ideogram 4. Il crée un planning de bruit personnalisé qui s'adapte aux dimensions de l'image et permet un réglage fin via des paramètres statistiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `étapes` | Le nombre d'étapes d'échantillonnage pour générer le planning (par défaut : 20) | INT | Oui | 1 à 200 |
| `largeur` | La largeur de l'image en pixels (par défaut : 1024) | INT | Oui | 256 à 8192 (pas : 16) |
| `hauteur` | La hauteur de l'image en pixels (par défaut : 1024) | INT | Oui | 256 à 8192 (pas : 16) |
| `mu` | Le paramètre de moyenne pour la distribution logit-normale, contrôlant le niveau de bruit central (par défaut : 0.0) | FLOAT | Oui | -10.0 à 10.0 (pas : 0.05) |
| `écart_type` | Le paramètre d'écart type pour la distribution logit-normale, contrôlant l'étalement des niveaux de bruit (par défaut : 1.75) | FLOAT | Oui | 0.1 à 5.0 (pas : 0.05) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SIGMAS` | Un tenseur de valeurs sigma représentant le planning de bruit, dont la longueur est égale à `steps + 1`. Les valeurs descendent d'un bruit élevé à un bruit faible, la valeur finale étant fixée à 0.0 pour un débruitage complet. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/fr.md)

---
**Source fingerprint (SHA-256):** `408ea680158500690e28e300098a5c4fd13eb1a2c96c3d95db06244151116f22`
