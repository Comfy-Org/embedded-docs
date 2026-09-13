# Options d’échantillonnage SenseNova

Options d'échantillonnage SenseNova définit le décalage de flux SenseNova sur un modèle. Il clone le modèle d'entrée, attache une configuration d'échantillonnage de modèle SenseNova en utilisant la valeur de décalage de flux choisie, et renvoie le modèle patché à utiliser pendant l'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle auquel la configuration d'échantillonnage du décalage de flux SenseNova est appliquée. | MODEL | Oui | - |
| `shift` | La valeur de décalage de flux à définir pour l'échantillonnage du modèle SenseNova (par défaut : 3.0 ; pas de l'interface : 0.01). | FLOAT | Oui | Aucun minimum ou maximum défini |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Un clone du modèle d'entrée avec le décalage de flux SenseNova appliqué à sa configuration d'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/fr.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
