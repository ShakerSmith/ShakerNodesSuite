# ShakerNodesSuite-0.2
Comfyui nodes for saving, combining, building, randomizing prompts

1. 
INSTALL:

Add this suite to "/ComfyUI/custom_nodes"

in cmd console: git clone https://github.com/ShakerSmith/ShakerNodesSuite

2. OPEN THE INCLUDED EXAMPLE "TUTORIAL" WORKFLOW: 

TUTORIAL WORKLOW: <img width="832" height="1248" alt="ShakerNodes-Tutorial" src="https://github.com/user-attachments/assets/f7d5071b-2543-4e54-9b02-49fac734d1b4" />

NODES IN THIS SUITE:

Prompt Builder:

<img width="488" height="347" alt="546561546-364eec63-7718-441f-a75e-188744aa4767" src="https://github.com/user-attachments/assets/4b1100f7-675b-4f72-8d0b-d3515154fc93" />

"Categories" "Presets" "Scenes"

A: Categories - contain "presets" and, on reload, will generate a new node for each category. That category's node will contain all the presets saved in that category.

B: Presets - presets contain the actual prompt text you want to be sent to the final prompt.
each "category" node can be set to manual (choose ONE preset), random all (randomly choose from ALL presets in that category), or random select (choose from only the presets user selects)

C: Scenes - contain the randomization modes and any preset selections for all loaded nodes in this nodesuite

3. Preset Manager / Scene Manager

<img width="614" height="233" alt="PresetManager" src="https://github.com/user-attachments/assets/5bfaed00-5f26-49bf-b3f8-751de33cec97" />


open the "PM" floating button, or "Preset Manager" on the Dashboard node. Add categories, reorder them, add/edit presets. can be pinned to the top or bottom of their category node. (default is alphabetical sorting)
open the "SM" floating button, or "Scene Manager" on the Dashboard node. Can "capture" the current state of all your nodes and quickly load captures scenes.

ADDING A NEW CATEGORY REQUIRES A COMFYUI RESTART. The Prompt Builder Console, on restart, will have a new input for your new category. There will ALSO be a new node available for you to connect to the Prompt Builder Console. Build order can be changed in the "edit categories" mode of the Preset Manager (floating "PM" button)


Metadata Filter,
will take all the LABELS of your presets and output them, can be turned on an off by category in the right-click node properties panel.

Big Display - display any, right-click properties to change font size and color - visible at any zoom level

Advanced Image Save -can save as .png or .webp - has inputs for metadata and toggles for folder_by_date (YYYY-MM-DD), prefix timestamp for the file (HHMM), and a custom sub_directory.
0424_BW-Group-Varied-Elderly-Bored-Business Suit-GlassesBlack-Close-Up-Portrait-CityDayTrees

# 📏 Shaker Latent Generator

The **Shaker Latent Generator** is a specialized resolution-management node for ComfyUI. It eliminates the guesswork and "math fatigue" associated with setting up latents for different models, ensuring your dimensions are always optimized for the specific architecture you are using (SD1.5 or SDXL).

## 🚀 Why use this instead of the Empty Latent Image node?

In standard ComfyUI, you have to manually enter pixel dimensions. If you get the math wrong, or use a resolution that isn't a multiple of 8, you'll encounter artifacts or performance degradation. The Shaker Latent Generator automates this process using industry-standard aspect ratios.

---

## ✨ Key Features

### 1. Smart Architecture Presets
Switching between **Small (SD1.5)** and **Large (SDXL)** models usually requires changing your resolution to hit the "sweet spot" for those models. This node handles that transition with one click:
* **Large (SDXL):** Uses base resolutions optimized for the 1024x1024 training bucket (e.g., 1344 x 768 for Cinema).
* **Small (SD1.5):** Uses base resolutions optimized for the 512x512 / 768x768 range.

### 2. Pro Aspect Ratios
Stop looking up pixel counts. Choose from standard cinematic and photographic ratios:
* **Portrait** (2:3)
* **Wide** (3:2)
* **Cinema** (16:9)
* **Ultrawide** (2.39:1)

### 3. The "Divisible by 8" Safety Net
No matter what multiplier or custom size you use, the node automatically calculates the nearest value divisible by 8. This ensures your VAE and Sampler never encounter dimension-mismatch errors.

### 4. Dynamic Multipliers & Custom Sizes
* **Multiplier:** Want to generate at 1.5x or 2x resolution for high-res fixing? Just move the slider.
* **Custom Mode:** Need a specific size? Switch to "Custom" to use the manual width/height sliders while still benefiting from the auto-rounding logic.
* **Random Mode:** Let the node roll the dice on a random aspect ratio for every generation to find new compositions.
* 

# 📺 Shaker Live Preview Mirror

The **Shaker Live Preview Mirror** is a specialized utility node designed to enhance the visibility of your generation process. In complex or sprawling ComfyUI workflows, the sampler—and its tiny native preview—is often buried or far away from your control center. This node acts as a "remote monitor" that you can place anywhere in your graph.

## 🚀 Why use this?

Standard ComfyUI previews are tethered to the sampler node itself. If you are using the **Shaker Main Console** and other control nodes in one area of your workspace, you usually have to scroll back and forth to see the progress of your image. 

The **Live Preview Mirror** allows you to stay focused on your prompt settings while maintaining a clear view of the sampling process in real-time.

---

## ✨ Key Features

### 1. Zero-Impact Performance
The node has no functional outputs and does not process tensors or latents. It acts as a visual bridge, meaning it adds **zero overhead** to your generation speed or VRAM usage.

### 2. Strategic Placement
Place the Mirror wherever you want - Even if your KSampler is ten screens away, you'll see every step of the denoising process as it happens.

## 🛠 How to Use

1. **Add the Node:** Find it under `ShakerNodes -> Utility -> Live Preview Mirror 📺`.
2. **Position It:** Place it wherever you spend the most time during generation (usually near your prompt nodes).
3. **Queue Prompt:** As soon as a sampler starts working anywhere in your workflow, the Mirror will automatically pick up the signal and display the live progress.

---

# 🛠 Shaker Pipe System

The **Shaker Pipe System** is a workflow organization utility for ComfyUI. It solves the "Spaghetti Problem" by allowing you to bundle multiple wires into a single connection, keeping your graph clean and manageable without sacrificing flexibility.

## 🚀 Why use this?

As workflows grow, you often find yourself dragging 10+ wires (Model, VAE, Positive, Negative, Latent, etc.) across the screen. If you move a group of nodes, you have to reorganize every single wire. 

The **Shaker Pipe** allows you to "pack" all those outputs into one single "pipe" wire, transport it across your graph, and "unpack" exactly what you need on the other side.

---

## ✨ Key Features

### 1. Flexible Packing
The **Pipe Pack** node accepts any data type (images, latents, conditioning, models, or strings). It doesn't care what you feed it—it just bundles it securely for transport.

### 2. High-Capacity Unpacking
The **Pipe Unpack** node provides up to 20 output slots. It remembers the order in which you packed your data, allowing you to pull out specific elements exactly when you need them.

### 3. Daisy-Chaining
The Unpack node features a **pipe_pass** output. This allows you to tap into the pipe to grab a few variables, then pass the entire bundle forward to the next section of your workflow.

---

## 🛠 How to Use

### Packing
1. Add a **Shaker Pipe Pack** node.
2. Plug your various outputs (e.g., your Model, Positive Prompt, and Latent) into the `in` slots.
3. Connect the `SHAKER_PIPE` output to your long-distance destination.

### Unpacking
1. Add a **Shaker Pipe Unpack** node at the end of your pipe.
2. The outputs will correspond to the order you plugged them into the Pack node.
3. Use the `pipe_pass` output if you need to send the bundle further down the line to another Unpack node.

---

B. Batch Any - lazy batching, doesn't fault if any inputs get a null in


# 🎞️ Shaker Gradual Color Match

The **Shaker Gradual Color Match** is a specialized image processing node designed primarily for video workflows and batch processing. It allows you to unify the color profile of an entire image sequence based on a single reference frame, with the unique ability to transition the strength of the effect over time.

## 🚀 Why use this?

In AI-generated video or long batch runs, color drift is a common issue—the lighting or palette often shifts as the sequence progresses. While standard color matching applies a static fix, the **Gradual Color Match** allows for a controlled "hand-off." You can start with 0% matching and slowly ramp up to 100% (or vice versa), making it an essential tool for smooth transitions between different scenes or styles.

---

## ✨ Key Features

### 1. Strength Interpolation
Unlike static matchers, this node calculates a unique strength for every single frame in your batch.
* **Linear:** A straight-line transition from your start strength to your end strength.
* **Smoothstep:** A curved, organic transition that starts slow, speeds up in the middle, and tapers off at the end—perfect for cinematic easing.

### 2. Dual Match Modes
* **RGB Mode:** Individually matches the Red, Green, and Blue histograms. This is the best choice for corrected color shifts and "grading" one image to look like another.
* **Luminance Mode:** Matches only the brightness values while preserving the original color data. This is ideal for fixing "flicker" or exposure inconsistencies without changing the actual colors of the shot.

### 3. Reference-Based Consistency
By picking one "Gold Standard" image (the `reference_image`), you can ensure that an entire batch of 100+ frames adheres to that specific look, drastically reducing visual popping in video animations.

---

## 🛠 Inputs & Controls

| Input | Description |
| :--- | :--- |
| **batch_images** | The sequence of images (video frames) you want to modify. |
| **reference_image** | The image whose color/lighting profile you want to copy. |
| **start_strength** | The match intensity for the first frame (0.0 to 1.0). |
| **end_strength** | The match intensity for the final frame (0.0 to 1.0). |
| **interpolation** | Choose between `linear` or `smoothstep` for the transition curve. |
| **match_mode** | `RGB` for full color matching, or `Luminance` for brightness-only matching. |

---

## 🚀 Common Use Cases

* **Deflickering:** Set `match_mode` to `Luminance` and use a clear frame as a reference to stabilize shaky exposure in AI video.
* **Scene Transitions:** Use `start_strength: 0.0` and `end_strength: 1.0` to gradually pull a sequence into the color palette of a new environment.
* **Batch Uniformity:** Keep both strengths at `1.0` to force every image in a large batch to match a specific photographic style.


D. Timer Node - right click to change font size and color - visible at any zoom level



ONCE YOU'VE GOT THE HANG OF HOW THE SUITE WORKS - build whatever kind of UI you want, drag your category nodes where they make sense to you, pin presets to the top or bottom of the category node from the Preset Manager. 

HERE'S AN EXAMPLE OF A COMPACT WORKFLOW:


<img width="832" height="1248" alt="ShakerNodes-Compact" src="https://github.com/user-attachments/assets/fe31627a-98eb-452e-82b8-73df498b821d" />



<img width="1000" height="808" alt="5-Compact" src="https://github.com/user-attachments/assets/652aabe6-40fd-4903-9550-eca2f6a3a8c9" />
