# MiniMax H3 Sigma Shift

Définit les valeurs de décalage de flux vidéo et audio pour un modèle MiniMax H3. Le décalage vidéo contrôle le programme sigma de l'échantillonneur, et les deux valeurs de décalage sont transmises au transformateur interne du modèle, qui les utilise pour dériver le programme audio à partir de la grille de base partagée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle auquel appliquer le correctif de décalage sigma. Le nœud clone le modèle, donc l'original reste inchangé. | MODEL | Oui | - |
| `décalage vidéo` | La valeur de décalage du flux vidéo. Elle pilote le programme sigma de l'échantillonneur. Par défaut : 12.0. | FLOAT | Oui | 0.01 à 100.0 |
| `décalage audio` | La valeur de décalage du flux audio. Elle est utilisée par le modèle pour dériver le programme audio. Par défaut : 3.0. | FLOAT | Oui | 0.01 à 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle cloné avec les paramètres de décalage sigma vidéo et audio appliqués. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/fr.md)

---
**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`
