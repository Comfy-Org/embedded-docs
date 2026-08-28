# LTX 2.5 Texte vers Vidéo

LTX 2.5 Text To Video est un nœud API qui génère des vidéos de qualité professionnelle à partir d'une description textuelle à l'aide du modèle LTX 2.5. Vous fournissez une invite et choisissez les paramètres de génération tels que le niveau du modèle, la durée, la résolution, la fréquence d'images et l'inclusion de l'audio ; le nœud soumet la tâche à l'API LTX et renvoie la vidéo obtenue.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le niveau du modèle LTX 2.5 à utiliser pour la génération de vidéos. | STRING | Oui | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `durée` | La durée de la vidéo générée. | INT | Oui | Entier |
| `résolution` | La résolution de sortie de la vidéo. Les options disponibles dépendent du `model` sélectionné. | STRING | Oui | Avec "LTX-2.5 (Fast)" :<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>Avec "LTX-2.5 (Pro)" :<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `fps` | Fréquence d'images de la vidéo générée (par défaut : 25). | INT | Non | Entier |
| `générer_audio` | Indique si l'audio doit être généré avec la vidéo (par défaut : True). | BOOLEAN | Non | True<br>False |
| `prompt` | La description textuelle de la vidéo à générer. Une invite non vide de 10 000 caractères maximum est requise (par défaut : ""). | STRING | Oui | 1 à 10000 caractères |
| `seed` | Valeur de seed utilisée pour une génération reproductible (par défaut : 42). | INT | Non | Entier |

Remarque : Les options `model.resolution` disponibles dépendent du `model` sélectionné. « LTX-2.5 (Fast) » prend en charge des résolutions jusqu'à 2160x3840, tandis que « LTX-2.5 (Pro) » prend en charge des résolutions jusqu'à 1920x1080.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée renvoyée par l'API LTX, prête à être utilisée dans le workflow. Si la génération audio a été activée, la vidéo inclut un audio synchronisé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
