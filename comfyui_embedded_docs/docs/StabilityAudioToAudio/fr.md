> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/fr.md)

Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/fr.md)

Transforme des échantillons audio existants en nouvelles compositions de haute qualité à l'aide d'instructions textuelles. Ce nœud prend un fichier audio en entrée et le modifie en fonction de votre invite textuelle pour créer un nouveau contenu audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | "stable-audio-2.5" | Le modèle d'IA à utiliser pour la transformation audio |
| `prompt` | STRING | Oui | | Instructions textuelles décrivant comment transformer l'audio (par défaut : vide) |
| `audio` | AUDIO | Oui | | L'audio doit durer entre 6 et 190 secondes |
| `duration` | INT | Non | 1-190 | Contrôle la durée en secondes de l'audio généré (par défaut : 190) |
| `seed` | INT | Non | 0-4294967294 | La graine aléatoire utilisée pour la génération (par défaut : 0) |
| `steps` | INT | Non | 4-8 | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8) |
| `strength` | FLOAT | Non | 0.01-1.0 | Ce paramètre contrôle l'influence du paramètre audio sur l'audio généré (par défaut : 1.0) |

**Remarque :** L'audio d'entrée doit durer entre 6 et 190 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio` | AUDIO | L'audio transformé généré à partir de l'audio d'entrée et de l'invite textuelle |

---
**Source fingerprint (SHA-256):** `d63ee2585be1ec1a21da72656ecea37f051a56595b15637013e515eb298fc4dc`
