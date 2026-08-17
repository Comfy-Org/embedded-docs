# Planificateur Ideogram 4

Le nœud Ideogram 4 Scheduler génère une séquence de valeurs sigma (niveaux de bruit) pour le processus d'échantillonnage de diffusion, sur la base du calendrier de référence Ideogram 4. Il crée un calendrier de bruit personnalisé qui s'adapte aux dimensions de l'image et permet un réglage fin via des paramètres statistiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `steps` | Le nombre d'étapes d'échantillonnage pour lesquelles générer le calendrier (par défaut : 20) | INT | Oui | 1 à 200 |
| `width` | La largeur de l'image en pixels (par défaut : 1024) | INT | Oui | 256 à 8192 (step: 16) |
| `height` | La hauteur de l'image en pixels (par défaut : 1024) | INT | Oui | 256 à 8192 (step: 16) |
| `mu` | Le paramètre de moyenne pour la distribution logit-normale, contrôlant le niveau de bruit central (par défaut : 0.0) | FLOAT | Oui | -10.0 à 10.0 (step: 0.05) |
| `std` | Le paramètre d'écart type pour la distribution logit-normale, contrôlant la dispersion des niveaux de bruit (par défaut : 1.75) | FLOAT | Oui | 0.1 à 5.0 (step: 0.05) |

Remarque : Le décalage central effectif du calendrier est déterminé par `mu` combiné avec un terme de résolution basé sur la surface de l'image par rapport à une référence 512×512. Des surfaces d'image plus grandes décalent donc le calendrier de bruit par rapport aux plus petites.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SIGMAS` | Un tenseur de valeurs sigma représentant le calendrier de bruit, avec une longueur égale à `steps + 1`. Les valeurs descendent du bruit élevé au bruit faible, avec la valeur finale fixée à 0.0 pour un débruitage complet. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/fr.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
