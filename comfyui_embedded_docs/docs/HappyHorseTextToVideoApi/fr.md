# HappyHorse Texte vers Vidéo

Génère une vidéo à partir d'une invite texte en utilisant le modèle HappyHorse. Ce nœud envoie votre invite et vos paramètres à l'API HappyHorse, attend que la vidéo soit générée, puis télécharge le résultat.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle HappyHorse utilisé pour la génération, ainsi que ses sous-paramètres. La sélection d'un modèle détermine les sous-paramètres disponibles (voir les sections de modèle ci-dessous). | DYNAMIC_COMBO | Oui | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | Graine à utiliser pour la génération. Utiliser la même graine avec les mêmes entrées produira le même résultat. (défaut : 0). | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane généré par IA au résultat. (défaut : False). | BOOLEAN | Oui | True / False |

### happyhorse-1.1-t2v Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. (défaut : ""). | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | "720P"<br>"1080P" |
| `ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `duration` | La durée de la vidéo en secondes. (défaut : 5, min : 3, max : 15, pas : 1). | INT | Oui | 3 à 15 |

### happyhorse-1.0-t2v Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. (défaut : ""). | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | "720P"<br>"1080P" |
| `ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | La durée de la vidéo en secondes. (défaut : 5, min : 3, max : 15, pas : 1). | INT | Oui | 3 à 15 |

Remarque : l'invite ne doit pas être vide ; une erreur est levée si aucune invite n'est fournie. Les deux modèles prennent en charge des durées vidéo de 3 à 15 secondes. Le modèle `happyhorse-1.1-t2v` offre des rapports hauteur/largeur supplémentaires (`21:9`, `9:21`, `5:4`, `4:5`) qui ne sont pas disponibles avec `happyhorse-1.0-t2v`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`
