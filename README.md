# AI Hairstyle & Makeup Style Generator Using Stable Diffusion

## Project Overview

This project builds a controlled image generation system using Stable Diffusion.
The system takes structured inputs such as hairstyle, hair color, makeup style, and occasion, then converts them into prompts to generate realistic face images.

## Scenario

Option 1: AI Hairstyle & Makeup Style Generator

## Goal

The goal of this project is to compare naive prompts and structured prompts for controlled image generation and evaluate the quality of the generated outputs.

## Inputs

The system takes the following structured inputs:

* hairstyle
* hair color
* makeup style
* occasion
* 
## Control Mechanisms

This project uses:
- structured prompt templates
- negative prompts
  
## Methodology

1. Load structured input from a JSON file
2. Convert input into:

   * naive prompt
   * structured prompt
   * structured prompt + negative prompt
3. Generate images using Stable Diffusion
4. Compare results
5. Evaluate outputs based on:

   * prompt alignment
   * consistency
   * diversity
   * visual quality

## Example Prompt

### Naive Prompt

A woman with curly brown hair

### Structured Prompt

A realistic portrait of a young woman with curly bob hairstyle, dark brown hair, soft glam makeup, suitable for a wedding, detailed face, realistic skin, high quality, professional lighting

### Negative Prompt

blurry, low quality, distorted face, extra eyes, extra nose, bad anatomy, unrealistic hair, deformed face, poorly drawn face

## Results

* Naive prompts produced lower-quality images with less control
* Structured prompts improved realism and detail
* Negative prompts reduced distortions and improved image clarity

## Limitations

* Slow performance due to CPU-based execution
* Limited number of generated images
* Some outputs may still contain minor visual artifacts

## AI Tools Used

* ChatGPT → code assistance and debugging
* Hugging Face → model access
* Python libraries → system implementation

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python generate.py
```

## Outputs

Generated images are saved in the `outputs/` folder.

## Conclusion

This project demonstrates that structured prompts and negative prompts significantly improve control and quality in AI image generation.
