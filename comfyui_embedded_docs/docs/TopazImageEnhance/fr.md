# Topaz Amélioration d'image

Le nœud Topaz Image Enhance fournit une mise à l'échelle et une amélioration d'image aux normes de l'industrie. Il traite une seule image d'entrée à l'aide d'un modèle d'IA basé sur le cloud pour améliorer la qualité, les détails et la résolution. Le nœud offre un contrôle précis du processus d'amélioration, y compris des options pour l'orientation créative, la mise au point du sujet et la préservation des visages.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle d'IA à utiliser pour l'amélioration d'image. | COMBO | Oui | `"Reimagine"` |
| `image` | L'image d'entrée à améliorer. Une seule image est prise en charge. | IMAGE | Oui | - |
| `prompt` | Invite de texte facultative pour l'orientation créative de la mise à l'échelle (par défaut : vide). | STRING | Non | - |
| `subject_detection` | Contrôle la partie de l'image sur laquelle l'amélioration se concentre (par défaut : « All »). | COMBO | Non | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Améliorer les visages (s'ils sont présents) pendant le traitement (par défaut : True). | BOOLEAN | Non | - |
| `face_enhancement_creativity` | Définir le niveau de créativité pour l'amélioration des visages (par défaut : 0.0). | FLOAT | Non | 0.0 - 1.0 |
| `face_enhancement_strength` | Contrôle le niveau de netteté des visages améliorés par rapport à l'arrière-plan (par défaut : 1.0). | FLOAT | Non | 0.0 - 1.0 |
| `crop_to_fill` | Par défaut, l'image est affichée en letterbox lorsque le rapport hauteur/largeur de sortie diffère. Activer cette option pour recadrer l'image afin de remplir les dimensions de sortie (par défaut : False). | BOOLEAN | Non | - |
| `output_width` | Une valeur nulle signifie que la largeur est calculée automatiquement (généralement la taille d'origine ou `output_height` si elle est spécifiée) (par défaut : 0). | INT | Non | 0 - 32000 |
| `output_height` | Une valeur nulle signifie que la hauteur de sortie est identique à celle d'origine ou à `output_width` (par défaut : 0). | INT | Non | 0 - 32000 |
| `creativity` | Contrôle le niveau de créativité global de l'amélioration (par défaut : 3). | INT | Non | 1 - 9 |
| `face_preservation` | Préserver l'identité faciale des sujets (par défaut : True). | BOOLEAN | Non | - |
| `color_preservation` | Préserver les couleurs d'origine (par défaut : True). | BOOLEAN | Non | - |

**Remarque :** Ce nœud ne peut traiter qu'une seule image d'entrée. La fourniture d'un lot de plusieurs images entraînera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image de sortie améliorée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
