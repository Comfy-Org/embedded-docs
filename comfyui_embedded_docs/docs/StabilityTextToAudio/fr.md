> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/fr.md)

Génère des morceaux de musique et des effets sonores de haute qualité à partir de descriptions textuelles. Ce nœud utilise la technologie de génération audio de Stability AI pour créer un contenu audio basé sur vos invites textuelles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"stable-audio-2.5"` | Le modèle de génération audio à utiliser (par défaut : "stable-audio-2.5") |
| `consigne` | STRING | Oui | - | La description textuelle utilisée pour générer le contenu audio (par défaut : chaîne vide) |
| `durée` | INT | Non | 1-190 | Contrôle la durée en secondes de l'audio généré (par défaut : 190) |
| `graine` | INT | Non | 0-4294967294 | La graine aléatoire utilisée pour la génération (par défaut : 0) |
| `étapes` | INT | Non | 4-8 | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio` | AUDIO | Le fichier audio généré à partir de l'invite textuelle |

---
**Source fingerprint (SHA-256):** `5185241ca7a9b4bc38dfa8bafdae63ec3c151a3038a26ffe8e35492c0550fa88`
