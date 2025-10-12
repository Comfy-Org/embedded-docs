> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/fr.md)

Transforme des échantillons audio existants en nouvelles compositions de haute qualité à l'aide d'instructions textuelles. Ce nœud prend un fichier audio en entrée et le modifie en fonction de votre prompt textuel pour créer un nouveau contenu audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | "stable-audio-2.5"<br> | Le modèle d'IA à utiliser pour la transformation audio |
| `prompt` | STRING | Oui |  | Instructions textuelles décrivant comment transformer l'audio (par défaut : vide) |
| `audio` | AUDIO | Oui |  | L'audio doit avoir une durée comprise entre 6 et 190 secondes |
| `duration` | INT | Non | 1-190 | Contrôle la durée en secondes de l'audio généré (par défaut : 190) |
| `seed` | INT | Non | 0-4294967294 | La graine aléatoire utilisée pour la génération (par défaut : 0) |
| `steps` | INT | Non | 4-8 | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8) |
| `strength` | FLOAT | Non | 0.01-1.0 | Ce paramètre contrôle l'influence du paramètre audio sur l'audio généré (par défaut : 1.0) |

**Note :** L'audio d'entrée doit avoir une durée comprise entre 6 et 190 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | L'audio transformé généré sur la base de l'audio d'entrée et du prompt textuel |