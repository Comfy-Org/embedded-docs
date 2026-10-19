# MOSS-Image Color/Depth Control

Ajoute les cartes de régions de couleur et de profondeur d’un adaptateur de contrôle couleur/profondeur MOSS-Image au conditionnement. Connectez les conditionnements positif et négatif, un VAE, et une ou les deux cartes : les cartes sont encodées en latents, fusionnées en un signal de contrôle couleur/profondeur, puis attachées au conditionnement pour la partie de l’échantillonnage que vous choisissez. Utilisez-le avec un adaptateur de contrôle MOSS-Image chargé via un chargeur LoRA.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Conditionnement positif auquel attacher le signal de contrôle. | CONDITIONING | Oui | N/A |
| `negative` | Conditionnement négatif auquel attacher le signal de contrôle. | CONDITIONING | Oui | N/A |
| `vae` | VAE utilisé pour encoder les cartes en latents. | VAE | Oui | N/A |
| `color_map` | Une couleur unie par région, à la taille de sortie. Les couleurs servent uniquement d’identifiants de région. | IMAGE | Non | N/A |
| `depth_map` | Carte de profondeur à la taille de sortie, le proche est blanc. | IMAGE | Non | N/A |
| `strength` | Met à l’échelle la contribution des cartes aux tokens d’image. 0.0 équivaut à l’absence de cartes, 1.0 correspond à la force d’entraînement (par défaut : 1.0). | FLOAT | Oui | 0.0 à 10.0 (pas 0.01) |
| `start_percent` | Pourcentage d’échantillonnage auquel le contrôle commence (par défaut : 0.0). | FLOAT | Oui | 0.0 à 1.0 (pas 0.001) |
| `end_percent` | Pourcentage d’échantillonnage auquel le contrôle se termine. Un arrêt précoce conserve la disposition et la profondeur tandis que le reste des étapes assouplit les formes (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas 0.001) |

**Remarque :** Connectez au moins l’une des entrées `color_map` et `depth_map` ; sans aucune des deux, le nœud renvoie les conditionnements inchangés. Une carte manquante est remplacée par des zéros, de sorte que les configurations avec couleur uniquement et profondeur uniquement fonctionnent toutes les deux. Lorsque les deux cartes ont des tailles différentes, la plus petite est agrandie à la taille de l’autre. Ce nœud est marqué comme expérimental dans ComfyUI.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement positif avec le signal de contrôle attaché. | CONDITIONING |
| `negative` | Le conditionnement négatif avec le signal de contrôle attaché. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageControl/fr.md)

---
**Source fingerprint (SHA-256):** `c4a40c76f26237408e47cb9f683c13bccc3507bd775bec1b89919947a308c115`
