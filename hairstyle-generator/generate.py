import json
import os
from diffusers import StableDiffusionPipeline
import torch

# -----------------------------
# Configuration
# -----------------------------
MODEL_ID = "runwayml/stable-diffusion-v1-5"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

NEGATIVE_PROMPT = (
    "blurry, low quality, distorted face, extra eyes, extra nose, "
    "bad anatomy, unrealistic hair, deformed face, poorly drawn face"
)

# -----------------------------
# Prompt builders
# -----------------------------
def build_naive_prompt(item):
    return f"A woman with {item['hairstyle']} and {item['hair_color']} hair"

def build_structured_prompt(item):
    return (
        f"A realistic portrait of a young woman with {item['hairstyle']}, "
        f"{item['hair_color']} hair, {item['makeup_style']}, suitable for {item['occasion']}, "
        f"detailed face, realistic skin, high quality, professional lighting"
    )

# -----------------------------
# Load sample inputs
# -----------------------------
def load_inputs(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

# -----------------------------
# Main generation
# -----------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading Stable Diffusion model...")
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32
    )
    pipe = pipe.to(DEVICE)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "sample_inputs.json")
    inputs = load_inputs(input_path)

    for idx, item in enumerate(inputs, start=1):
        print(f"\nGenerating images for case {idx}...")

        naive_prompt = build_naive_prompt(item)
        structured_prompt = build_structured_prompt(item)

        prompt_versions = {
            "naive": {"prompt": naive_prompt, "negative_prompt": None},
            "structured": {"prompt": structured_prompt, "negative_prompt": None},
            "structured_negative": {
                "prompt": structured_prompt,
                "negative_prompt": NEGATIVE_PROMPT
            },
        }

        for version_name, prompt_data in prompt_versions.items():
            for image_num in range(1, 3):  # generate 2 images per version
                generator = torch.Generator(device=DEVICE).manual_seed(42 + image_num)

                result = pipe(
                    prompt=prompt_data["prompt"],
                    negative_prompt=prompt_data["negative_prompt"],
                    num_inference_steps=30,
                    guidance_scale=7.5,
                    generator=generator
               )
                image = result.images[0]
                filename = f"case{idx}_{version_name}_{image_num}.png"
                filepath = os.path.join(OUTPUT_DIR, filename)
                image.save(filepath)

                print(f"Saved: {filepath}")

    print("\nDone. All images are saved in the outputs folder.")

if __name__ == "__main__":
    main()
