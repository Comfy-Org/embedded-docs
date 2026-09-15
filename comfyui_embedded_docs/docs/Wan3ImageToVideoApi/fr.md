# Wan 3.0 Image vers vidéo

Ce nœud génère une vidéo à partir d'une image de début en utilisant le modèle Wan 3.0. Vous pouvez éventuellement fournir une image de fin pour contrôler la fin de la vidéo ; le modèle crée alors une vidéo qui effectue une transition de la première à la dernière image.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélectionne la variante du modèle Wan 3.0 à utiliser et détermine quels paramètres spécifiques au modèle sont affichés ci-dessous. | DYNAMIC_COMBO | Oui | "wan3.0-video"<br>"wan3.0-video-prime" |
| `first_frame` | Image de la première frame. Exactement une image est requise. | IMAGE | Oui | Image unique |
| `last_frame` | Image de la dernière frame. Le modèle génère une vidéo effectuant une transition de la première à la dernière frame. Facultatif ; si fourni, exactement une image est requise. | IMAGE | Non | Image unique |
| `seed` | Graine à utiliser pour la génération (par défaut : 42). | INT | Oui | 0 - 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : false). | BOOLEAN | Oui | true<br>false |

### Entrées wan3.0-video et wan3.0-video-prime

Ces paramètres spécifiques au modèle sont partagés par les deux options de modèle et apparaissent lorsqu'un modèle est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. Peut être laissé vide (par défaut : vide). | STRING | Oui | Jusqu'à 20000 caractères |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Format d'image de la vidéo de sortie. Avec "adaptive", les dimensions de sortie sont dérivées de la première frame. | COMBO | Oui | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Durée de sortie en secondes. Avec "auto", le modèle choisit une durée adaptée au prompt. | COMBO | Oui | "auto"<br>"2" - "30" |
| `audio` | Indique si la vidéo de sortie contient une piste audio (par défaut : true). | BOOLEAN | Oui | true<br>false |
| `prompt_extend` | Indique s'il faut améliorer le prompt avec l'assistance de l'IA (par défaut : true). | BOOLEAN | Oui | true<br>false |

Remarque : Le nœud accepte exactement une image `first_frame` et éventuellement une image `last_frame`. Si plusieurs images sont connectées à l'une ou l'autre des entrées, une erreur est générée. Lorsque `last_frame` est fourni, la vidéo générée effectue une transition de la première à la dernière frame. Le `prompt` est limité à 20 000 caractères. Le prix d'une exécution dépend du `model`, de la `resolution` et de la `duration` sélectionnés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée. Contient une piste audio lorsque l'option `audio` est activée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
