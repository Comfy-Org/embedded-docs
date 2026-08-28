# Planificateur Ideogram 4

Le nœud Ideogram 4 Scheduler génère une séquence de valeurs sigma (niveaux de bruit) pour le processus d'échantillonnage de diffusion, basé sur le programme de référence Ideogram 4. Il crée un programme de bruit personnalisé qui s'adapte aux dimensions de l'image et permet un réglage fin via des paramètres statistiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `étapes` | Le nombre d'étapes d'échantillonnage pour générer le programme (par défaut : 20). La sortie contient `steps + 1` valeurs sigma. | INT | Oui | 1 à 200 |
| `largeur` | La largeur de l'image en pixels (par défaut : 1024). La résolution par rapport à une référence 512×512 décale le programme de bruit. | INT | Oui | 256 à 8192 (step: 16) |
| `hauteur` | La hauteur de l'image en pixels (par défaut : 1024). La résolution par rapport à une référence 512×512 décale le programme de bruit. | INT | Oui | 256 à 8192 (step: 16) |
| `mu` | Le paramètre de moyenne de la distribution logit-normale, contrôlant le niveau de bruit central. Combiné avec le terme de résolution pour former le décalage logSNR (par défaut : 0.0). | FLOAT | Oui | -10.0 à 10.0 (step: 0.05) |
| `écart_type` | Le paramètre d'écart type de la distribution logit-normale, contrôlant la dispersion des niveaux de bruit (par défaut : 1.75). | FLOAT | Oui | 0.1 à 5.0 (step: 0.05) |

Remarque : Le programme est dérivé d'une distribution logit-normale sur le temps de référence. Un terme de résolution égal à `0.5 * log((width × height) / (512 × 512))` est ajouté à `mu`, de sorte que les images plus grandes ou plus petites décalent le programme par rapport à une référence 512×512 pour la même valeur de `mu`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `SIGMAS` | Un tenseur de valeurs sigma représentant le programme de bruit, dont la longueur est égale à `steps + 1`. Les valeurs descendent d'un bruit élevé à un bruit faible, la valeur finale étant définie à 0.0 pour un débruitage complet. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/fr.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
