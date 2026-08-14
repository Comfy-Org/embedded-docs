# Google Gemini

Générer des réponses textuelles avec les modèles Gemini de Google. Fournissez une invite textuelle et, éventuellement, une ou plusieurs images, clips audio, vidéos ou fichiers comme contexte multimodal.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Saisie textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. | STRING | Oui |  |
| `modèle` | Le modèle Gemini utilisé pour générer la réponse. | COMBO | Oui | `"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `graine` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. La sortie déterministe n'est pas garantie. (par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `invite système` | Instructions fondamentales qui dictent le comportement du modèle. (par défaut : "") | STRING | Non |  |

**Remarque :** Lors de la fourniture d'images, d'audio ou de vidéos comme contexte multimodal, le nœud télécharge les médias sous forme d'URL pour les 10 premières entrées. Tout média supplémentaire est envoyé en ligne sous forme de données base64, avec une charge utile maximale en ligne de 18 Mo. Si la charge utile en ligne dépasse cette limite, une erreur est générée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle Gemini. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `ec9921f218a726082eb8987cf94b3575f61a3c6cf55fb33aeb81d42fad35d302`
