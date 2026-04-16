# AI Hairstyle & Makeup Style Generator Using Stable Diffusion

## Project Overview
This project builds a controlled image generation system using Stable Diffusion.  
The system takes structured beauty-related inputs such as hairstyle, hair color, makeup style, and occasion, then converts them into prompts to generate realistic face images.

## Scenario
Option 1: AI Hairstyle & Makeup Style Generator

## Goal
To compare naive prompts and structured prompts for controlled face image generation and evaluate the quality of generated outputs.

## Inputs
The system takes:
- hairstyle
- hair color
- makeup style
- occasion

## Methodology
1. Load structured input from a JSON file
2. Convert input into:
   - naive prompt
   - structured prompt
   - structured prompt + negative prompt
3. Generate multiple images using Stable Diffusion
4. Compare results
5. Evaluate outputs based on:
   - prompt alignment
   - consistency
   - diversity
   - visual quality

## Control Mechanisms
This project uses:
- structured prompt templates
- negative prompts

## Example Prompt
### Structured Prompt
A realistic portrait of a young woman with curly bob hairstyle, dark brown hair, soft glam makeup, suitable for a wedding, detailed face, realistic skin, high quality, professional lighting

### Negative Prompt
blurry, low quality, distorted face, extra eyes, extra nose, bad anatomy, unrealistic hair, deformed face, poorly drawn face

## Files
- `generate.py`: main script for image generation
- `sample_inputs.json`: structured input cases
- `requirements.txt`: required Python libraries

## Installation
```bash
pip install -r requirements.txt
