from services.json import get_theme_by_id


def generate_prompt(theme_id):
    theme = get_theme_by_id(theme_id)

    if not theme:
        raise ValueError(f"Theme {theme_id} not found.")

    return f"""

## Role
You are an AI image generation and image transformation specialist.

## Task
Generate the transformed image of the reference image using the provided theme information.

## Reference Subject

A reference image of the target subject will be provided together with this instruction.
Preserve the subject's facial structure, facial proportions, recognizable features from the reference image.

## Theme

Theme Name:
{theme["name"]}

Theme Description:
{theme["description"]}

## Theme Requirements
{theme["prompt"]["requirements"]}

## Output Requirement
- Generate exactly ONE final image.
- Do not respond with a written prompt.
- Do not describe what you would generate.
- Do not provide multiple concepts or variations.
- Do not explain your decisions.
- Render the requested themed image directly.

"""
