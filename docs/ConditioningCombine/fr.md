Ce nœud combine deux entrées de conditionnement en une seule sortie, fusionnant efficacement leurs informations.

## Types d'entrée

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning_1`      | `CONDITIONING`     | La première entrée de conditionnement à combiner. Elle joue un rôle égal avec `conditioning_2` dans le processus de combinaison. |
| `conditioning_2`      | `CONDITIONING`     | La deuxième entrée de conditionnement à combiner. Elle est tout aussi importante que `conditioning_1` dans le processus de fusion. |

## Types de sortie

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | Le résultat de la combinaison de `conditioning_1` et `conditioning_2`, encapsulant les informations fusionnées. |