# LTX 2.5 Audio vers Vidéo

Ce nœud génère une vidéo qui suit une piste audio à l’aide du modèle LTX 2.5. L’audio détermine la durée de la vidéo (entre 2 et 20 secondes), et vous pouvez éventuellement fournir une image à utiliser comme première image. La vidéo est générée via le service API LTX 2.5.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Piste audio qui pilote la vidéo. Sa durée (2-20 secondes) détermine la durée de la vidéo. | AUDIO | Oui | 2-20 seconds |
| `modèle` | La version du modèle LTX 2.5 à utiliser. La résolution vidéo (1920x1080 ou 1080x1920) est sélectionnée avec le modèle ; les deux modèles offrent les mêmes options de résolution. | COMBO | Oui | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `prompt` | Une description textuelle qui guide le contenu de la vidéo générée (par défaut : ""). Doit contenir au moins 1 caractère et au plus 10000 caractères. | STRING | Oui | 1-10000 characters |
| `seed` | Un nombre qui contrôle le caractère aléatoire de la génération. La même valeur de `seed` produit le même résultat (par défaut : 42). | INT | Oui | Any integer |
| `image` | Première image facultative à utiliser pour la vidéo. Une seule image est prise en charge. | IMAGE | Non | Single image |

Notes sur les contraintes :
- La durée de l’audio doit être comprise entre 2 et 20 secondes ; le nœud génère une erreur si elle est hors de cette plage.
- Le prompt est obligatoire et ne peut pas être vide ; il doit contenir entre 1 et 10000 caractères.
- Une seule image d’entrée est acceptée lorsque `image` est fourni.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, pilotée par la piste audio fournie. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
